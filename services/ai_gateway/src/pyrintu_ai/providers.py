"""Provider adapters. The domain layer must depend only on LLMProvider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ProviderResult:
    text: str
    provider: str
    model: str
    request_id: str | None = None


class LLMProvider(Protocol):
    def generate(self, *, instructions: str, user_input: str, model: str | None = None) -> ProviderResult:
        """Generate text without mutating Pyrintu domain state."""


class OpenAIProvider:
    """OpenAI Responses API adapter.

    API keys are read from the environment by the official SDK. No key is accepted
    from callers, preventing accidental propagation through application payloads.
    """

    def __init__(self, client=None, default_model: str = "gpt-5.5") -> None:
        if client is None:
            from openai import OpenAI

            client = OpenAI()
        self._client = client
        self._default_model = default_model

    def generate(self, *, instructions: str, user_input: str, model: str | None = None) -> ProviderResult:
        response = self._client.responses.create(
            model=model or self._default_model,
            instructions=instructions,
            input=user_input,
        )
        return ProviderResult(
            text=response.output_text,
            provider="openai",
            model=model or self._default_model,
            request_id=getattr(response, "_request_id", None),
        )


class MockProvider:
    """Deterministic test provider; never contacts an external model."""

    def __init__(self, text: str = "MOCK_AI_RESPONSE") -> None:
        self.text = text
        self.calls: list[tuple[str, str, str | None]] = []

    def generate(self, *, instructions: str, user_input: str, model: str | None = None) -> ProviderResult:
        self.calls.append((instructions, user_input, model))
        return ProviderResult(
            text=self.text,
            provider="mock",
            model=model or "mock",
            request_id="mock-request",
        )
