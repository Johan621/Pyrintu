from __future__ import annotations

from dataclasses import replace
from threading import RLock
from uuid import UUID

from .models import Intent, IntentState, ParsedIntent


class IntentValidationError(ValueError):
    pass


class InMemoryIntentRepository:
    """Temporary persistence boundary for the first vertical slice."""

    def __init__(self) -> None:
        self._items: dict[UUID, Intent] = {}
        self._lock = RLock()

    def save(self, intent: Intent) -> Intent:
        with self._lock:
            self._items[intent.id] = intent
            return intent

    def get(self, owner_id: UUID, intent_id: UUID) -> Intent | None:
        with self._lock:
            intent = self._items.get(intent_id)
            if intent is None or intent.owner_id != owner_id:
                return None
            return intent


class IntentInterpreter:
    """Deterministic MVP interpreter used until the AI structured-output adapter is wired in."""

    def parse(self, raw_text: str) -> ParsedIntent:
        text = " ".join(raw_text.strip().split())
        lowered = text.lower()
        if not text:
            raise IntentValidationError("Intent text is required.")

        group_size = None
        for token in lowered.replace("-", " ").split():
            if token.isdigit():
                value = int(token)
                if 1 <= value <= 20:
                    group_size = value
                    break

        budget_max = None
        digits = "".join(ch if ch.isdigit() else " " for ch in text).split()
        if "under" in lowered and digits:
            candidate = int(digits[0])
            if candidate > 0:
                budget_max = candidate

        return ParsedIntent(
            goal=text,
            experience=("chill" if "chill" in lowered else None),
            group_size=group_size,
            budget_max=budget_max,
            time_window=("this weekend" if "weekend" in lowered else None),
            location=("nearby" if "nearby" in lowered else None),
        )


class IntentService:
    def __init__(self, repository: InMemoryIntentRepository, interpreter: IntentInterpreter | None = None) -> None:
        self._repository = repository
        self._interpreter = interpreter or IntentInterpreter()

    def create(self, owner_id: UUID, raw_text: str) -> Intent:
        parsed = self._interpreter.parse(raw_text)
        intent = Intent.create(owner_id=owner_id, raw_text=raw_text.strip(), parsed=parsed)
        return self._repository.save(intent)

    def submit(self, owner_id: UUID, intent_id: UUID, expected_version: int | None = None) -> Intent:
        intent = self._repository.get(owner_id, intent_id)
        if intent is None:
            raise IntentValidationError("Intent not found.")
        if expected_version is not None and intent.version != expected_version:
            raise IntentValidationError("INTENT_VERSION_STALE")
        if intent.state is not IntentState.DRAFT:
            raise IntentValidationError("Only draft intents can be submitted.")
        return self._repository.save(replace(intent, state=IntentState.SUBMITTED, version=intent.version + 1))
