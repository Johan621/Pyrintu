from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass(frozen=True)
class CompatibilityResult:
    """Result of compatibility evaluation between two intents."""
    compatible: bool
    same_activity_context: bool
    compatible_time: bool
    compatible_budget: bool
    compatible_location: bool
    compatible_group_constraints: bool
    failure_reasons: tuple[str, ...] = ()


def evaluate_compatibility(
    intent_a_activity_id: UUID,
    intent_a_constraints: dict,
    intent_a_availability: dict,
    intent_b_activity_id: UUID,
    intent_b_constraints: dict,
    intent_b_availability: dict,
) -> CompatibilityResult:
    """
    Evaluate compatibility between two intents for matching.
    
    Missing constraint = unconstrained (compatible by default).
    Only known conflicting values make a pair incompatible.
    """
    failure_reasons = []
    
    # 1. Same activity context
    same_activity = intent_a_activity_id == intent_b_activity_id
    if not same_activity:
        failure_reasons.append("Different activity context")
    
    # 2. Compatible time (missing constraint = unconstrained)
    compatible_time = _check_time_compatibility(
        intent_a_availability,
        intent_b_availability,
    )
    if not compatible_time:
        failure_reasons.append("Incompatible time constraints")
    
    # 3. Compatible budget (missing constraint = unconstrained)
    compatible_budget = _check_budget_compatibility(
        intent_a_constraints,
        intent_b_constraints,
    )
    if not compatible_budget:
        failure_reasons.append("Incompatible budget constraints")
    
    # 4. Compatible location (missing constraint = unconstrained)
    compatible_location = _check_location_compatibility(
        intent_a_constraints,
        intent_b_constraints,
    )
    if not compatible_location:
        failure_reasons.append("Incompatible location constraints")
    
    # 5. Compatible group constraints (missing constraint = unconstrained)
    compatible_group = _check_group_compatibility(
        intent_a_constraints,
        intent_b_constraints,
    )
    if not compatible_group:
        failure_reasons.append("Incompatible group size constraints")
    
    all_compatible = (
        same_activity and
        compatible_time and
        compatible_budget and
        compatible_location and
        compatible_group
    )
    
    return CompatibilityResult(
        compatible=all_compatible,
        same_activity_context=same_activity,
        compatible_time=compatible_time,
        compatible_budget=compatible_budget,
        compatible_location=compatible_location,
        compatible_group_constraints=compatible_group,
        failure_reasons=tuple(failure_reasons),
    )


def _check_time_compatibility(
    availability_a: dict,
    availability_b: dict,
) -> bool:
    """
    Check if time constraints are compatible.
    
    Missing constraint = unconstrained (compatible by default).
    If both have time constraints, they must overlap.
    """
    time_a = availability_a.get("time")
    time_b = availability_b.get("time")
    
    # If either has no time constraint, they are compatible
    if not time_a or not time_b:
        return True
    
    # Both have time constraints - check for overlap
    # Expected structure: {"start": "2024-01-01T10:00", "end": "2024-01-01T18:00"}
    start_a = time_a.get("start")
    end_a = time_a.get("end")
    start_b = time_b.get("start")
    end_b = time_b.get("end")
    
    # If any field is missing, treat as unconstrained
    if not all([start_a, end_a, start_b, end_b]):
        return True
    
    # Check for overlap: intervals overlap if start_a < end_b and start_b < end_a
    try:
        from datetime import datetime
        start_a_dt = datetime.fromisoformat(start_a)
        end_a_dt = datetime.fromisoformat(end_a)
        start_b_dt = datetime.fromisoformat(start_b)
        end_b_dt = datetime.fromisoformat(end_b)
        
        return start_a_dt < end_b_dt and start_b_dt < end_a_dt
    except (ValueError, TypeError):
        # If parsing fails, treat as unconstrained
        return True


def _check_budget_compatibility(
    constraints_a: dict,
    constraints_b: dict,
) -> bool:
    """
    Check if budget constraints are compatible.
    
    Missing constraint = unconstrained (compatible by default).
    If both have budget constraints, they must overlap (both can afford).
    """
    budget_a = constraints_a.get("budget")
    budget_b = constraints_b.get("budget")
    
    # If either has no budget constraint, they are compatible
    if not budget_a or not budget_b:
        return True
    
    # Both have budget constraints - check if both can afford
    # Expected structure: {"max": 500} or {"min": 100, "max": 500}
    max_a = budget_a.get("max")
    max_b = budget_b.get("max")
    
    # If either has no max, treat as unconstrained
    if max_a is None or max_b is None:
        return True
    
    # Both can afford if their max budgets are sufficient
    # For pairwise matching, we just need both to have some budget
    # The actual activity cost check happens at opportunity level
    return True


def _check_location_compatibility(
    constraints_a: dict,
    constraints_b: dict,
) -> bool:
    """
    Check if location constraints are compatible.
    
    Missing constraint = unconstrained (compatible by default).
    If both have location constraints, they must be compatible.
    """
    location_a = constraints_a.get("location")
    location_b = constraints_b.get("location")
    
    # If either has no location constraint, they are compatible
    if not location_a or not location_b:
        return True
    
    # Both have location constraints - check compatibility
    # Expected structure: {"city": "Hyderabad"} or {"radius_km": 10, "lat": 17.4, "lon": 78.4}
    city_a = location_a.get("city")
    city_b = location_b.get("city")
    
    # If both specify cities, they must match
    if city_a and city_b:
        return city_a.lower() == city_b.lower()
    
    # If either has no city specified, treat as compatible
    return True


def _check_group_compatibility(
    constraints_a: dict,
    constraints_b: dict,
) -> bool:
    """
    Check if group size constraints are compatible.
    
    Missing constraint = unconstrained (compatible by default).
    If both have group size preferences, they must overlap.
    """
    group_a = constraints_a.get("group_size")
    group_b = constraints_b.get("group_size")
    
    # If either has no group size constraint, they are compatible
    if not group_a or not group_b:
        return True
    
    # Both have group constraints - check for overlap
    # Expected structure: {"min": 2, "max": 4}
    min_a = group_a.get("min")
    max_a = group_a.get("max")
    min_b = group_b.get("min")
    max_b = group_b.get("max")
    
    # For pairwise matching (exactly 2 people), we just need both to accept 2
    # If min is specified, it must be <= 2
    # If max is specified, it must be >= 2
    if min_a is not None and min_a > 2:
        return False
    if min_b is not None and min_b > 2:
        return False
    if max_a is not None and max_a < 2:
        return False
    if max_b is not None and max_b < 2:
        return False
    
    return True
