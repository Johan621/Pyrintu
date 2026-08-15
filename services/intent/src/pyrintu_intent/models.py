from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID, uuid4


class IntentState(StrEnum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    CLOSED = "CLOSED"


@dataclass(frozen=True)
class ParsedIntent:
    goal: str
    experience: str | None = None
    group_size: int | None = None
    budget_max: int | None = None
    time_window: str | None = None
    location: str | None = None


@dataclass(frozen=True)
class Intent:
    id: UUID
    owner_id: UUID
    raw_text: str
    parsed: ParsedIntent
    state: IntentState = IntentState.DRAFT
    version: int = 1
    metadata: dict[str, str] = field(default_factory=dict)

    @classmethod
    def create(cls, owner_id: UUID, raw_text: str, parsed: ParsedIntent) -> "Intent":
        return cls(id=uuid4(), owner_id=owner_id, raw_text=raw_text, parsed=parsed)
