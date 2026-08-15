from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class WhyThisFitsItem(BaseModel):
    signal_key: str
    label: str


class OpportunitySummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    intent_id: UUID
    state: str
    fit_label: str
    when_label: str | None
    what_label: str | None
    group_size: int | None
    location_label: str | None
    estimated_cost_minor: int | None
    currency: str | None
    why_this_fits: list[WhyThisFitsItem]
    expires_at: datetime | None


class OpportunitiesListResponse(BaseModel):
    opportunities: list[OpportunitySummary] = Field(default_factory=list)
