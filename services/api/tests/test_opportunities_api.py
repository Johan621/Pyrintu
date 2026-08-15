from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID, uuid4

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./pyrintu-test.db"
os.environ["PYRINTU_AUTH_MODE"] = "development"

from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import func, select

from pyrintu_api.db import SessionLocal
from pyrintu_api.main import app
from pyrintu_api.models import ActivityRecord, OpportunityRecord
from pyrintu_api.opportunity_repository import DuplicateOpportunityError, OpportunityRepository
from pyrintu_api.seeds.mvp_activities import (
    ACTIVITY_BUDGET_FRIENDLY_ID,
    ACTIVITY_CHILL_WEEKEND_HYDERABAD_ID,
    seed_mvp_activities,
)

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "pyrintu-test.db"


def _migrate() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    command.upgrade(Config(str(BASE_DIR / "alembic.ini")), "head")


def _prepare_db() -> None:
    import asyncio

    _migrate()
    asyncio.run(_seed_catalog())


async def _seed_catalog() -> None:
    async with SessionLocal() as session:
        await seed_mvp_activities(session)


_migrate()
import asyncio

asyncio.run(_seed_catalog())


def _create_submitted_intent(client: TestClient, user_id, text: str) -> str:
    headers = {"X-User-ID": str(user_id)}
    created = client.post("/api/v1/intents", json={"text": text}, headers=headers)
    intent_id = created.json()["id"]
    submitted = client.post(
        f"/api/v1/intents/{intent_id}/submit",
        json={"expected_version": 1},
        headers=headers,
    )
    assert submitted.status_code == 200
    return intent_id


async def _count_opportunities() -> int:
    async with SessionLocal() as session:
        return await session.scalar(select(func.count()).select_from(OpportunityRecord)) or 0


def test_opportunities_requires_authentication() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/opportunities")
        assert response.status_code == 401


def test_opportunities_requires_submitted_intent() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        created = client.post("/api/v1/intents", json={"text": "Go hiking"}, headers=headers)
        assert created.status_code == 201
        response = client.get("/api/v1/opportunities", headers=headers)
        assert response.status_code == 409
        assert response.json()["detail"] == "INVALID_STATE"


def test_get_is_read_only() -> None:
    import asyncio

    before = asyncio.run(_count_opportunities())
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 4 people this weekend nearby under 500",
        )
        response = client.get("/api/v1/opportunities", headers=headers)
        assert response.status_code == 200
        assert response.json()["opportunities"]
    after = asyncio.run(_count_opportunities())
    assert before == after


def test_two_users_owner_isolation() -> None:
    owner = uuid4()
    other = uuid4()
    with TestClient(app) as client:
        owner_intent = _create_submitted_intent(
            client,
            owner,
            "I want something chill with 3 people this weekend nearby under 500",
        )
        other_intent = _create_submitted_intent(
            client,
            other,
            "Networking with 12 people under 1000",
        )

        owner_response = client.get("/api/v1/opportunities", headers={"X-User-ID": str(owner)})
        other_response = client.get("/api/v1/opportunities", headers={"X-User-ID": str(other)})

        assert owner_response.status_code == 200
        assert other_response.status_code == 200

        owner_body = owner_response.json()["opportunities"]
        other_body = other_response.json()["opportunities"]

        assert owner_body
        assert other_body
        assert all(item["intent_id"] == owner_intent for item in owner_body)
        assert all(item["intent_id"] == other_intent for item in other_body)
        assert {item["what_label"] for item in owner_body} != {item["what_label"] for item in other_body}


def test_opportunities_uses_latest_submitted_intent() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 3 people this weekend nearby under 500",
        )
        second_id = _create_submitted_intent(
            client,
            user_id,
            "Networking with 12 people under 1000",
        )

        response = client.get("/api/v1/opportunities", headers=headers)
        assert response.status_code == 200
        for item in response.json()["opportunities"]:
            assert item["intent_id"] == second_id


def test_budget_exclusion() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 4 people this weekend nearby under 500",
        )
        response = client.get("/api/v1/opportunities", headers=headers)
        summaries = response.json()["opportunities"]
        assert all(
            item.get("estimated_cost_minor", 0) <= 500
            for item in summaries
            if item.get("estimated_cost_minor") is not None
        )
        assert not any(item["what_label"] == "Premium dining" for item in summaries)


def test_group_size_exclusion() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 3 people this weekend nearby under 500",
        )
        summaries = client.get("/api/v1/opportunities", headers=headers).json()["opportunities"]
        assert all(item.get("group_size", 0) <= 3 for item in summaries if item.get("group_size"))
        assert not any(item["what_label"] == "Networking mixer" for item in summaries)


def test_expired_activity_not_returned() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 3 people this weekend nearby under 500",
        )
        summaries = client.get("/api/v1/opportunities", headers=headers).json()["opportunities"]
        assert not any(item["what_label"] == "Morning walk" for item in summaries)


def test_inactive_activity_not_returned() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 3 people this weekend nearby under 500",
        )
        summaries = client.get("/api/v1/opportunities", headers=headers).json()["opportunities"]
        assert not any(item["what_label"] == "Studio session" for item in summaries)


def test_hidden_opportunity_excluded() -> None:
    import asyncio

    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        intent_id = _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 4 people this weekend nearby under 500",
        )

        async def _insert_hidden() -> None:
            async with SessionLocal() as session:
                session.add(
                    OpportunityRecord(
                        user_id=user_id,
                        intent_id=UUID(intent_id),
                        candidate_type="ACTIVITY",
                        candidate_id=ACTIVITY_CHILL_WEEKEND_HYDERABAD_ID,
                        visibility_state="HIDDEN",
                        evidence_json={"soft_match_count": 0},
                        created_at=datetime.now(timezone.utc),
                    )
                )
                await session.commit()

        asyncio.run(_insert_hidden())

        summaries = client.get("/api/v1/opportunities", headers=headers).json()["opportunities"]
        assert not any(item["what_label"] == "Badminton + Café" for item in summaries)


def test_empty_eligible_result() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 3 people this weekend nearby under 50",
        )
        response = client.get("/api/v1/opportunities", headers=headers)
        assert response.status_code == 200
        assert response.json()["opportunities"] == []


def test_exact_ranking_order() -> None:
    import asyncio

    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 4 people this weekend nearby under 500",
        )

        async def _adjust_created_at() -> None:
            async with SessionLocal() as session:
                board_games = await session.get(ActivityRecord, ACTIVITY_BUDGET_FRIENDLY_ID)
                cafe = await session.scalar(
                    select(ActivityRecord).where(ActivityRecord.name == "Relaxed café hangout")
                )
                assert board_games is not None and cafe is not None
                board_games.created_at = datetime(2026, 1, 2, tzinfo=timezone.utc)
                cafe.created_at = datetime(2026, 1, 1, tzinfo=timezone.utc)
                await session.commit()

        asyncio.run(_adjust_created_at())

        summaries = client.get("/api/v1/opportunities", headers=headers).json()["opportunities"]
        labels = [item["what_label"] for item in summaries]
        assert labels.index("Board games") < labels.index("Café conversation")


def test_evidence_projection_and_no_internal_json_leakage() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 3 people this weekend nearby under 500",
        )
        item = client.get("/api/v1/opportunities", headers=headers).json()["opportunities"][0]
        assert "evidence_json" not in item
        assert "fit_signals" not in item
        assert "soft_match_count" not in item
        assert item["why_this_fits"]
        assert "matched" not in item["why_this_fits"][0]


def test_duplicate_opportunity_protection() -> None:
    import asyncio

    user_id = uuid4()
    repo = OpportunityRepository()

    with TestClient(app) as client:
        intent_id = _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 3 people this weekend nearby under 500",
        )

        intent_uuid = UUID(intent_id)

        async def _create_twice() -> None:
            async with SessionLocal() as session:
                await repo.create_opportunity(
                    session,
                    user_id=user_id,
                    intent_id=intent_uuid,
                    candidate_type="ACTIVITY",
                    candidate_id=ACTIVITY_BUDGET_FRIENDLY_ID,
                    visibility_state="ACTIVE",
                    evidence_json={"soft_match_count": 1},
                )
                try:
                    await repo.create_opportunity(
                        session,
                        user_id=user_id,
                        intent_id=intent_uuid,
                        candidate_type="ACTIVITY",
                        candidate_id=ACTIVITY_BUDGET_FRIENDLY_ID,
                        visibility_state="ACTIVE",
                        evidence_json={"soft_match_count": 1},
                    )
                except DuplicateOpportunityError:
                    return
                raise AssertionError("expected duplicate opportunity insert to fail")

        asyncio.run(_create_twice())


def test_opportunities_reference_catalog_activities() -> None:
    user_id = uuid4()
    with TestClient(app) as client:
        headers = {"X-User-ID": str(user_id)}
        _create_submitted_intent(
            client,
            user_id,
            "I want something chill with 4 people this weekend nearby under 500",
        )
        labels = {
            item["what_label"]
            for item in client.get("/api/v1/opportunities", headers=headers).json()["opportunities"]
        }
        assert "Board games" in labels or "Café conversation" in labels
