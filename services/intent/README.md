# Pyrintu Intent Creation MVP

First vertical domain slice for turning a user's natural-language request into a validated, structured Intent object.

## Flow

```text
Natural-language request
        ↓
Intent interpreter
   ┌────┴─────┐
 deterministic  AI-backed
        ↓
Structured Intent
        ↓
Domain validation
        ↓
In-memory persistence
```

The persistence boundary is intentionally in memory for this first slice. Database wiring will follow the approved schema after the core domain behavior is validated.

`AIIntentInterpreter` accepts a narrow text-generation interface so the application can wire the existing `PyrintuAIGateway` without making the domain package depend on a vendor SDK. Tests use a deterministic stub; no live model call is required to validate the domain behavior.
