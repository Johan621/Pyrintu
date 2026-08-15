from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pyrintu_discovery import DiscoveryService, ranking_id

from .discovery_mappers import (
    activity_snapshot_from_record,
    intent_snapshot_from_record,
    persisted_opportunity_from_record,
)
from .models import ActivityRecord, IntentRecord, OpportunityRecord
from .opportunity_schemas import OpportunitySummary, WhyThisFitsItem


class NoSubmittedIntentError(Exception):
    pass


class DiscoveryApplicationService:
    def __init__(self, discovery_service: DiscoveryService | None = None) -> None:
        self._discovery_service = discovery_service or DiscoveryService()

    async def list_opportunities(self, session: AsyncSession, user_id: UUID) -> list[OpportunitySummary]:
        intent_record = await self._load_active_intent(session, user_id)
        if intent_record is None:
            raise NoSubmittedIntentError()

        intent = intent_snapshot_from_record(intent_record)
        activity_records = (
            await session.scalars(select(ActivityRecord).where(ActivityRecord.status == "ACTIVE"))
        ).all()
        activities = tuple(activity_snapshot_from_record(record) for record in activity_records)

        opportunity_records = (
            await session.scalars(
                select(OpportunityRecord).where(
                    OpportunityRecord.user_id == user_id,
                    OpportunityRecord.intent_id == intent.intent_id,
                )
            )
        ).all()
        persisted = tuple(persisted_opportunity_from_record(record) for record in opportunity_records)

        projections = self._discovery_service.discover(
            intent,
            activities,
            persisted_opportunities=persisted,
            now=datetime.now(timezone.utc),
        )
        return [self._summary_from_projection(projection) for projection in projections]

    async def _load_active_intent(self, session: AsyncSession, user_id: UUID) -> IntentRecord | None:
        return await session.scalar(
            select(IntentRecord)
            .where(
                IntentRecord.owner_user_id == user_id,
                IntentRecord.status == "SUBMITTED",
                IntentRecord.closed_at.is_(None),
            )
            .order_by(IntentRecord.updated_at.desc())
            .limit(1)
        )

    def _summary_from_projection(self, projection) -> OpportunitySummary:
        why_this_fits = [
            WhyThisFitsItem(signal_key=signal.signal_key, label=signal.label)
            for signal in projection.why_this_fits
        ]
        return OpportunitySummary(
            id=ranking_id(projection),
            intent_id=projection.intent_id,
            state=projection.state.value,
            fit_label=projection.fit_label.value,
            when_label=projection.when_label,
            what_label=projection.what_label,
            group_size=projection.group_size,
            location_label=projection.location_label,
            estimated_cost_minor=projection.estimated_cost_minor,
            currency=projection.currency,
            why_this_fits=why_this_fits,
            expires_at=projection.expires_at,
        )
