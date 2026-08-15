from dataclasses import replace
from datetime import datetime, timedelta, timezone
from typing import Optional, Callable
from uuid import UUID

from pyrintu_matching.models import (
    Match,
    MatchParticipant,
    MatchStatus,
    ParticipantDecision,
    MutualityRevealState,
)
from pyrintu_matching.compatibility import CompatibilityResult, evaluate_compatibility


class PairwiseInvariantError(Exception):
    """Raised when pairwise invariant is violated."""
    pass


class MatchProvenanceError(Exception):
    """Raised when match provenance is invalid."""
    pass


class DuplicateMatchError(Exception):
    """Raised when attempting to create a duplicate match."""
    pass


class MatchingService:
    """
    Service for pairwise activity-based matching with deterministic compatibility.
    
    Key invariants:
    - Exactly 2 distinct participants per match
    - Match must be tied to a valid opportunity
    - Candidate generation is idempotent
    - No AI involvement in state transitions
    """
    
    def __init__(
        self,
        decision_window_hours: int = 48,
        now_provider: Optional[Callable[[], datetime]] = None,
    ):
        self._decision_window_hours = decision_window_hours
        self._now_provider = now_provider or (lambda: datetime.now(timezone.utc))
    
    def create_match(
        self,
        match_id: UUID,
        opportunity_id: UUID,
        user_a_id: UUID,
        user_b_id: UUID,
        now: Optional[datetime] = None,
    ) -> Match:
        """
        Create a new match with exactly 2 participants.
        
        Raises PairwiseInvariantError if pairwise invariant is violated.
        """
        now = now or self._now_provider()
        expires_at = now + timedelta(hours=self._decision_window_hours)
        
        # Validate pairwise invariant
        self._validate_pairwise_invariant(user_a_id, user_b_id)
        
        # Create match with CANDIDATE status
        match = Match(
            id=match_id,
            opportunity_id=opportunity_id,
            status=MatchStatus.CANDIDATE,
            created_at=now,
            updated_at=now,
            expires_at=expires_at,
            version=0,
            participants=(
                MatchParticipant(
                    match_id=match_id,
                    user_id=user_a_id,
                    decision=ParticipantDecision.PENDING,
                    decided_at=None,
                    mutuality_reveal_state=MutualityRevealState.PRIVATE,
                    created_at=now,
                    updated_at=now,
                ),
                MatchParticipant(
                    match_id=match_id,
                    user_id=user_b_id,
                    decision=ParticipantDecision.PENDING,
                    decided_at=None,
                    mutuality_reveal_state=MutualityRevealState.PRIVATE,
                    created_at=now,
                    updated_at=now,
                ),
            ),
        )
        
        return match
    
    def record_decision(
        self,
        match: Match,
        user_id: UUID,
        decision: ParticipantDecision,
        now: Optional[datetime] = None,
    ) -> Match:
        """
        Record a participant's decision and update match state accordingly.
        
        Raises PairwiseInvariantError if user is not a participant.
        """
        now = now or self._now_provider()
        
        # Find the participant
        participant = self._find_participant(match, user_id)
        if participant is None:
            raise PairwiseInvariantError(f"User {user_id} is not a participant in match {match.id}")
        
        # Update participant decision
        updated_participants = []
        for p in match.participants:
            if p.user_id == user_id:
                updated_participants.append(
                    replace(
                        p,
                        decision=decision,
                        decided_at=now if decision != ParticipantDecision.PENDING else None,
                        updated_at=now,
                    )
                )
            else:
                updated_participants.append(p)
        
        # Determine new match status based on decisions
        new_status = self._evaluate_match_status(updated_participants, match.status)
        
        # Update mutuality reveal state if mutuality achieved
        new_reveal_states = self._evaluate_mutuality_reveal(
            updated_participants,
            new_status,
        )
        
        # Apply reveal state updates
        final_participants = []
        for p, reveal_state in zip(updated_participants, new_reveal_states):
            final_participants.append(
                replace(p, mutuality_reveal_state=reveal_state)
            )
        
        # Update match
        updated_match = replace(
            match,
            status=new_status,
            participants=tuple(final_participants),
            updated_at=now,
            version=match.version + 1,
        )
        
        return updated_match
    
    def evaluate_mutuality(self, match: Match) -> bool:
        """
        Evaluate if match has achieved mutuality.
        
        Mutuality requires both participants to be INTERESTED.
        MAYBE does not count.
        NOT_INTERESTED prevents mutuality.
        """
        interested_count = sum(
            1 for p in match.participants if p.decision == ParticipantDecision.INTERESTED
        )
        return interested_count == 2
    
    def check_match_validity(
        self,
        match: Match,
        opportunity_expires_at: Optional[datetime],
        now: Optional[datetime] = None,
    ) -> bool:
        """
        Check if match is still valid.
        
        Match is invalid if:
        - It has expired (decision window or opportunity expiry)
        - It has been terminated
        """
        now = now or self._now_provider()
        
        if match.status == MatchStatus.TERMINATED:
            return False
        
        # Check decision window expiry
        if now >= match.expires_at:
            return False
        
        # Check opportunity expiry
        if opportunity_expires_at and now >= opportunity_expires_at:
            return False
        
        return True
    
    def handle_material_change(
        self,
        match: Match,
        now: Optional[datetime] = None,
    ) -> Match:
        """
        Handle material change by resetting match state.
        
        Material change effects:
        - Reset match status to SHOWN
        - Reset participant decisions to PENDING
        - Reset mutuality reveal state to PRIVATE
        - Require independent reconfirmation
        """
        now = now or self._now_provider()
        
        # Reset all participants to PENDING
        reset_participants = []
        for p in match.participants:
            reset_participants.append(
                replace(
                    p,
                    decision=ParticipantDecision.PENDING,
                    decided_at=None,
                    mutuality_reveal_state=MutualityRevealState.PRIVATE,
                    updated_at=now,
                )
            )
        
        # Reset match status to SHOWN
        updated_match = replace(
            match,
            status=MatchStatus.SHOWN,
            participants=tuple(reset_participants),
            updated_at=now,
            version=match.version + 1,
        )
        
        return updated_match
    
    def generate_candidates(
        self,
        opportunity_id: UUID,
        user_a_id: UUID,
        user_a_intent: dict,
        candidate_users: list[tuple[UUID, dict]],  # (user_id, intent_data)
        existing_matches: list[Match],
        now: Optional[datetime] = None,
    ) -> list[tuple[UUID, UUID, CompatibilityResult]]:
        """
        Generate candidate matches for compatible users.
        
        Returns list of (user_a_id, user_b_id, compatibility_result) for compatible pairs.
        This is idempotent - duplicate calls do not create duplicate matches.
        """
        now = now or self._now_provider()
        candidates = []
        
        # Extract user A intent data
        user_a_activity_id = user_a_intent.get("activity_id")
        user_a_constraints = user_a_intent.get("constraints", {})
        user_a_availability = user_a_intent.get("availability", {})
        
        # Check each candidate user
        for user_b_id, user_b_intent in candidate_users:
            # Skip if user B is the same as user A
            if user_b_id == user_a_id:
                continue
            
            # Check for existing match between this pair for this opportunity
            if self._has_existing_match(opportunity_id, user_a_id, user_b_id, existing_matches):
                continue
            
            # Extract user B intent data
            user_b_activity_id = user_b_intent.get("activity_id")
            user_b_constraints = user_b_intent.get("constraints", {})
            user_b_availability = user_b_intent.get("availability", {})
            
            # Evaluate compatibility
            compatibility = evaluate_compatibility(
                intent_a_activity_id=user_a_activity_id,
                intent_a_constraints=user_a_constraints,
                intent_a_availability=user_a_availability,
                intent_b_activity_id=user_b_activity_id,
                intent_b_constraints=user_b_constraints,
                intent_b_availability=user_b_availability,
            )
            
            if compatibility.compatible:
                candidates.append((user_a_id, user_b_id, compatibility))
        
        return candidates
    
    def _validate_pairwise_invariant(self, user_a_id: UUID, user_b_id: UUID) -> None:
        """Validate that exactly 2 distinct users are provided."""
        if user_a_id == user_b_id:
            raise PairwiseInvariantError("Cannot create match with same user twice")
    
    def _find_participant(self, match: Match, user_id: UUID) -> Optional[MatchParticipant]:
        """Find a participant by user ID."""
        for p in match.participants:
            if p.user_id == user_id:
                return p
        return None
    
    def _evaluate_match_status(
        self,
        participants: list[MatchParticipant],
        current_status: MatchStatus,
    ) -> MatchStatus:
        """Evaluate new match status based on participant decisions."""
        decisions = [p.decision for p in participants]
        
        # If any participant is NOT_INTERESTED, terminate
        if ParticipantDecision.NOT_INTERESTED in decisions:
            return MatchStatus.TERMINATED
        
        # Count interested participants
        interested_count = sum(1 for d in decisions if d == ParticipantDecision.INTERESTED)
        
        # If both are INTERESTED, achieve mutuality
        if interested_count == 2:
            return MatchStatus.MUTUAL_INTEREST
        
        # If one is INTERESTED, move to USER_INTEREST
        if interested_count == 1:
            return MatchStatus.USER_INTEREST
        
        # Otherwise, maintain current status or move to SHOWN
        if current_status == MatchStatus.CANDIDATE:
            return MatchStatus.SHOWN
        
        return current_status
    
    def _evaluate_mutuality_reveal(
        self,
        participants: list[MatchParticipant],
        match_status: MatchStatus,
    ) -> list[MutualityRevealState]:
        """Evaluate mutuality reveal states based on match status."""
        if match_status in (MatchStatus.MUTUAL_INTEREST, MatchStatus.CONNECTION_ELIGIBLE):
            # Reveal to participants when mutuality achieved
            return [MutualityRevealState.REVEALED_TO_PARTICIPANTS] * len(participants)
        
        # Otherwise, keep private
        return [MutualityRevealState.PRIVATE] * len(participants)
    
    def _has_existing_match(
        self,
        opportunity_id: UUID,
        user_a_id: UUID,
        user_b_id: UUID,
        existing_matches: list[Match],
    ) -> bool:
        """
        Check if an existing match exists for this opportunity and participant pair.
        
        This ensures idempotent candidate generation.
        """
        for match in existing_matches:
            if match.opportunity_id != opportunity_id:
                continue
            
            participant_ids = {p.user_id for p in match.participants}
            if user_a_id in participant_ids and user_b_id in participant_ids:
                # Check if match is still active (not terminated)
                if match.status != MatchStatus.TERMINATED:
                    return True
        
        return False
