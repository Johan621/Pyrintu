from __future__ import annotations

from datetime import datetime, timezone

from .models import (
    ActivitySnapshot,
    EligibilityResult,
    FitLabel,
    FitSignal,
    IntentSnapshot,
    OpportunityState,
)


def _normalize(value: str | None) -> str:
    return value.strip().lower() if value else ""


def _text_contains(left: str | None, right: str | None) -> bool:
    left_norm = _normalize(left)
    right_norm = _normalize(right)
    if not left_norm or not right_norm:
        return False
    return left_norm in right_norm or right_norm in left_norm


def compute_soft_signals(intent: IntentSnapshot, activity: ActivitySnapshot) -> tuple[tuple[FitSignal, ...], int]:
    signals: list[FitSignal] = []
    match_count = 0

    experience = intent.constraints.get("experience")
    if isinstance(experience, str) and experience.strip():
        env_match = _text_contains(experience, activity.environment)
        category_match = _text_contains(experience, activity.category)
        matched = env_match or category_match
        if env_match:
            label = f"{experience} matches the activity environment ({activity.environment})."
        elif category_match:
            label = f"{experience} matches the activity category ({activity.category})."
        else:
            label = f"{experience} does not match this activity's environment or category."
        signals.append(FitSignal(signal_key="experience", label=label, matched=matched))
        if matched:
            match_count += 1

    time_window = intent.availability.get("time_window")
    if isinstance(time_window, str) and time_window.strip():
        matched = any(_text_contains(time_window, tag) for tag in activity.time_tags)
        label = (
            f"{time_window} fits this opportunity's timing."
            if matched
            else f"{time_window} does not match this opportunity's timing."
        )
        signals.append(FitSignal(signal_key="time_window", label=label, matched=matched))
        if matched:
            match_count += 1

    location = intent.constraints.get("location")
    if isinstance(location, str) and location.strip():
        matched = _text_contains(location, activity.location_label)
        label = (
            f"{location} matches the opportunity location context ({activity.location_label})."
            if matched
            else f"{location} does not match this opportunity's location context."
        )
        signals.append(FitSignal(signal_key="location", label=label, matched=matched))
        if matched:
            match_count += 1

    intent_group_size = intent.constraints.get("group_size")
    if isinstance(intent_group_size, int) and activity.group_size is not None:
        matched = activity.group_size <= intent_group_size
        label = (
            f"Group size ({activity.group_size}) fits your intent (up to {intent_group_size} people)."
            if matched
            else f"Group size ({activity.group_size}) exceeds your intent limit ({intent_group_size} people)."
        )
        signals.append(FitSignal(signal_key="group_size", label=label, matched=matched))
        if matched:
            match_count += 1

    budget_max = intent.constraints.get("budget_max")
    if isinstance(budget_max, int) and activity.estimated_cost_minor is not None:
        matched = activity.estimated_cost_minor <= budget_max
        label = (
            f"Estimated cost fits within your budget (up to {budget_max})."
            if matched
            else f"Estimated cost exceeds your budget (up to {budget_max})."
        )
        signals.append(FitSignal(signal_key="budget", label=label, matched=matched))
        if matched:
            match_count += 1

    return tuple(signals), match_count


def fit_label_for_count(soft_match_count: int) -> FitLabel:
    if soft_match_count >= 4:
        return FitLabel.STRONG_FIT
    if soft_match_count >= 2:
        return FitLabel.GOOD_FIT
    if soft_match_count == 1:
        return FitLabel.VERY_RELEVANT
    return FitLabel.GOOD_FIT


def evaluate_eligibility(
    intent: IntentSnapshot,
    activity: ActivitySnapshot,
    now: datetime | None = None,
) -> EligibilityResult:
    now = now or datetime.now(timezone.utc)
    hard_fail_reasons: list[str] = []

    if activity.status != "ACTIVE":
        hard_fail_reasons.append("ACTIVITY_NOT_ACTIVE")

    if activity.expires_at is not None:
        expires_at = activity.expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if expires_at <= now:
            hard_fail_reasons.append("EXPIRED")

    budget_max = intent.constraints.get("budget_max")
    if isinstance(budget_max, int) and activity.estimated_cost_minor is not None:
        if activity.estimated_cost_minor > budget_max:
            hard_fail_reasons.append("BUDGET_EXCEEDED")

    intent_group_size = intent.constraints.get("group_size")
    if isinstance(intent_group_size, int) and activity.group_size is not None:
        if activity.group_size > intent_group_size:
            hard_fail_reasons.append("GROUP_SIZE_EXCEEDED")

    fit_signals, soft_match_count = compute_soft_signals(intent, activity)
    fit_label = fit_label_for_count(soft_match_count)

    if hard_fail_reasons:
        state = OpportunityState.EXPIRED if "EXPIRED" in hard_fail_reasons else OpportunityState.UNAVAILABLE
        return EligibilityResult(
            eligible=False,
            hard_fail_reasons=tuple(hard_fail_reasons),
            fit_signals=fit_signals,
            soft_match_count=soft_match_count,
            fit_label=fit_label,
            opportunity_state=state,
        )

    return EligibilityResult(
        eligible=True,
        fit_signals=fit_signals,
        soft_match_count=soft_match_count,
        fit_label=fit_label,
        opportunity_state=OpportunityState.READY,
    )
