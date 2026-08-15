from __future__ import annotations

from datetime import datetime, timezone

from pyrintu_discovery import ActivitySnapshot, CandidateType, IntentSnapshot, PersistedOpportunitySnapshot, VisibilityState

from .models import ActivityRecord, IntentRecord, OpportunityRecord


def ensure_aware(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def parse_metadata_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def activity_snapshot_from_record(record: ActivityRecord) -> ActivitySnapshot:
    metadata = record.metadata_json or {}
    time_tags = metadata.get("time_tags") or []
    if not isinstance(time_tags, list):
        time_tags = []

    return ActivitySnapshot(
        activity_id=record.id,
        name=record.name,
        category=record.category,
        description=record.description,
        status=record.status,
        group_size=metadata.get("group_size") if isinstance(metadata.get("group_size"), int) else None,
        estimated_cost_minor=metadata.get("estimated_cost_minor")
        if isinstance(metadata.get("estimated_cost_minor"), int)
        else None,
        currency=metadata.get("currency") if isinstance(metadata.get("currency"), str) else None,
        environment=metadata.get("environment") if isinstance(metadata.get("environment"), str) else None,
        time_tags=tuple(str(tag) for tag in time_tags),
        location_label=metadata.get("location_label") if isinstance(metadata.get("location_label"), str) else None,
        when_label=metadata.get("when_label") if isinstance(metadata.get("when_label"), str) else None,
        what_label=metadata.get("what_label") if isinstance(metadata.get("what_label"), str) else None,
        expires_at=parse_metadata_datetime(metadata.get("expires_at"))
        if isinstance(metadata.get("expires_at"), str)
        else None,
        created_at=ensure_aware(record.created_at),
    )


def intent_snapshot_from_record(record: IntentRecord) -> IntentSnapshot:
    return IntentSnapshot(
        intent_id=record.id,
        owner_user_id=record.owner_user_id,
        status=record.status,
        normalized_goal=record.normalized_goal_json or {},
        constraints=record.constraints_json or {},
        availability=record.availability_json or {},
        version=record.version,
    )


def persisted_opportunity_from_record(record: OpportunityRecord) -> PersistedOpportunitySnapshot:
    visibility = VisibilityState(record.visibility_state)
    return PersistedOpportunitySnapshot(
        opportunity_id=record.id,
        candidate_id=record.candidate_id,
        candidate_type=CandidateType(record.candidate_type),
        visibility_state=visibility,
        created_at=ensure_aware(record.created_at),
    )
