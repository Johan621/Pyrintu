"""MVP structured activity catalog and idempotent seed helpers."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pyrintu_api.models import ActivityRecord

# Fixed IDs keep local/test environments deterministic.
ACTIVITY_CHILL_WEEKEND_NEARBY_ID = UUID("11111111-1111-4111-8111-111111111101")
ACTIVITY_CHILL_WEEKEND_HYDERABAD_ID = UUID("11111111-1111-4111-8111-111111111102")
ACTIVITY_EXPENSIVE_GROUP_ID = UUID("11111111-1111-4111-8111-111111111103")
ACTIVITY_LARGE_GROUP_ID = UUID("11111111-1111-4111-8111-111111111104")
ACTIVITY_EXPIRED_ID = UUID("11111111-1111-4111-8111-111111111105")
ACTIVITY_INACTIVE_ID = UUID("11111111-1111-4111-8111-111111111106")
ACTIVITY_BUDGET_FRIENDLY_ID = UUID("11111111-1111-4111-8111-111111111107")


def _expiry(now: datetime, days_from_now: int) -> str:
    return (now + timedelta(days=days_from_now)).replace(microsecond=0).isoformat()


def _past_expiry(now: datetime) -> str:
    return (now - timedelta(days=1)).replace(microsecond=0).isoformat()


def build_mvp_activity_catalog(now: datetime | None = None) -> list[dict]:
    """Return catalog rows with expiry timestamps anchored to `now`."""
    anchor = now or datetime.now(timezone.utc)
    return [
        {
            "id": ACTIVITY_CHILL_WEEKEND_NEARBY_ID,
            "name": "Relaxed café hangout",
            "category": "social",
            "description": "A relaxed café conversation nearby.",
            "status": "ACTIVE",
            "metadata_json": {
                "group_size": 3,
                "estimated_cost_minor": 300,
                "currency": "INR",
                "environment": "chill",
                "time_tags": ["weekend", "this weekend"],
                "location_label": "nearby",
                "when_label": "Saturday · 5:00 PM",
                "what_label": "Café conversation",
                "expires_at": _expiry(anchor, 7),
            },
        },
        {
            "id": ACTIVITY_CHILL_WEEKEND_HYDERABAD_ID,
            "name": "Badminton and café",
            "category": "sports",
            "description": "Badminton followed by a relaxed café stop.",
            "status": "ACTIVE",
            "metadata_json": {
                "group_size": 4,
                "estimated_cost_minor": 350,
                "currency": "INR",
                "environment": "chill",
                "time_tags": ["weekend", "sunday"],
                "location_label": "Hyderabad",
                "when_label": "Sunday · 6:30 PM",
                "what_label": "Badminton + Café",
                "expires_at": _expiry(anchor, 5),
            },
        },
        {
            "id": ACTIVITY_EXPENSIVE_GROUP_ID,
            "name": "Premium dining circle",
            "category": "dining",
            "description": "Higher-cost dining experience.",
            "status": "ACTIVE",
            "metadata_json": {
                "group_size": 4,
                "estimated_cost_minor": 900,
                "currency": "INR",
                "environment": "upscale",
                "time_tags": ["weekend"],
                "location_label": "nearby",
                "when_label": "Saturday · 8:00 PM",
                "what_label": "Premium dining",
                "expires_at": _expiry(anchor, 10),
            },
        },
        {
            "id": ACTIVITY_LARGE_GROUP_ID,
            "name": "Open networking mixer",
            "category": "networking",
            "description": "Larger-group networking event.",
            "status": "ACTIVE",
            "metadata_json": {
                "group_size": 12,
                "estimated_cost_minor": 200,
                "currency": "INR",
                "environment": "networking",
                "time_tags": ["weekend"],
                "location_label": "nearby",
                "when_label": "Saturday · 4:00 PM",
                "what_label": "Networking mixer",
                "expires_at": _expiry(anchor, 8),
            },
        },
        {
            "id": ACTIVITY_EXPIRED_ID,
            "name": "Past weekend walk",
            "category": "outdoors",
            "description": "Expired catalog activity.",
            "status": "ACTIVE",
            "metadata_json": {
                "group_size": 3,
                "estimated_cost_minor": 100,
                "currency": "INR",
                "environment": "chill",
                "time_tags": ["weekend"],
                "location_label": "nearby",
                "when_label": "Last Sunday · 10:00 AM",
                "what_label": "Morning walk",
                "expires_at": _past_expiry(anchor),
            },
        },
        {
            "id": ACTIVITY_INACTIVE_ID,
            "name": "Inactive studio session",
            "category": "creative",
            "description": "Inactive catalog activity.",
            "status": "INACTIVE",
            "metadata_json": {
                "group_size": 3,
                "estimated_cost_minor": 250,
                "currency": "INR",
                "environment": "creative",
                "time_tags": ["weekend"],
                "location_label": "nearby",
                "when_label": "Friday · 7:00 PM",
                "what_label": "Studio session",
                "expires_at": _expiry(anchor, 6),
            },
        },
        {
            "id": ACTIVITY_BUDGET_FRIENDLY_ID,
            "name": "Budget board games",
            "category": "games",
            "description": "Low-cost board game evening.",
            "status": "ACTIVE",
            "metadata_json": {
                "group_size": 3,
                "estimated_cost_minor": 150,
                "currency": "INR",
                "environment": "chill",
                "time_tags": ["weekend", "this weekend"],
                "location_label": "nearby",
                "when_label": "Saturday · 3:00 PM",
                "what_label": "Board games",
                "expires_at": _expiry(anchor, 6),
            },
        },
    ]


async def seed_mvp_activities(session: AsyncSession, now: datetime | None = None) -> int:
    """Insert MVP catalog activities that are not already present. Returns inserted count."""
    anchor = now or datetime.now(timezone.utc)
    inserted = 0
    for item in build_mvp_activity_catalog(anchor):
        existing = await session.get(ActivityRecord, item["id"])
        if existing is not None:
            continue
        session.add(
            ActivityRecord(
                id=item["id"],
                name=item["name"],
                category=item["category"],
                description=item["description"],
                metadata_json=item["metadata_json"],
                status=item["status"],
                created_at=anchor,
                updated_at=anchor,
            )
        )
        inserted += 1
    if inserted:
        await session.commit()
    return inserted


async def count_catalog_activities(session: AsyncSession) -> int:
    catalog_ids = [item["id"] for item in build_mvp_activity_catalog()]
    result = await session.scalars(select(ActivityRecord.id).where(ActivityRecord.id.in_(catalog_ids)))
    return len(result.all())
