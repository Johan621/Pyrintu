from typing import Any

from pyrintu_matching.models import (
    Match,
    MatchParticipant,
    MatchStatus,
    ParticipantDecision,
    MutualityRevealState,
)


def match_from_record(record: dict[str, Any]) -> Match:
    """
    Convert a database record to a Match domain model.
    
    Expected record structure:
    {
        "id": UUID,
        "opportunity_id": UUID,
        "status": str,
        "created_at": datetime,
        "updated_at": datetime,
        "expires_at": datetime,
        "version": int,
        "participants": list of participant records
    }
    """
    return Match(
        id=record["id"],
        opportunity_id=record["opportunity_id"],
        status=MatchStatus(record["status"]),
        created_at=record["created_at"],
        updated_at=record["updated_at"],
        expires_at=record["expires_at"],
        version=record["version"],
        participants=tuple(
            match_participant_from_record(p) for p in record.get("participants", [])
        ),
    )


def match_to_record(match: Match) -> dict[str, Any]:
    """
    Convert a Match domain model to a database record structure.
    """
    return {
        "id": match.id,
        "opportunity_id": match.opportunity_id,
        "status": match.status.value,
        "created_at": match.created_at,
        "updated_at": match.updated_at,
        "expires_at": match.expires_at,
        "version": match.version,
    }


def match_participant_from_record(record: dict[str, Any]) -> MatchParticipant:
    """
    Convert a database record to a MatchParticipant domain model.
    
    Expected record structure:
    {
        "match_id": UUID,
        "user_id": UUID,
        "decision": str,
        "decided_at": datetime | None,
        "mutuality_reveal_state": str,
        "created_at": datetime,
        "updated_at": datetime
    }
    """
    return MatchParticipant(
        match_id=record["match_id"],
        user_id=record["user_id"],
        decision=ParticipantDecision(record["decision"]),
        decided_at=record.get("decided_at"),
        mutuality_reveal_state=MutualityRevealState(record["mutuality_reveal_state"]),
        created_at=record["created_at"],
        updated_at=record["updated_at"],
    )


def match_participant_to_record(participant: MatchParticipant) -> dict[str, Any]:
    """
    Convert a MatchParticipant domain model to a database record structure.
    """
    return {
        "match_id": participant.match_id,
        "user_id": participant.user_id,
        "decision": participant.decision.value,
        "decided_at": participant.decided_at,
        "mutuality_reveal_state": participant.mutuality_reveal_state.value,
        "created_at": participant.created_at,
        "updated_at": participant.updated_at,
    }
