# Pyrintu Intent Creation MVP

First end-to-end domain slice for turning a user's natural-language intent into a validated, structured Intent object.

## Flow

```text
Natural-language request
        ↓
Intent interpreter
        ↓
Structured Intent
        ↓
Domain validation
        ↓
In-memory persistence
```

This MVP intentionally keeps persistence in memory. Database wiring will follow the approved schema once the core domain behavior is validated.

The interpreter depends on the existing `PyrintuAIGateway` abstraction. A deterministic interpreter is used in tests so the domain behavior does not depend on a live model call.
