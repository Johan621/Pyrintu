from uuid import uuid4

import pytest

from pyrintu_intent import IntentService, IntentState, InMemoryIntentRepository, IntentValidationError


def make_service() -> IntentService:
    return IntentService(InMemoryIntentRepository())


def test_create_structures_and_persists_user_intent() -> None:
    service = make_service()
    owner_id = uuid4()

    intent = service.create(
        owner_id,
        "I want something chill with 3 people this weekend nearby under 500",
    )

    assert intent.owner_id == owner_id
    assert intent.state == IntentState.DRAFT
    assert intent.version == 1
    assert intent.parsed.experience == "chill"
    assert intent.parsed.group_size == 3
    assert intent.parsed.time_window == "this weekend"
    assert intent.parsed.location == "nearby"
    assert intent.parsed.budget_max == 500


def test_empty_intent_is_rejected() -> None:
    service = make_service()

    with pytest.raises(IntentValidationError, match="Intent text is required"):
        service.create(uuid4(), "   ")


def test_only_owner_can_read_intent() -> None:
    repository = InMemoryIntentRepository()
    service = IntentService(repository)
    owner_id = uuid4()
    other_user = uuid4()
    intent = service.create(owner_id, "Find something fun")

    assert repository.get(owner_id, intent.id) is not None
    assert repository.get(other_user, intent.id) is None


def test_submit_moves_draft_to_submitted_and_increments_version() -> None:
    service = make_service()
    owner_id = uuid4()
    intent = service.create(owner_id, "Go hiking this weekend")

    submitted = service.submit(owner_id, intent.id, expected_version=1)

    assert submitted.state == IntentState.SUBMITTED
    assert submitted.version == 2


def test_stale_submit_is_rejected() -> None:
    service = make_service()
    owner_id = uuid4()
    intent = service.create(owner_id, "Go hiking")

    with pytest.raises(IntentValidationError, match="INTENT_VERSION_STALE"):
        service.submit(owner_id, intent.id, expected_version=2)
