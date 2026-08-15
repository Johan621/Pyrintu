import pytest
from uuid import uuid4

from pyrintu_matching.compatibility import evaluate_compatibility, CompatibilityResult


def test_same_activity_context_returns_true():
    """Test that same activity context returns true."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={},
        intent_b_availability={},
    )
    
    assert result.compatible is True
    assert result.same_activity_context is True


def test_different_activity_context_returns_false():
    """Test that different activity context returns false."""
    activity_a_id = uuid4()
    activity_b_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_a_id,
        intent_a_constraints={},
        intent_a_availability={},
        intent_b_activity_id=activity_b_id,
        intent_b_constraints={},
        intent_b_availability={},
    )
    
    assert result.compatible is False
    assert result.same_activity_context is False


def test_compatible_time_with_both_constraints_returns_true():
    """Test that compatible time with both constraints returns true."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={},
        intent_a_availability={
            "time": {"start": "2024-01-01T10:00", "end": "2024-01-01T18:00"}
        },
        intent_b_activity_id=activity_id,
        intent_b_constraints={},
        intent_b_availability={
            "time": {"start": "2024-01-01T12:00", "end": "2024-01-01T20:00"}
        },
    )
    
    assert result.compatible is True
    assert result.compatible_time is True


def test_compatible_time_with_one_constraint_returns_true():
    """Test that compatible time with one constraint returns true (missing = unconstrained)."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={},
        intent_a_availability={
            "time": {"start": "2024-01-01T10:00", "end": "2024-01-01T18:00"}
        },
        intent_b_activity_id=activity_id,
        intent_b_constraints={},
        intent_b_availability={},  # No time constraint
    )
    
    assert result.compatible is True
    assert result.compatible_time is True


def test_incompatible_time_with_both_constraints_returns_false():
    """Test that incompatible time with both constraints returns false."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={},
        intent_a_availability={
            "time": {"start": "2024-01-01T10:00", "end": "2024-01-01T12:00"}
        },
        intent_b_activity_id=activity_id,
        intent_b_constraints={},
        intent_b_availability={
            "time": {"start": "2024-01-01T14:00", "end": "2024-01-01T16:00"}
        },
    )
    
    assert result.compatible is False
    assert result.compatible_time is False


def test_compatible_budget_with_both_constraints_returns_true():
    """Test that compatible budget with both constraints returns true."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"budget": {"max": 500}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={"budget": {"max": 600}},
        intent_b_availability={},
    )
    
    assert result.compatible is True
    assert result.compatible_budget is True


def test_compatible_budget_with_one_constraint_returns_true():
    """Test that compatible budget with one constraint returns true (missing = unconstrained)."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"budget": {"max": 500}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={},  # No budget constraint
        intent_b_availability={},
    )
    
    assert result.compatible is True
    assert result.compatible_budget is True


def test_compatible_location_with_both_constraints_returns_true():
    """Test that compatible location with both constraints returns true."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"location": {"city": "Hyderabad"}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={"location": {"city": "Hyderabad"}},
        intent_b_availability={},
    )
    
    assert result.compatible is True
    assert result.compatible_location is True


def test_compatible_location_with_one_constraint_returns_true():
    """Test that compatible location with one constraint returns true (missing = unconstrained)."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"location": {"city": "Hyderabad"}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={},  # No location constraint
        intent_b_availability={},
    )
    
    assert result.compatible is True
    assert result.compatible_location is True


def test_incompatible_location_with_both_constraints_returns_false():
    """Test that incompatible location with both constraints returns false."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"location": {"city": "Hyderabad"}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={"location": {"city": "Bangalore"}},
        intent_b_availability={},
    )
    
    assert result.compatible is False
    assert result.compatible_location is False


def test_compatible_group_constraints_with_both_constraints_returns_true():
    """Test that compatible group constraints with both constraints returns true."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"group_size": {"min": 2, "max": 4}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={"group_size": {"min": 2, "max": 5}},
        intent_b_availability={},
    )
    
    assert result.compatible is True
    assert result.compatible_group_constraints is True


def test_compatible_group_constraints_with_one_constraint_returns_true():
    """Test that compatible group constraints with one constraint returns true (missing = unconstrained)."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"group_size": {"min": 2, "max": 4}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={},  # No group size constraint
        intent_b_availability={},
    )
    
    assert result.compatible is True
    assert result.compatible_group_constraints is True


def test_incompatible_group_constraints_with_both_constraints_returns_false():
    """Test that incompatible group constraints with both constraints returns false."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={"group_size": {"min": 3, "max": 5}},
        intent_a_availability={},
        intent_b_activity_id=activity_id,
        intent_b_constraints={"group_size": {"min": 4, "max": 6}},
        intent_b_availability={},
    )
    
    assert result.compatible is False
    assert result.compatible_group_constraints is False


def test_all_compatibility_checks_pass():
    """Test that all compatibility checks pass."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={
            "budget": {"max": 500},
            "location": {"city": "Hyderabad"},
            "group_size": {"min": 2, "max": 4},
        },
        intent_a_availability={
            "time": {"start": "2024-01-01T10:00", "end": "2024-01-01T18:00"}
        },
        intent_b_activity_id=activity_id,
        intent_b_constraints={
            "budget": {"max": 600},
            "location": {"city": "Hyderabad"},
            "group_size": {"min": 2, "max": 5},
        },
        intent_b_availability={
            "time": {"start": "2024-01-01T12:00", "end": "2024-01-01T20:00"}
        },
    )
    
    assert result.compatible is True
    assert result.same_activity_context is True
    assert result.compatible_time is True
    assert result.compatible_budget is True
    assert result.compatible_location is True
    assert result.compatible_group_constraints is True


def test_any_compatibility_check_fails():
    """Test that any compatibility check fails makes the result incompatible."""
    activity_id = uuid4()
    
    result = evaluate_compatibility(
        intent_a_activity_id=activity_id,
        intent_a_constraints={
            "budget": {"max": 500},
            "location": {"city": "Hyderabad"},
            "group_size": {"min": 2, "max": 4},
        },
        intent_a_availability={
            "time": {"start": "2024-01-01T10:00", "end": "2024-01-01T18:00"}
        },
        intent_b_activity_id=activity_id,
        intent_b_constraints={
            "budget": {"max": 600},
            "location": {"city": "Bangalore"},  # Different city
            "group_size": {"min": 2, "max": 5},
        },
        intent_b_availability={
            "time": {"start": "2024-01-01T12:00", "end": "2024-01-01T20:00"}
        },
    )
    
    assert result.compatible is False
    assert result.compatible_location is False
    assert len(result.failure_reasons) > 0
