from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .models import OpportunityRecord


class DuplicateOpportunityError(Exception):
    pass


class OpportunityRepository:
    async def create_opportunity(
        self,
        session: AsyncSession,
        user_id: UUID,
        intent_id: UUID,
        candidate_type: str,
        candidate_id: UUID,
        visibility_state: str,
        evidence_json: dict,
        expires_at: datetime | None = None,
    ) -> OpportunityRecord:
        record = OpportunityRecord(
            user_id=user_id,
            intent_id=intent_id,
            candidate_type=candidate_type,
            candidate_id=candidate_id,
            visibility_state=visibility_state,
            evidence_json=evidence_json,
            expires_at=expires_at,
            created_at=datetime.now(timezone.utc),
        )
        session.add(record)
        try:
            await session.commit()
        except IntegrityError as exc:
            await session.rollback()
            raise DuplicateOpportunityError() from exc
        await session.refresh(record)
        return record
