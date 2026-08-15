# Pyrintu AI Gateway

Small provider-agnostic gateway for Pyrintu's AI layer.

## MVP behavior

- Domain/application code depends on `LLMProvider`, not a vendor SDK.
- OpenAI is the first concrete provider adapter.
- `MockProvider` enables deterministic tests without external calls.
- The gateway requires an authorized context before it calls a provider.
- The gateway can return an `ACTION_PROPOSAL`, but it never executes domain actions.
- API keys are read by the provider SDK from environment configuration and are never accepted from user payloads.

## Local setup

```bash
python -m venv .venv
.venv\\Scripts\\activate  # Windows
pip install -e .[test]
pytest
```

For live OpenAI calls, configure `OPENAI_API_KEY` in the runtime environment. The implementation uses the official OpenAI Python SDK and Responses API. Provider/model selection remains behind the `LLMProvider` interface.

The provider layer is intentionally small so a Gemini or other adapter can be added without changing the gateway or domain code.
