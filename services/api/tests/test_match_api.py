from __future__ import annotations

import os
import asyncio
from pathlib import Path
from uuid import uuid4

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./pyrintu-test.db"
os.environ["PYRINTU_AUTH_MODE"] = "development"

from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient

from pyrintu_api.main import app
from pyrintu_api.models import MatchRecord, MatchParticipantRecord, OpportunityRecord, IntentRecord
from pyrintu_api.db import SessionLocal
from pyrintu_matching.models import MatchStatus, ParticipantDecision, MutualityRevealState


BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "pyrintu-test.db"


def _migrate() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    config = Config(str(BASE_DIR / "alembic.ini"))
    command.upgrade(config, "head")


_migrate()


def _create_user(client, email):
    """Helper to generate a user ID (no user creation API needed for development mode)."""
    from uuid import uuid4
    return uuid4()


def _create_intent(client, user_id, raw_input):
    """Helper to create an intent using the Intent API."""
    response = client.post(
        "/api/v1/intents",
        json={"text": raw_input},
        headers={"X-User-ID": str(user_id)},
    )
    assert response.status_code == 201
    return response.json()["id"]


def _submit_intent(client, user_id, intent_id):
    """Helper to submit an intent using the Intent API."""
    response = client.post(
        f"/api/v1/intents/{intent_id}/submit",
        json={"expected_version": 1},
        headers={"X-User-ID": str(user_id)},
    )
    assert response.status_code == 200


async def _create_opportunity_directly_async(session, user_id, intent_id, candidate_id):
    """Helper to create an opportunity directly in the database using async session."""
    import uuid
    from datetime import datetime, timezone, timedelta
    
    # Convert string IDs to UUID if needed
    if isinstance(intent_id, str):
        intent_id = uuid.UUID(intent_id)
    if isinstance(candidate_id, str):
        candidate_id = uuid.UUID(candidate_id)
    
    opportunity = OpportunityRecord(
        id=uuid.uuid4(),
        user_id=user_id,
        intent_id=intent_id,
        candidate_type="ACTIVITY",
        candidate_id=candidate_id,
        visibility_state="ACTIVE",
        evidence_json={},
        created_at=datetime.now(timezone.utc),
        expires_at=datetime.now(timezone.utc) + timedelta(days=7),
    )
    session.add(opportunity)
    await session.commit()
    await session.refresh(opportunity)
    return opportunity.id


async def _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id):
    """Helper to create a match directly in the database using async session."""
    import uuid
    from datetime import datetime, timezone, timedelta
    
    match_id = uuid.uuid4()
    now = datetime.now(timezone.utc)
    
    match_record = MatchRecord(
        id=match_id,
        opportunity_id=opportunity_id,
        status=MatchStatus.CANDIDATE.value,
        created_at=now,
        updated_at=now,
        expires_at=now + timedelta(hours=48),
        version=0,
    )
    session.add(match_record)
    
    participant_a = MatchParticipantRecord(
        match_id=match_id,
        user_id=user_a_id,
        decision=ParticipantDecision.PENDING.value,
        decided_at=None,
        mutuality_reveal_state=MutualityRevealState.PRIVATE.value,
        created_at=now,
        updated_at=now,
    )
    session.add(participant_a)
    
    participant_b = MatchParticipantRecord(
        match_id=match_id,
        user_id=user_b_id,
        decision=ParticipantDecision.PENDING.value,
        decided_at=None,
        mutuality_reveal_state=MutualityRevealState.PRIVATE.value,
        created_at=now,
        updated_at=now,
    )
    session.add(participant_b)
    
    await session.commit()
    await session.refresh(match_record)
    
    return match_id


def test_get_match_returns_401_without_auth():
    """Test that GET /api/v1/matches/:matchId returns 401 without authentication."""
    match_id = uuid4()
    with TestClient(app) as client:
        response = client.get(f"/api/v1/matches/{match_id}")
        assert response.status_code == 401


def test_get_match_returns_404_for_non_existent_match():
    """Test that GET /api/v1/matches/:matchId returns 404 for non-existent match."""
    user_id = uuid4()
    match_id = uuid4()
    with TestClient(app) as client:
        response = client.get(
            f"/api/v1/matches/{match_id}",
            headers={"X-User-ID": str(user_id)},
        )
        assert response.status_code == 404


def test_get_match_returns_403_for_non_participant():
    """Test that GET /api/v1/matches/:matchId returns 403 for non-participant."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    user_c_id = _create_user(None, "user_c@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User C tries to access match they're not part of
                response = client.get(
                    f"/api/v1/matches/{match_id}",
                    headers={"X-User-ID": str(user_c_id)},
                )
                assert response.status_code == 403
    
    asyncio.run(setup_and_test())


def test_get_match_returns_200_for_participant():
    """Test that GET /api/v1/matches/:matchId returns 200 for participant."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User A accesses their match
                response = client.get(
                    f"/api/v1/matches/{match_id}",
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                assert data["id"] == str(match_id)
                assert data["opportunity_id"] == str(opportunity_id)
                assert len(data["participants"]) == 2
    
    asyncio.run(setup_and_test())


def test_get_match_does_not_expose_private_decisions_before_mutuality():
    """Test that GET /api/v1/matches/:matchId does not expose private decisions before mutuality."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User A accesses their match
                response = client.get(
                    f"/api/v1/matches/{match_id}",
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # All participants should have PRIVATE reveal state
                for participant in data["participants"]:
                    assert participant["mutuality_reveal_state"] == "PRIVATE"
    
    asyncio.run(setup_and_test())


def test_post_decision_returns_401_without_auth():
    """Test that POST /api/v1/matches/:matchId/decision returns 401 without authentication."""
    match_id = uuid4()
    with TestClient(app) as client:
        response = client.post(
            f"/api/v1/matches/{match_id}/decision",
            json={"decision": "INTERESTED"},
        )
        assert response.status_code == 401


def test_post_decision_returns_404_for_non_existent_match():
    """Test that POST /api/v1/matches/:matchId/decision returns 404 for non-existent match."""
    user_id = uuid4()
    match_id = uuid4()
    with TestClient(app) as client:
        response = client.post(
            f"/api/v1/matches/{match_id}/decision",
            json={"decision": "INTERESTED"},
            headers={"X-User-ID": str(user_id)},
        )
        assert response.status_code == 404


def test_post_decision_returns_403_for_non_participant():
    """Test that POST /api/v1/matches/:matchId/decision returns 403 for non-participant."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    user_c_id = _create_user(None, "user_c@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User C tries to record decision for match they're not part of
                response = client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "INTERESTED"},
                    headers={"X-User-ID": str(user_c_id)},
                )
                assert response.status_code == 403
    
    asyncio.run(setup_and_test())


def test_post_decision_interested_updates_decision():
    """Test that POST /api/v1/matches/:matchId/decision with INTERESTED updates decision."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User A records INTERESTED
                response = client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "INTERESTED"},
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # Check that User A's decision is INTERESTED
                user_a_participant = next(p for p in data["participants"] if p["user_id"] == str(user_a_id))
                assert user_a_participant["decision"] == "INTERESTED"
                assert user_a_participant["decided_at"] is not None
    
    asyncio.run(setup_and_test())


def test_post_decision_maybe_updates_decision():
    """Test that POST /api/v1/matches/:matchId/decision with MAYBE updates decision."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User A records MAYBE
                response = client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "MAYBE"},
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # Check that User A's decision is MAYBE
                user_a_participant = next(p for p in data["participants"] if p["user_id"] == str(user_a_id))
                assert user_a_participant["decision"] == "MAYBE"
    
    asyncio.run(setup_and_test())


def test_post_decision_not_interested_terminates_match():
    """Test that POST /api/v1/matches/:matchId/decision with NOT_INTERESTED terminates match."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User A records NOT_INTERESTED
                response = client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "NOT_INTERESTED"},
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # Check that match is TERMINATED
                assert data["status"] == "TERMINATED"
    
    asyncio.run(setup_and_test())


def test_post_decision_updates_match_status_correctly():
    """Test that POST /api/v1/matches/:matchId/decision updates match status correctly."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User A records INTERESTED
                response = client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "INTERESTED"},
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # Status should be USER_INTEREST
                assert data["status"] == "USER_INTEREST"
                
                # User B records INTERESTED
                response = client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "INTERESTED"},
                    headers={"X-User-ID": str(user_b_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # Status should be MUTUAL_INTEREST
                assert data["status"] == "MUTUAL_INTEREST"
    
    asyncio.run(setup_and_test())


def test_get_mutuality_returns_401_without_auth():
    """Test that GET /api/v1/matches/:matchId/mutuality returns 401 without authentication."""
    match_id = uuid4()
    with TestClient(app) as client:
        response = client.get(f"/api/v1/matches/{match_id}/mutuality")
        assert response.status_code == 401


def test_get_mutuality_returns_404_for_non_existent_match():
    """Test that GET /api/v1/matches/:matchId/mutuality returns 404 for non-existent match."""
    user_id = uuid4()
    match_id = uuid4()
    with TestClient(app) as client:
        response = client.get(
            f"/api/v1/matches/{match_id}/mutuality",
            headers={"X-User-ID": str(user_id)},
        )
        assert response.status_code == 404


def test_get_mutuality_returns_403_for_non_participant():
    """Test that GET /api/v1/matches/:matchId/mutuality returns 403 for non-participant."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    user_c_id = _create_user(None, "user_c@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User C tries to access mutuality for match they're not part of
                response = client.get(
                    f"/api/v1/matches/{match_id}/mutuality",
                    headers={"X-User-ID": str(user_c_id)},
                )
                assert response.status_code == 403
    
    asyncio.run(setup_and_test())


def test_get_mutuality_returns_private_state_before_mutuality():
    """Test that GET /api/v1/matches/:matchId/mutuality returns PRIVATE state before mutuality."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # User A accesses mutuality state
                response = client.get(
                    f"/api/v1/matches/{match_id}/mutuality",
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # Should be PRIVATE
                assert data["mutuality_reveal_state"] == "PRIVATE"
                assert data["is_mutual"] is False
    
    asyncio.run(setup_and_test())


def test_get_mutuality_returns_revealed_state_after_mutuality():
    """Test that GET /api/v1/matches/:matchId/mutuality returns REVEALED state after mutuality."""
    user_a_id = _create_user(None, "user_a@example.com")
    user_b_id = _create_user(None, "user_b@example.com")
    
    async def setup_and_test():
        async with SessionLocal() as session:
            with TestClient(app) as client:
                intent_a_id = _create_intent(client, user_a_id, "I want to do something fun")
                _submit_intent(client, user_a_id, intent_a_id)
                
                activity_id = uuid4()
                opportunity_id = await _create_opportunity_directly_async(session, user_a_id, intent_a_id, activity_id)
                match_id = await _create_match_directly_async(session, opportunity_id, user_a_id, user_b_id)
                
                # Both users record INTERESTED
                client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "INTERESTED"},
                    headers={"X-User-ID": str(user_a_id)},
                )
                client.post(
                    f"/api/v1/matches/{match_id}/decision",
                    json={"decision": "INTERESTED"},
                    headers={"X-User-ID": str(user_b_id)},
                )
                
                # User A accesses mutuality state
                response = client.get(
                    f"/api/v1/matches/{match_id}/mutuality",
                    headers={"X-User-ID": str(user_a_id)},
                )
                assert response.status_code == 200
                data = response.json()
                
                # Should be REVEALED_TO_PARTICIPANTS
                assert data["mutuality_reveal_state"] == "REVEALED_TO_PARTICIPANTS"
                assert data["is_mutual"] is True
                assert data["interested_count"] == 2
    
    asyncio.run(setup_and_test())
