from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from .eligibility import evaluate_eligibility
from .models import (
    ActivitySnapshot,
    CandidateType,
    IntentSnapshot,
    OpportunityProjection,
    PersistedOpportunitySnapshot,
    VisibilityState,
)
from .ranking import projection_rank_key


def build_evidence_json(activity: ActivitySnapshot, eligibility) -> dict:
    return {
        "when_label": activity.when_label,
        "what_label": activity.what_label or activity.name,
        "group_size": activity.group_size,
        "location_label": activity.location_label,
        "estimated_cost_minor": activity.estimated_cost_minor,
        "currency": activity.currency,
        "environment": activity.environment,
        "time_tags": list(activity.time_tags),
        "fit_label": eligibility.fit_label.value,
        "opportunity_state": eligibility.opportunity_state.value,
        "soft_match_count": eligibility.soft_match_count,
        "fit_signals": [
            {"signal_key": signal.signal_key, "label": signal.label, "matched": signal.matched}
            for signal in eligibility.fit_signals
        ],
    }


def build_projection(
    intent: IntentSnapshot,
    activity: ActivitySnapshot,
    eligibility,
    opportunity_id: UUID | None = None,
    created_at: datetime | None = None,
    visibility_state: VisibilityState = VisibilityState.ACTIVE,
) -> OpportunityProjection:
    matched_signals = tuple(signal for signal in eligibility.fit_signals if signal.matched)
    resolved_created_at = created_at if created_at is not None else activity.created_at

    return OpportunityProjection(
        opportunity_id=opportunity_id,
        intent_id=intent.intent_id,
        candidate_type=CandidateType.ACTIVITY,
        candidate_id=activity.activity_id,
        visibility_state=visibility_state,
        state=eligibility.opportunity_state,
        fit_label=eligibility.fit_label,
        when_label=activity.when_label,
        what_label=activity.what_label or activity.name,
        group_size=activity.group_size,
        location_label=activity.location_label,
        estimated_cost_minor=activity.estimated_cost_minor,
        currency=activity.currency,
        why_this_fits=matched_signals,
        expires_at=activity.expires_at,
        created_at=resolved_created_at,
        evidence_json=build_evidence_json(activity, eligibility),
    )


class DiscoveryService:
    def discover(
        self,
        intent: IntentSnapshot,
        activities: tuple[ActivitySnapshot, ...],
        persisted_opportunities: tuple[PersistedOpportunitySnapshot, ...] = (),
        now: datetime | None = None,
    ) -> tuple[OpportunityProjection, ...]:
        now = now or datetime.now(timezone.utc)
        persisted_by_candidate = {row.candidate_id: row for row in persisted_opportunities}

        projections: list[OpportunityProjection] = []
        for activity in activities:
            eligibility = evaluate_eligibility(intent, activity, now=now)
            if not eligibility.eligible:
                continue

            persisted = persisted_by_candidate.get(activity.activity_id)
            if persisted is not None and persisted.visibility_state == VisibilityState.HIDDEN:
                continue

            opportunity_id = persisted.opportunity_id if persisted is not None else None
            created_at = persisted.created_at if persisted is not None else activity.created_at
            visibility = persisted.visibility_state if persisted is not None else VisibilityState.ACTIVE

            projections.append(
                build_projection(
                    intent,
                    activity,
                    eligibility,
                    opportunity_id=opportunity_id,
                    created_at=created_at,
                    visibility_state=visibility,
                )
            )

        projections.sort(key=projection_rank_key)
        return tuple(projections)
