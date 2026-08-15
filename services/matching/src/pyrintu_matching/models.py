from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID


class MatchStatus(str, Enum):
    """Match lifecycle states."""
    CANDIDATE = "CANDIDATE"
    SHOWN = "SHOWN"
    USER_INTEREST = "USER_INTEREST"
    MUTUAL_INTEREST = "MUTUAL_INTEREST"
    CONNECTION_ELIGIBLE = "CONNECTION_ELIGIBLE"
    TERMINATED = "TERMINATED"


class ParticipantDecision(str, Enum):
    """Participant decision states."""
    PENDING = "PENDING"
    INTERESTED = "INTERESTED"
    MAYBE = "MAYBE"
    NOT_INTERESTED = "NOT_INTERESTED"
    SKIPPED = "SKIPPED"


class MutualityRevealState(str, Enum):
    """Mutuality reveal privacy states."""
    PRIVATE = "PRIVATE"
    REVEALED_TO_PARTICIPANTS = "REVEALED_TO_PARTICIPANTS"
    FULLY_PUBLIC = "FULLY_PUBLIC"


@dataclass(frozen=True)
class MatchParticipant:
    """Domain model for a match participant."""
    match_id: UUID
    user_id: UUID
    decision: ParticipantDecision
    decided_at: Optional[datetime]
    mutuality_reveal_state: MutualityRevealState
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class Match:
    """Domain model for a match."""
    id: UUID
    opportunity_id: UUID
    status: MatchStatus
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    version: int
    participants: tuple[MatchParticipant, ...]

    @property
    def is_mutual(self) -> bool:
        """Check if match has achieved mutuality."""
        return self.status in (MatchStatus.MUTUAL_INTEREST, MatchStatus.CONNECTION_ELIGIBLE)

    @property
    def is_expired(self) -> bool:
        """Check if match has expired."""
        return datetime.now(self.expires_at.tzinfo) >= self.expires_at

    @property
    def participant_count(self) -> int:
        """Get number of participants."""
        return len(self.participants)
