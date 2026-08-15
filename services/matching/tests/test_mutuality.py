import pytest
from datetime import datetime, timezone
from uuid import uuid4

from pyrintu_matching.models import (
    Match,
    MatchStatus,
    ParticipantDecision,
    MutualityRevealState,
)
from pyrintu_matching.service import MatchingService


def test_mutuality_not_reached_with_one_interested():
    """Test that mutuality is not reached with only one interested participant."""
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
    
    # User A records INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    assert service.evaluate_mutuality(match) is False


def test_mutuality_reached_with_both_interested():
    """Test that mutuality is reached when both participants are INTERESTED."""
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
    
    # User A records INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    # User B records INTERESTED
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    assert service.evaluate_mutuality(match) is True
    assert match.status == MatchStatus.MUTUAL_INTEREST


def test_maybe_does_not_count_toward_mutuality():
    """Test that MAYBE does not count toward mutuality."""
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
    
    # User A records INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    # User B records MAYBE
    match = service.record_decision(match, user_b_id, ParticipantDecision.MAYBE)
    
    assert service.evaluate_mutuality(match) is False


def test_not_interested_prevents_mutuality():
    """Test that NOT_INTERESTED prevents mutuality."""
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
    
    # User A records INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    # User B records NOT_INTERESTED
    match = service.record_decision(match, user_b_id, ParticipantDecision.NOT_INTERESTED)
    
    assert service.evaluate_mutuality(match) is False
    assert match.status == MatchStatus.TERMINATED


def test_pending_does_not_count_toward_mutuality():
    """Test that PENDING does not count toward mutuality."""
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
    
    # Both participants are PENDING (default)
    assert service.evaluate_mutuality(match) is False


def test_mutuality_reveal_state_transitions_to_revealed():
    """Test that mutuality reveal state transitions to REVEALED_TO_PARTICIPANTS when mutuality achieved."""
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
    
    # User A records INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    # Still private
    assert all(p.mutuality_reveal_state == MutualityRevealState.PRIVATE for p in match.participants)
    
    # User B records INTERESTED
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    # Now revealed to participants
    assert all(p.mutuality_reveal_state == MutualityRevealState.REVEALED_TO_PARTICIPANTS for p in match.participants)


def test_mutuality_reveal_state_remains_private_without_mutuality():
    """Test that mutuality reveal state remains PRIVATE without mutuality."""
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
    
    # User A records INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    
    # User B records MAYBE
    match = service.record_decision(match, user_b_id, ParticipantDecision.MAYBE)
    
    # Still private
    assert all(p.mutuality_reveal_state == MutualityRevealState.PRIVATE for p in match.participants)


def test_material_change_resets_decisions_to_pending():
    """Test that material change resets decisions to PENDING."""
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
    
    # Both participants record INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    assert match.status == MatchStatus.MUTUAL_INTEREST
    
    # Handle material change
    match = service.handle_material_change(match)
    
    # Decisions reset to PENDING
    assert all(p.decision == ParticipantDecision.PENDING for p in match.participants)
    assert all(p.decided_at is None for p in match.participants)


def test_material_change_resets_reveal_state_to_private():
    """Test that material change resets reveal state to PRIVATE."""
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
    
    # Both participants record INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    # Reveal state is REVEALED_TO_PARTICIPANTS
    assert all(p.mutuality_reveal_state == MutualityRevealState.REVEALED_TO_PARTICIPANTS for p in match.participants)
    
    # Handle material change
    match = service.handle_material_change(match)
    
    # Reveal state reset to PRIVATE
    assert all(p.mutuality_reveal_state == MutualityRevealState.PRIVATE for p in match.participants)


def test_material_change_invalidates_prior_mutuality():
    """Test that material change invalidates prior mutuality."""
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
    
    # Both participants record INTERESTED
    match = service.record_decision(match, user_a_id, ParticipantDecision.INTERESTED)
    match = service.record_decision(match, user_b_id, ParticipantDecision.INTERESTED)
    
    assert match.status == MatchStatus.MUTUAL_INTEREST
    assert service.evaluate_mutuality(match) is True
    
    # Handle material change
    match = service.handle_material_change(match)
    
    # Mutuality invalidated
    assert match.status == MatchStatus.SHOWN
    assert service.evaluate_mutuality(match) is False
