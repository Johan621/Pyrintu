import pytest
from datetime import datetime, timezone
from uuid import uuid4

from pyrintu_matching.models import (
    Match,
    MatchStatus,
    ParticipantDecision,
    MutualityRevealState,
)
from pyrintu_matching.service import MatchingService, PairwiseInvariantError


def test_match_creation_with_exactly_two_participants_succeeds():
    """Test that creating a match with exactly 2 participants succeeds."""
    service = MatchingService()
    match_id = uuid4()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    
    match = service.create_match(
        match_id=match_id,
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_b_id=user_b_id,
    )
    
    assert match.id == match_id
    assert match.opportunity_id == opportunity_id
    assert match.status == MatchStatus.CANDIDATE
    assert match.participant_count == 2
    assert match.version == 0


def test_match_creation_with_duplicate_user_id_fails():
    """Test that creating a match with duplicate user ID fails."""
    service = MatchingService()
    match_id = uuid4()
    opportunity_id = uuid4()
    user_id = uuid4()
    
    with pytest.raises(PairwiseInvariantError, match="Cannot create match with same user twice"):
        service.create_match(
            match_id=match_id,
            opportunity_id=opportunity_id,
            user_a_id=user_id,
            user_b_id=user_id,
        )


def test_pairwise_invariant_maintained_on_material_change():
    """Test that pairwise invariant is maintained on material change."""
    service = MatchingService()
    match_id = uuid4()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    
    match = service.create_match(
        match_id=match_id,
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_b_id=user_b_id,
    )
    
    # Handle material change
    updated_match = service.handle_material_change(match)
    
    # Should still have exactly 2 participants
    assert updated_match.participant_count == 2
    assert updated_match.status == MatchStatus.SHOWN
    assert all(p.decision == ParticipantDecision.PENDING for p in updated_match.participants)
    assert all(p.mutuality_reveal_state == MutualityRevealState.PRIVATE for p in updated_match.participants)
