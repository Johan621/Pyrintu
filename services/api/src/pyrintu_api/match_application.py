from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from pyrintu_api.match_repository import (
    MatchRepository,
    MatchNotFoundError,
)
from pyrintu_api.match_schemas import (
    MatchResponse,
    MatchDecisionRequest,
    MutualityResponse,
)
from pyrintu_matching.models import (
    Match,
    MatchStatus,
    ParticipantDecision,
    MutualityRevealState,
)
from pyrintu_matching.service import (
    MatchingService,
    PairwiseInvariantError,
)


class MatchApplicationService:
    """
    Application service for match operations.
    
    Orchestrates between repository, matching service, and API layer.
    """
    
    def __init__(
        self,
        matching_service: MatchingService,
        decision_window_hours: int = 48,
    ):
        self._matching_service = matching_service
        self._decision_window_hours = decision_window_hours
        self._repository = MatchRepository()
    
    async def get_match(
        self,
        session: AsyncSession,
        match_id: UUID,
        requesting_user_id: UUID,
    ) -> MatchResponse:
        """
        Get a match by ID.
        
        Raises MatchNotFoundError if match not found.
        Raises PermissionError if user is not a participant.
        """
        match = await self._repository.get_match_by_id(session, match_id)
        
        # Authorization: user must be a participant
        participant_ids = {p.user_id for p in match.participants}
        if requesting_user_id not in participant_ids:
            raise PermissionError(f"User {requesting_user_id} is not a participant in match {match_id}")
        
        # Build response
        return self._build_match_response(match)
    
    async def record_decision(
        self,
        session: AsyncSession,
        match_id: UUID,
        requesting_user_id: UUID,
        request: MatchDecisionRequest,
    ) -> MatchResponse:
        """
        Record a participant's decision.
        
        Raises MatchNotFoundError if match not found.
        Raises PermissionError if user is not a participant.
        Raises ValueError for invalid decision.
        Raises PairwiseInvariantError for pairwise invariant violations.
        """
        match = await self._repository.get_match_by_id(session, match_id)
        
        # Authorization: user must be a participant
        participant_ids = {p.user_id for p in match.participants}
        if requesting_user_id not in participant_ids:
            raise PermissionError(f"User {requesting_user_id} is not a participant in match {match_id}")
        
        # Validate decision
        try:
            decision = ParticipantDecision(request.decision)
        except ValueError:
            raise ValueError(f"Invalid decision: {request.decision}")
        
        # Validate version if provided
        if request.expected_version is not None and match.version != request.expected_version:
            raise ValueError(f"Version mismatch: expected {request.expected_version}, got {match.version}")
        
        # Check match validity
        opportunity = await self._repository.get_opportunity(session, match.opportunity_id)
        is_valid = self._matching_service.check_match_validity(
            match,
            opportunity.expires_at,
        )
        if not is_valid:
            raise ValueError("Match has expired or is no longer valid")
        
        # Record decision using matching service
        updated_match = self._matching_service.record_decision(
            match,
            requesting_user_id,
            decision,
        )
        
        # Persist to database
        await self._repository.update_match(session, updated_match)
        
        # Build response
        return self._build_match_response(updated_match)
    
    async def get_mutuality_state(
        self,
        session: AsyncSession,
        match_id: UUID,
        requesting_user_id: UUID,
    ) -> MutualityResponse:
        """
        Get mutuality state for a match.
        
        Raises MatchNotFoundError if match not found.
        Raises PermissionError if user is not a participant.
        """
        match = await self._repository.get_match_by_id(session, match_id)
        
        # Authorization: user must be a participant
        participant_ids = {p.user_id for p in match.participants}
        if requesting_user_id not in participant_ids:
            raise PermissionError(f"User {requesting_user_id} is not a participant in match {match_id}")
        
        # Evaluate mutuality
        is_mutual = self._matching_service.evaluate_mutuality(match)
        
        # Count interested participants
        interested_count = sum(
            1 for p in match.participants if p.decision == ParticipantDecision.INTERESTED
        )
        
        # Determine reveal state (use requesting user's reveal state)
        requesting_participant = next(
            p for p in match.participants if p.user_id == requesting_user_id
        )
        
        # Build response
        return MutualityResponse(
            match_id=match.id,
            status=match.status.value,
            is_mutual=is_mutual,
            participant_count=match.participant_count,
            interested_count=interested_count,
            mutuality_reveal_state=requesting_participant.mutuality_reveal_state.value,
        )
    
    def _build_match_response(self, match: Match) -> MatchResponse:
        """Build a MatchResponse from a Match domain model."""
        from pyrintu_api.match_schemas import MatchParticipantSummary
        
        participants = [
            MatchParticipantSummary(
                user_id=p.user_id,
                decision=p.decision.value,
                decided_at=p.decided_at,
                mutuality_reveal_state=p.mutuality_reveal_state.value,
            )
            for p in match.participants
        ]
        
        return MatchResponse(
            id=match.id,
            opportunity_id=match.opportunity_id,
            status=match.status.value,
            created_at=match.created_at,
            updated_at=match.updated_at,
            expires_at=match.expires_at,
            version=match.version,
            participants=participants,
        )
