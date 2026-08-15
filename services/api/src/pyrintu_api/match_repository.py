from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pyrintu_api.models import (
    MatchRecord,
    MatchParticipantRecord,
    OpportunityRecord,
)
from pyrintu_api.datetime_utils import normalize_to_utc
from pyrintu_matching.models import (
    Match,
    MatchParticipant,
    MatchStatus,
    ParticipantDecision,
    MutualityRevealState,
)
from pyrintu_matching.mappers import (
    match_from_record,
    match_to_record,
    match_participant_from_record,
    match_participant_to_record,
)


class MatchNotFoundError(Exception):
    """Raised when a match is not found."""
    pass


class MatchRepository:
    """Repository for match persistence operations."""
    
    async def create_match(
        self,
        session: AsyncSession,
        match: Match,
    ) -> Match:
        """Create a new match with participants."""
        # Create match record
        match_record = MatchRecord(
            id=match.id,
            opportunity_id=match.opportunity_id,
            status=match.status.value,
            created_at=match.created_at,
            updated_at=match.updated_at,
            expires_at=match.expires_at,
            version=match.version,
        )
        session.add(match_record)
        
        # Create participant records
        for participant in match.participants:
            participant_record = MatchParticipantRecord(
                match_id=participant.match_id,
                user_id=participant.user_id,
                decision=participant.decision.value,
                decided_at=participant.decided_at,
                mutuality_reveal_state=participant.mutuality_reveal_state.value,
                created_at=participant.created_at,
                updated_at=participant.updated_at,
            )
            session.add(participant_record)
        
        await session.commit()
        await session.refresh(match_record)
        
        # Reload with participants
        return await self.get_match_by_id(session, match.id)
    
    async def get_match_by_id(
        self,
        session: AsyncSession,
        match_id: UUID,
    ) -> Match:
        """Get a match by ID with participants."""
        # Get match record
        match_result = await session.execute(
            select(MatchRecord).where(MatchRecord.id == match_id)
        )
        match_record = match_result.scalar_one_or_none()
        
        if match_record is None:
            raise MatchNotFoundError(f"Match {match_id} not found")
        
        # Get participant records
        participants_result = await session.execute(
            select(MatchParticipantRecord).where(
                MatchParticipantRecord.match_id == match_id
            )
        )
        participant_records = participants_result.scalars().all()
        
        # Build match domain model with normalized datetimes
        match_dict = {
            "id": match_record.id,
            "opportunity_id": match_record.opportunity_id,
            "status": match_record.status,
            "created_at": normalize_to_utc(match_record.created_at),
            "updated_at": normalize_to_utc(match_record.updated_at),
            "expires_at": normalize_to_utc(match_record.expires_at),
            "version": match_record.version,
            "participants": [
                {
                    "match_id": p.match_id,
                    "user_id": p.user_id,
                    "decision": p.decision,
                    "decided_at": normalize_to_utc(p.decided_at),
                    "mutuality_reveal_state": p.mutuality_reveal_state,
                    "created_at": normalize_to_utc(p.created_at),
                    "updated_at": normalize_to_utc(p.updated_at),
                }
                for p in participant_records
            ],
        }
        
        return match_from_record(match_dict)
    
    async def get_matches_for_user(
        self,
        session: AsyncSession,
        user_id: UUID,
    ) -> list[Match]:
        """Get all matches for a user."""
        # Get participant records for user
        participants_result = await session.execute(
            select(MatchParticipantRecord).where(
                MatchParticipantRecord.user_id == user_id
            )
        )
        participant_records = participants_result.scalars().all()
        
        matches = []
        for participant_record in participant_records:
            try:
                match = await self.get_match_by_id(session, participant_record.match_id)
                matches.append(match)
            except MatchNotFoundError:
                # Skip if match not found (shouldn't happen with FK)
                continue
        
        return matches
    
    async def update_match(
        self,
        session: AsyncSession,
        match: Match,
    ) -> Match:
        """Update a match record."""
        # Get existing match record
        match_result = await session.execute(
            select(MatchRecord).where(MatchRecord.id == match.id)
        )
        match_record = match_result.scalar_one_or_none()
        
        if match_record is None:
            raise MatchNotFoundError(f"Match {match.id} not found")
        
        # Update match fields
        match_record.status = match.status.value
        match_record.updated_at = match.updated_at
        match_record.expires_at = match.expires_at
        match_record.version = match.version
        
        # Update participant records
        for participant in match.participants:
            participant_result = await session.execute(
                select(MatchParticipantRecord).where(
                    MatchParticipantRecord.match_id == match.id,
                    MatchParticipantRecord.user_id == participant.user_id,
                )
            )
            participant_record = participant_result.scalar_one_or_none()
            
            if participant_record:
                # Update existing
                participant_record.decision = participant.decision.value
                participant_record.decided_at = participant.decided_at
                participant_record.mutuality_reveal_state = participant.mutuality_reveal_state.value
                participant_record.updated_at = participant.updated_at
            else:
                # Create new (shouldn't happen in normal flow)
                new_participant_record = MatchParticipantRecord(
                    match_id=participant.match_id,
                    user_id=participant.user_id,
                    decision=participant.decision.value,
                    decided_at=participant.decided_at,
                    mutuality_reveal_state=participant.mutuality_reveal_state.value,
                    created_at=participant.created_at,
                    updated_at=participant.updated_at,
                )
                session.add(new_participant_record)
        
        await session.commit()
        await session.refresh(match_record)
        
        # Reload with participants
        return await self.get_match_by_id(session, match.id)
    
    async def get_opportunity(
        self,
        session: AsyncSession,
        opportunity_id: UUID,
    ) -> OpportunityRecord:
        """Get an opportunity by ID with normalized datetime."""
        result = await session.execute(
            select(OpportunityRecord).where(OpportunityRecord.id == opportunity_id)
        )
        opportunity = result.scalar_one_or_none()
        
        if opportunity is None:
            raise MatchNotFoundError(f"Opportunity {opportunity_id} not found")
        
        # Normalize expires_at to timezone-aware UTC
        if opportunity.expires_at is not None:
            opportunity.expires_at = normalize_to_utc(opportunity.expires_at)
        
        return opportunity
    
    async def find_existing_match(
        self,
        session: AsyncSession,
        opportunity_id: UUID,
        user_a_id: UUID,
        user_b_id: UUID,
    ) -> Match | None:
        """
        Find an existing match for this opportunity and participant pair.
        
        Used for idempotent candidate generation.
        """
        # Find matches for this opportunity
        matches_result = await session.execute(
            select(MatchRecord).where(MatchRecord.opportunity_id == opportunity_id)
        )
        match_records = matches_result.scalars().all()
        
        for match_record in match_records:
            # Get participants for this match
            participants_result = await session.execute(
                select(MatchParticipantRecord).where(
                    MatchParticipantRecord.match_id == match_record.id
                )
            )
            participant_records = participants_result.scalars().all()
            
            participant_ids = {p.user_id for p in participant_records}
            
            # Check if both users are participants
            if user_a_id in participant_ids and user_b_id in participant_ids:
                # Check if match is not terminated
                if match_record.status != "TERMINATED":
                    return await self.get_match_by_id(session, match_record.id)
        
        return None
