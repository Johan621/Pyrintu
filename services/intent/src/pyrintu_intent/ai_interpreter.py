from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Protocol

from .models import ParsedIntent


class AITextGenerator(Protocol):
    def generate(self, user_input: str) -> str:
        """Return a JSON object containing the fields required by ParsedIntent."""


@dataclass(frozen=True)
class AIIntentInterpreter:
    generator: AITextGenerator

    def parse(self, raw_text: str) -> ParsedIntent:
        if not raw_text.strip():
            raise ValueError("Intent text is required.")

        response = self.generator.generate(raw_text)
        try:
            payload = json.loads(response)
        except json.JSONDecodeError as exc:
            raise ValueError("AI intent response was not valid JSON.") from exc

        if not isinstance(payload, dict):
            raise ValueError("AI intent response must be a JSON object.")

        goal = payload.get("goal")
        if not isinstance(goal, str) or not goal.strip():
            raise ValueError("AI intent response is missing goal.")

        group_size = payload.get("group_size")
        if group_size is not None and (not isinstance(group_size, int) or not 1 <= group_size <= 20):
            raise ValueError("group_size must be an integer between 1 and 20.")

        budget_max = payload.get("budget_max")
        if budget_max is not None and (not isinstance(budget_max, int) or budget_max <= 0):
            raise ValueError("budget_max must be a positive integer.")

        return ParsedIntent(
            goal=goal.strip(),
            experience=self._optional_string(payload, "experience"),
            group_size=group_size,
            budget_max=budget_max,
            time_window=self._optional_string(payload, "time_window"),
            location=self._optional_string(payload, "location"),
        )

    @staticmethod
    def _optional_string(payload: dict, key: str) -> str | None:
        value = payload.get(key)
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string when provided.")
        return value.strip() or None
