from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest

from pyrintu_discovery import ActivitySnapshot, evaluate_eligibility, IntentSnapshot
from pyrintu_discovery.eligibility import fit_label_for_count
from pyrintu_discovery.models import FitLabel, OpportunityState
from pyrintu_discovery.service import DiscoveryService


def _intent(
    group_size: int | None = None,
    budget_max: int | None = None,
    experience: str | None = None,
    location: str | None = None,
    time_window: str | None = None,
) -> IntentSnapshot:
    constraints: dict = {}
    if group_size is not None:
        constraints["group_size"] = group_size
    if budget_max is not None:
        constraints["budget_max"] = budget_max
    if experience is not None:
        constraints["experience"] = experience
    if location is not None:
        constraints["location"] = location
    availability = {"time_window": time_window} if time_window else {}
    return IntentSnapshot(
        intent_id=uuid4(),
        owner_user_id=uuid4(),
        status="SUBMITTED",
        normalized_goal={"goal": "test"},
        constraints=constraints,
        availability=availability,
        version=2,
    )


def _activity(
    group_size: int | None = 4,
    cost: int | None = 350,
    environment: str | None = "chill",
    category: str = "sports",
    location_label: str | None = "nearby",
    time_tags: tuple[str, ...] = ("weekend", "this weekend"),
    status: str = "ACTIVE",
    expires_at: datetime | None = None,
    created_at: datetime | None = None,
) -> ActivitySnapshot:
    return ActivitySnapshot(
        activity_id=uuid4(),
        name="Test activity",
        category=category,
        description="Test",
        status=status,
        group_size=group_size,
        estimated_cost_minor=cost,
        currency="INR",
        environment=environment,
        time_tags=time_tags,
        location_label=location_label,
        when_label="Sunday · 6:30 PM",
        what_label="Badminton + Café",
        expires_at=expires_at,
        created_at=created_at or datetime.now(timezone.utc),
    )


def test_budget_hard_exclude() -> None:
    intent = _intent(budget_max=500)
    activity = _activity(cost=900)
    result = evaluate_eligibility(intent, activity)
    assert not result.eligible
    assert "BUDGET_EXCEEDED" in result.hard_fail_reasons


def test_group_size_hard_exclude() -> None:
    intent = _intent(group_size=3)
    activity = _activity(group_size=12)
    result = evaluate_eligibility(intent, activity)
    assert not result.eligible
    assert "GROUP_SIZE_EXCEEDED" in result.hard_fail_reasons


def test_expiry_hard_exclude() -> None:
    intent = _intent()
    past = datetime.now(timezone.utc) - timedelta(days=1)
    activity = _activity(expires_at=past)
    result = evaluate_eligibility(intent, activity)
    assert not result.eligible
    assert "EXPIRED" in result.hard_fail_reasons


def test_activity_not_active_hard_exclude() -> None:
    intent = _intent()
    activity = _activity(status="INACTIVE")
    result = evaluate_eligibility(intent, activity)
    assert not result.eligible
    assert "ACTIVITY_NOT_ACTIVE" in result.hard_fail_reasons


def test_nullable_cost_does_not_trigger_budget_hard_exclude() -> None:
    intent = _intent(budget_max=500)
    activity = _activity(cost=None)
    result = evaluate_eligibility(intent, activity)
    assert result.eligible
    assert "BUDGET_EXCEEDED" not in result.hard_fail_reasons


def test_nullable_group_size_does_not_trigger_group_hard_exclude() -> None:
    intent = _intent(group_size=3)
    activity = _activity(group_size=None)
    result = evaluate_eligibility(intent, activity)
    assert result.eligible
    assert "GROUP_SIZE_EXCEEDED" not in result.hard_fail_reasons


def test_soft_signals_and_fit_label() -> None:
    intent = _intent(
        group_size=4,
        budget_max=500,
        experience="chill",
        location="nearby",
        time_window="this weekend",
    )
    activity = _activity()
    result = evaluate_eligibility(intent, activity)
    assert result.eligible
    assert result.soft_match_count >= 4
    assert result.fit_label == FitLabel.STRONG_FIT


def test_fit_label_thresholds() -> None:
    assert fit_label_for_count(4) == FitLabel.STRONG_FIT
    assert fit_label_for_count(3) == FitLabel.GOOD_FIT
    assert fit_label_for_count(1) == FitLabel.VERY_RELEVANT
    assert fit_label_for_count(0) == FitLabel.GOOD_FIT


def test_eligible_activity_state_ready() -> None:
    intent = _intent(budget_max=500, group_size=4)
    activity = _activity()
    result = evaluate_eligibility(intent, activity)
    assert result.eligible
    assert result.opportunity_state == OpportunityState.READY


def test_discovery_ranking_order() -> None:
    now = datetime.now(timezone.utc)
    intent = _intent(group_size=4, budget_max=500, experience="chill")
    high_fit = _activity(
        cost=400,
        created_at=now + timedelta(hours=2),
        expires_at=now + timedelta(days=5),
    )
    low_fit = _activity(
        cost=150,
        environment="networking",
        category="networking",
        location_label="Hyderabad",
        created_at=now + timedelta(hours=1),
        expires_at=now + timedelta(days=3),
    )
    service = DiscoveryService()
    projections = service.discover(intent, (low_fit, high_fit), now=now)
    assert projections[0].candidate_id == high_fit.activity_id

    same_fit_cheaper = _activity(cost=100, created_at=now + timedelta(hours=1))
    same_fit_pricier = _activity(cost=300, created_at=now + timedelta(hours=1))
    projections = service.discover(intent, (same_fit_pricier, same_fit_cheaper), now=now)
    assert projections[0].candidate_id == same_fit_cheaper.activity_id
