import pytest
from datetime import datetime, timezone, timedelta
from uuid import uuid4

from pyrintu_matching.models import (
    Match,
    MatchStatus,
    ParticipantDecision,
    MutualityRevealState,
)
from pyrintu_matching.service import MatchingService, PairwiseInvariantError


def test_create_match_creates_two_participants():
    """Test that creating a match creates exactly two participants."""
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
    
    assert match.participant_count == 2
    assert match.status == MatchStatus.CANDIDATE


def test_create_match_validates_pairwise_invariant():
    """Test that creating a match validates pairwise invariant."""
    service = MatchingService()
    match_id = uuid4()
    opportunity_id = uuid4()
    user_id = uuid4()
    
    with pytest.raises(PairwiseInvariantError):
        service.create_match(
            match_id=match_id,
            opportunity_id=opportunity_id,
            user_a_id=user_id,
            user_b_id=user_id,
        )


def test_create_match_sets_candidate_status():
    """Test that creating a match sets CANDIDATE status."""
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
    
    assert match.status == MatchStatus.CANDIDATE


def test_create_match_sets_expires_at():
    """Test that creating a match sets expires_at based on decision window."""
    service = MatchingService(decision_window_hours=48)
    match_id = uuid4()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    
    now = datetime.now(timezone.utc)
    match = service.create_match(
        match_id=match_id,
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_b_id=user_b_id,
        now=now,
    )
    
    expected_expires_at = now + timedelta(hours=48)
    assert match.expires_at == expected_expires_at


def test_record_decision_updates_participant_decision():
    """Test that recording a decision updates participant decision."""
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
    
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    participant = next(p for p in match.participants if p.user_id == user_a_id)
    assert participant.decision == ParticipantDecision.INTERESTED
    assert participant.decided_at is not None


def test_record_decision_updates_match_status_to_user_interest():
    """Test that recording first INTERESTED updates match status to USER_INTEREST."""
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
    
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    assert match.status == MatchStatus.USER_INTEREST


def test_record_decision_updates_match_status_to_mutual_interest():
    """Test that recording second INTERESTED updates match status to MUTUAL_INTEREST."""
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
    
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    assert match.status == MatchStatus.MUTUAL_INTEREST


def test_record_decision_updates_mutuality_reveal_state():
    """Test that recording decisions updates mutuality reveal state."""
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
    
    # Initially private
    assert all(p.mutuality_reveal_state == MutualityRevealState.PRIVATE for p in match.participants)
    
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    # Now revealed
    assert all(p.mutuality_reveal_state == MutualityRevealState.REVEALED_TO_PARTICIPANTS for p in match.participants)


def test_record_decision_not_interested_terminates_match():
    """Test that recording NOT_INTERESTED terminates the match."""
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
    
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.NOT_INTERESTED)
    
    assert match.status == MatchStatus.TERMINATED


def test_evaluate_mutuality_returns_false_with_one_interested():
    """Test that evaluate_mutuality returns false with one interested."""
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
    
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    assert service.evaluate_mutuality(match) is False


def test_evaluate_mutuality_returns_true_with_both_interested():
    """Test that evaluate_mutuality returns true with both interested."""
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
    
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    assert service.evaluate_mutuality(match) is True


def test_check_match_validity_returns_true_when_valid():
    """Test that check_match_validity returns true when match is valid."""
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
    
    is_valid = service.check_match_validity(
        match,
        opportunity_expires_at=None,
    )
    
    assert is_valid is True


def test_check_match_validity_returns_false_when_expired():
    """Test that check_match_validity returns false when match has expired."""
    service = MatchingService()
    match_id = uuid4()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    
    # Create match in the past
    past = datetime.now(timezone.utc) - timedelta(hours=49)
    match = service.create_match(
        match_id=match_id,
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_b_id=user_b_id,
        now=past,
    )
    
    is_valid = service.check_match_validity(
        match,
        opportunity_expires_at=None,
    )
    
    assert is_valid is False


def test_handle_material_change_resets_to_shown():
    """Test that handle_material_change resets match to SHOWN."""
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
    
    # Advance to MUTUAL_INTEREST
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    assert match.status == MatchStatus.MUTUAL_INTEREST
    
    # Handle material change
    match = service.handle_material_change(match)
    
    assert match.status == MatchStatus.SHOWN


def test_handle_material_change_resets_decisions_to_pending():
    """Test that handle_material_change resets decisions to PENDING."""
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
    
    # Both record INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    # Handle material change
    match = service.handle_material_change(match)
    
    assert all(p.decision == ParticipantDecision.PENDING for p in match.participants)
    assert all(p.decided_at is None for p in match.participants)


def test_handle_material_change_resets_reveal_state_to_private():
    """Test that handle_material_change resets reveal state to PRIVATE."""
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
    
    # Both record INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    # Handle material change
    match = service.handle_material_change(match)
    
    assert all(p.mutuality_reveal_state == MutualityRevealState.PRIVATE for p in match.participants)


def test_handle_material_change_requires_reconfirmation():
    """Test that handle_material_change requires reconfirmation."""
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
    
    # Both record INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    assert match.status == MatchStatus.MUTUAL_INTEREST
    assert service.evaluate_mutuality(match) is True
    
    # Handle material change
    match = service.handle_material_change(match)
    
    # Mutuality lost, requires reconfirmation
    assert match.status == MatchStatus.SHOWN
    assert service.evaluate_mutuality(match) is False
