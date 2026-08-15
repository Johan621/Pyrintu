from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class IntentCreateRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)


class IntentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    owner_user_id: UUID
    status: str
    goal_type: str
    raw_input: str | None
    normalized_goal: dict
    constraints: dict
    availability: dict
    version: int
    created_at: datetime
    updated_at: datetime


class IntentSubmitRequest(BaseModel):
    expected_version: int = Field(ge=1)


class ProfileUpsertRequest(BaseModel):
    display_name: str = Field(min_length=1, max_length=120)
    bio: str | None = Field(default=None, max_length=1000)
    avatar_url: str | None = Field(default=None, max_length=2048)
    profile_visibility: str = Field(default="CONNECTIONS", pattern="^(PRIVATE|CONNECTIONS|DISCOVERABLE)$")


class ProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: UUID
    display_name: str
    bio: str | None
    avatar_url: str | None
    profile_visibility: str
    created_at: datetime
    updated_at: datetime
