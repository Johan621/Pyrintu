from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from .models import OpportunityProjection


def ensure_aware(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def ranking_id(projection: OpportunityProjection) -> UUID:
    return projection.opportunity_id if projection.opportunity_id is not None else projection.candidate_id


def projection_rank_key(projection: OpportunityProjection) -> tuple:
    evidence = projection.evidence_json or {}
    soft_match_count = evidence.get("soft_match_count")
    if not isinstance(soft_match_count, int):
        soft_match_count = 0

    cost = projection.estimated_cost_minor
    cost_sort = cost if isinstance(cost, int) else float("inf")

    expiry = projection.expires_at
    if expiry is not None:
        expiry_sort = ensure_aware(expiry)
    else:
        expiry_sort = datetime.max.replace(tzinfo=timezone.utc)

    created_at = projection.created_at
    if created_at is not None:
        created_sort = ensure_aware(created_at)
    else:
        created_sort = datetime.min.replace(tzinfo=timezone.utc)

    return (
        -soft_match_count,
        cost_sort,
        expiry_sort,
        created_sort,
        str(ranking_id(projection)),
    )
