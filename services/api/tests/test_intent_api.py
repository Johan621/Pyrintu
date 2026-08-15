from __future__ import annotations

import os
from uuid import UUID, uuid4

os.environ["DATABASE_URL"] = "sqlite+aiosqlite://"

from fastapi.testclient import TestClient

from pyrintu_api.main import app


def test_create_get_and_submit_intent() -> None:
    user_id = uuid4()
    headers = {"X-User-ID": str(user_id)}

    with TestClient(app) as client:
        created = client.post(
            "/api/v1/intents",
            json={"text": "I want something chill with 3 people this weekend nearby under 500"},
            headers=headers,
        )
        assert created.status_code == 201
        body = created.json()
        assert body["status"] == "DRAFT"
        assert body["version"] == 1
        assert body["constraints"]["group_size"] == 3
        assert body["constraints"]["budget_max"] == 500

        intent_id = body["id"]
        fetched = client.get(f"/api/v1/intents/{intent_id}", headers=headers)
        assert fetched.status_code == 200

        submitted = client.post(
            f"/api/v1/intents/{intent_id}/submit",
            json={"expected_version": 1},
            headers=headers,
        )
        assert submitted.status_code == 200
        assert submitted.json()["status"] == "SUBMITTED"
        assert submitted.json()["version"] == 2


def test_intent_is_owner_scoped() -> None:
    owner = uuid4()
    other_user = uuid4()

    with TestClient(app) as client:
        created = client.post(
            "/api/v1/intents",
            json={"text": "Go hiking"},
            headers={"X-User-ID": str(owner)},
        )
        intent_id = created.json()["id"]

        denied = client.get(
            f"/api/v1/intents/{intent_id}",
            headers={"X-User-ID": str(other_user)},
        )
        assert denied.status_code == 404


def test_stale_submit_is_rejected() -> None:
    owner = uuid4()

    with TestClient(app) as client:
        created = client.post(
            "/api/v1/intents",
            json={"text": "Go hiking"},
            headers={"X-User-ID": str(owner)},
        )
        intent_id = created.json()["id"]

        stale = client.post(
            f"/api/v1/intents/{intent_id}/submit",
            json={"expected_version": 2},
            headers={"X-User-ID": str(owner)},
        )
        assert stale.status_code == 409
        assert stale.json()["detail"] == "INTENT_VERSION_STALE"
