from __future__ import annotations

import os
from pathlib import Path
from uuid import uuid4

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./pyrintu-profile-test.db"
os.environ["PYRINTU_AUTH_MODE"] = "development"

from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient

from pyrintu_api.main import app

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "pyrintu-profile-test.db"


def _migrate() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    command.upgrade(Config(str(BASE_DIR / "alembic.ini")), "head")


_migrate()


def test_profile_create_and_read() -> None:
    user_id = uuid4()
    headers = {"X-User-ID": str(user_id)}

    with TestClient(app) as client:
        created = client.put(
            "/api/v1/me/profile",
            json={
                "display_name": "Suraj",
                "bio": "Building with Pyrintu",
                "profile_visibility": "DISCOVERABLE",
            },
            headers=headers,
        )
        assert created.status_code == 200
        body = created.json()
        assert body["user_id"] == str(user_id)
        assert body["display_name"] == "Suraj"
        assert body["profile_visibility"] == "DISCOVERABLE"

        fetched = client.get("/api/v1/me/profile", headers=headers)
        assert fetched.status_code == 200
        assert fetched.json()["display_name"] == "Suraj"


def test_profile_is_owner_scoped() -> None:
    owner = uuid4()
    other_user = uuid4()

    with TestClient(app) as client:
        client.put(
            "/api/v1/me/profile",
            json={"display_name": "Owner", "profile_visibility": "CONNECTIONS"},
            headers={"X-User-ID": str(owner)},
        )
        # The authenticated principal always determines which profile is addressed.
        missing = client.get(
            "/api/v1/me/profile",
            headers={"X-User-ID": str(other_user)},
        )
        assert missing.status_code == 404
