"""Explicit authorized context contract for Pyrintu AI calls."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class AuthorizedAIContext:
    """Structured context that has already passed authorization filtering.

    Callers should construct this from trusted application/domain projections,
    never from raw client payloads or unrestricted database records.
    """

    fields: Mapping[str, str]
    context_version: str = "1"

    def to_prompt_text(self) -> str:
        if not self.fields:
            return ""
        return "\n".join(f"{key}: {value}" for key, value in sorted(self.fields.items()))
