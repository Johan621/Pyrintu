from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from uuid import UUID


class CandidateType(StrEnum):
    ACTIVITY = "ACTIVITY"


class VisibilityState(StrEnum):
    ACTIVE = "ACTIVE"
    HIDDEN = "HIDDEN"


class OpportunityState(StrEnum):
    READY = "READY"
    EXPIRED = "EXPIRED"
    UNAVAILABLE = "UNAVAILABLE"


class FitLabel(StrEnum):
    STRONG_FIT = "STRONG_FIT"
    GOOD_FIT = "GOOD_FIT"
    VERY_RELEVANT = "VERY_RELEVANT"


@dataclass(frozen=True)
class IntentSnapshot:
    intent_id: UUID
    owner_user_id: UUID
    status: str
    normalized_goal: dict
    constraints: dict
    availability: dict
    version: int


@dataclass(frozen=True)
class ActivitySnapshot:
    activity_id: UUID
    name: str
    category: str
    description: str | None
    status: str
    group_size: int | None
    estimated_cost_minor: int | None
    currency: str | None
    environment: str | None
    time_tags: tuple[str, ...]
    location_label: str | None
    when_label: str | None
    what_label: str | None
    expires_at: datetime | None
    created_at: datetime


@dataclass(frozen=True)
class PersistedOpportunitySnapshot:
    opportunity_id: UUID
    candidate_id: UUID
    candidate_type: CandidateType
    visibility_state: VisibilityState
    created_at: datetime


@dataclass(frozen=True)
class FitSignal:
    signal_key: str
    label: str
    matched: bool


@dataclass(frozen=True)
class EligibilityResult:
    eligible: bool
    hard_fail_reasons: tuple[str, ...] = ()
    fit_signals: tuple[FitSignal, ...] = ()
    soft_match_count: int = 0
    fit_label: FitLabel = FitLabel.GOOD_FIT
    opportunity_state: OpportunityState = OpportunityState.READY


@dataclass(frozen=True)
class RankedActivity:
    activity: ActivitySnapshot
    eligibility: EligibilityResult


@dataclass(frozen=True)
class OpportunityProjection:
    opportunity_id: UUID | None
    intent_id: UUID
    candidate_type: CandidateType
    candidate_id: UUID
    visibility_state: VisibilityState
    state: OpportunityState
    fit_label: FitLabel
    when_label: str | None
    what_label: str | None
    group_size: int | None
    location_label: str | None
    estimated_cost_minor: int | None
    currency: str | None
    why_this_fits: tuple[FitSignal, ...]
    expires_at: datetime | None
    created_at: datetime | None = None
    evidence_json: dict = field(default_factory=dict)
