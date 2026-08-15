from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class MatchParticipantSummary(BaseModel):
    """Summary of a match participant for API responses."""
    user_id: UUID
    decision: str
    decided_at: Optional[datetime] = None
    mutuality_reveal_state: str


class MatchResponse(BaseModel):
    """Response for GET /api/v1/matches/:matchId."""
    id: UUID
    opportunity_id: UUID
    status: str
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    version: int
    participants: list[MatchParticipantSummary]


class MatchDecisionRequest(BaseModel):
    """Request for POST /api/v1/matches/:matchId/decision."""
    decision: str = Field(..., description="Decision: INTERESTED, MAYBE, or NOT_INTERESTED")
    expected_version: Optional[int] = Field(None, description="Expected match version for optimistic concurrency")


class MutualityResponse(BaseModel):
    """Response for GET /api/v1/matches/:matchId/mutuality."""
    match_id: UUID
    status: str
    is_mutual: bool
    participant_count: int
    interested_count: int
    mutuality_reveal_state: str
    # Individual decisions are not exposed before mutuality
