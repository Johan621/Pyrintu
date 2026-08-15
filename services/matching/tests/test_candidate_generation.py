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
from pyrintu_matching.compatibility import CompatibilityResult


def test_candidate_generation_triggered_by_user_a_interested():
    """Test that candidate generation is triggered by User A INTERESTED."""
    service = MatchingService()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    
    user_a_intent = {
        "activity_id": uuid4(),
        "constraints": {},
        "availability": {},
    }
    
    user_b_intent = {
        "activity_id": user_a_intent["activity_id"],
        "constraints": {},
        "availability": {},
    }
    
    candidates = service.generate_candidates(
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_a_intent=user_a_intent,
        candidate_users=[(user_b_id, user_b_intent)],
        existing_matches=[],
    )
    
    assert len(candidates) == 1
    assert candidates[0][0] == user_a_id
    assert candidates[0][1] == user_b_id
    assert candidates[0][2].compatible is True


def test_candidate_generation_finds_compatible_users():
    """Test that candidate generation finds compatible users."""
    service = MatchingService()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    user_c_id = uuid4()
    
    activity_id = uuid4()
    
    user_a_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    user_b_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    user_c_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    candidates = service.generate_candidates(
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_a_intent=user_a_intent,
        candidate_users=[(user_b_id, user_b_intent), (user_c_id, user_c_intent)],
        existing_matches=[],
    )
    
    assert len(candidates) == 2


def test_candidate_generation_filters_incompatible_users():
    """Test that candidate generation filters incompatible users."""
    service = MatchingService()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    user_c_id = uuid4()
    
    activity_a_id = uuid4()
    activity_b_id = uuid4()
    
    user_a_intent = {
        "activity_id": activity_a_id,
        "constraints": {},
        "availability": {},
    }
    
    user_b_intent = {
        "activity_id": activity_a_id,  # Compatible
        "constraints": {},
        "availability": {},
    }
    
    user_c_intent = {
        "activity_id": activity_b_id,  # Incompatible (different activity)
        "constraints": {},
        "availability": {},
    }
    
    candidates = service.generate_candidates(
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_a_intent=user_a_intent,
        candidate_users=[(user_b_id, user_b_intent), (user_c_id, user_c_intent)],
        existing_matches=[],
    )
    
    assert len(candidates) == 1
    assert candidates[0][1] == user_b_id


def test_candidate_generation_skips_same_user():
    """Test that candidate generation skips the same user."""
    service = MatchingService()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    
    user_a_intent = {
        "activity_id": uuid4(),
        "constraints": {},
        "availability": {},
    }
    
    candidates = service.generate_candidates(
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_a_intent=user_a_intent,
        candidate_users=[(user_a_id, user_a_intent)],  # Same user
        existing_matches=[],
    )
    
    assert len(candidates) == 0


def test_candidate_generation_is_idempotent():
    """Test that candidate generation is idempotent - doesn't create duplicate matches."""
    service = MatchingService()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    
    activity_id = uuid4()
    
    user_a_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    user_b_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    # Create an existing match for this pair
    existing_match = service.create_match(
        match_id=uuid4(),
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_b_id=user_b_id,
    )
    
    # Generate candidates - should skip existing match
    candidates = service.generate_candidates(
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_a_intent=user_a_intent,
        candidate_users=[(user_b_id, user_b_intent)],
        existing_matches=[existing_match],
    )
    
    assert len(candidates) == 0


def test_candidate_generation_skips_terminated_matches():
    """Test that candidate generation skips terminated matches but allows new ones."""
    service = MatchingService()
    opportunity_id = uuid4()
    user_a_id = uuid4()
    user_b_id = uuid4()
    user_c_id = uuid4()
    
    activity_id = uuid4()
    
    user_a_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    user_b_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    user_c_intent = {
        "activity_id": activity_id,
        "constraints": {},
        "availability": {},
    }
    
    # Create a terminated match for user_a and user_b
    terminated_match = service.create_match(
        match_id=uuid4(),
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_b_id=user_b_id,
    )
    terminated_match = service.record_decision(terminated_match, user_a_id, ParticipantDecision.NOT_INTERESTED)
    
    # Verify match is terminated
    assert terminated_match.status == MatchStatus.TERMINATED
    
    # Generate candidates - should skip terminated match but allow new one with user_c
    candidates = service.generate_candidates(
        opportunity_id=opportunity_id,
        user_a_id=user_a_id,
        user_a_intent=user_a_intent,
        candidate_users=[(user_b_id, user_b_intent), (user_c_id, user_c_intent)],
        existing_matches=[terminated_match],
    )
    
    # Should match with both user_b and user_c (terminated match is skipped, allowing new match with user_b)
    # This is the correct behavior: terminated matches don't prevent new matches
    assert len(candidates) == 2
