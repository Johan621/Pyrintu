# PYRINTU — SYSTEM ARCHITECTURE v1.0

**Status:** Architecture checkpoint

## 1. Purpose

Define the technical boundaries required to implement the approved Pyrintu product without tying the design to a specific cloud vendor, framework, or ORM.

The architecture must preserve the product source of truth, canonical domain transitions, authorization rules, privacy boundaries, and the two differentiating capabilities:

- Plan Reliability Engine
- Post-Meetup Learning

## 2. Architecture principles

1. The server is authoritative for identity, authorization, domain state, and consequential transitions.
2. UI screens are projections of domain state; screens do not own business rules.
3. AI is advisory and orchestrated through typed proposals; it is never a direct domain authority.
4. Sensitive data is protected at service, storage, and response-projection boundaries.
5. Material plan changes are versioned and revalidated.
6. Consequential writes are idempotent and concurrency-safe.
7. Background work is asynchronous where latency or external dependencies make synchronous execution inappropriate.
8. External integrations are isolated behind adapters so providers can change without changing domain semantics.
9. Observability is built into domain mutations rather than added after launch.
10. MVP architecture should be modular enough to scale, but not fragmented into unnecessary microservices.

## 3. Recommended deployment shape

Start as a **modular monolith** with separately deployable frontend and backend components, plus a worker process for asynchronous jobs.

```text
Web / Mobile Client
        |
        v
   API / Backend
        |
  +-----+---------------------------+
  | Domain / Application Modules    |
  |                                 |
  | Identity & Profile              |
  | Intent & Discovery              |
  | Match / Mutuality               |
  | Group / Connection              |
  | Meetup / Planning               |
  | Confirmation / Reservation      |
  | Safety / Trust                  |
  | Plan Reliability                |
  | Post-Meetup Learning            |
  | AI Orchestration                |
  +-----+---------------------------+
        |
  +-----+---------------------------+
  | Persistence / Cache / Queue     |
  +-----+---------------------------+
        |
  +-----+---------------------------+
  | External adapters               |
  | Maps / venues / notifications   |
  | Payments / reservations         |
  | AI provider(s)                  |
  +---------------------------------+

          Background Worker
```

Do not start with independent microservices for each domain. The domains should be modular in code and API boundaries while sharing one transactional persistence boundary until scale or team structure justifies extraction.

## 4. Frontend boundary

The frontend is responsible for:

- rendering authorized projections
- local interaction state
- optimistic presentation only where safe
- input validation for user experience
- accessibility
- navigation
- displaying loading, empty, error, and stale-state states

The frontend must not be trusted for:

- authorization
- final state transitions
- mutuality calculation
- confirmation validity
- reservation validity
- safety permissions
- reliability risk decisions
- private-field filtering

Recommended frontend structure:

```text
app/
  routes/
  features/
    onboarding/
    discovery/
    matches/
    connections/
    groups/
    meetups/
    safety/
  components/
  api/
  state/
  validation/
```

Feature modules should map to domain capabilities, not to the 30 historical UX documents.

## 5. Backend boundary

The backend contains four logical layers:

```text
HTTP / Transport
        ↓
Application Services
        ↓
Domain Services / Policies
        ↓
Repositories / External Adapters
```

### Transport layer

Responsible for:

- authentication extraction
- request parsing
- response projection
- error mapping
- rate limiting hooks

### Application layer

Responsible for:

- orchestration of use cases
- authorization invocation
- transaction boundaries
- idempotency
- publishing domain events

### Domain layer

Responsible for:

- state transitions
- invariants
- mutuality
- planning rules
- confirmation rules
- reliability evaluation
- connection lifecycle
- safety constraints

### Infrastructure layer

Responsible for:

- database access
- queue access
- cache
- external service adapters
- email/push providers
- AI provider adapters

## 6. Canonical module map

### Identity

Owns authenticated user identity projection and account lifecycle.

### Intent & Discovery

Owns Intent lifecycle, opportunity retrieval, and discovery projections.

### Match & Mutuality

Owns participant decisions, mutuality reveal rules, and match lifecycle.

### Group & Connection

Owns group membership, direct connection state, pause/end/block semantics.

### Meetup

Owns Meetup aggregate, participants, plan versions, operational state, and completion.

### Reservation

Owns reservation state and external reservation adapter interaction.

### Safety

Owns reports, blocks, safety-case access, and moderation boundaries.

### Plan Reliability

Owns deterministic plan checks, risk classification, reasons, and fallbacks.

### Learning

Owns private post-meetup outcome capture and derived user learning signals.

### AI Orchestration

Owns context assembly, authorization filtering, model invocation, typed proposals, and evaluation metadata.

## 7. Domain event flow

Consequential transitions should produce domain events after the authoritative transaction succeeds.

Example:

```text
Confirm participant
      ↓
Transaction commits
      ↓
participant.confirmed
      ↓
Queue / worker
      ├── notification
      ├── analytics projection
      └── reliability reevaluation where needed
```

The event stream is not a second source of truth. It is a record/projection mechanism driven by authoritative state.

## 8. Background worker responsibilities

Use asynchronous workers for:

- notification delivery
- email/push fan-out
- stale reliability reevaluation
- recommendation refresh
- learning-signal derivation
- external reservation polling/webhooks where supported
- analytics/event projection
- AI-heavy non-interactive jobs

Do not move core authorization or final state transition decisions into asynchronous workers when the user expects an immediate authoritative result.

## 9. Cache policy

Cache only data whose staleness is acceptable.

Good candidates:

- public activity metadata
- venue discovery results
- non-sensitive recommendation candidates
- read-heavy projections with explicit freshness bounds

Do not treat cache as authoritative for:

- participant confirmation
- connection state
- safety access
- reservation state
- current meetup plan version
- permission decisions

## 10. Plan Reliability Engine architecture

The Plan Reliability Engine is deterministic.

```text
Current Plan Version
        ↓
Constraint Resolver
        ↓
Checks
  ├── Availability
  ├── Venue
  ├── Cost
  ├── Participant constraints
  ├── Logistics
  └── Change risk
        ↓
Risk classifier
        ↓
Reasons + fallback candidates
```

The result is stored against the plan version.

AI may explain or summarize the result, but it does not decide the risk classification.

## 11. Post-Meetup Learning architecture

```text
Private outcome
      ↓
Validation / privacy policy
      ↓
Learning signal derivation
      ↓
User-specific preference signals
      ↓
Future recommendation features
```

Source facts remain immutable. Derived signals must reference their source meetup/outcome.

Learning signals must be:

- user-scoped
- traceable
- confidence-aware where inference is involved
- revocable/recomputable
- excluded from public social projections

## 12. AI architecture

AI access follows this path:

```text
User question / task
       ↓
Authorized context resolver
       ↓
Structured domain context
       ↓
Prompt / tool orchestration
       ↓
Model provider
       ↓
Typed result
       ↓
Policy validation
       ↓
User-visible answer or proposal
```

AI must never receive unauthorized fields merely because they exist in the database.

### Typed AI result classes

- `ANSWER`
- `SUGGESTION`
- `DRAFT`
- `ACTION_PROPOSAL`
- `REFUSAL`
- `INSUFFICIENT_CONTEXT`

`ACTION_PROPOSAL` is still uncommitted until an authorized application service validates and applies the user's explicit action.

## 13. External integration adapters

External providers must be behind interfaces such as:

```text
VenueProvider
ReservationProvider
MapProvider
NotificationProvider
PaymentProvider
AIProvider
```

The domain layer must not depend on provider-specific response shapes.

## 14. Security architecture

Baseline controls:

- authenticated API boundary
- deny-by-default authorization
- field-level response projections
- encrypted transport
- encrypted sensitive storage where appropriate
- secret management outside source control
- rate limiting
- abuse prevention
- audit logging for sensitive operations
- least-privilege service credentials
- separate staff/safety privilege boundary

Never put private safety text, payment secrets, or raw provider credentials into normal analytics events.

## 15. Concurrency architecture

Use optimistic concurrency for plan and meetup state.

Every mutation that depends on a version should validate that version server-side.

Stale writes return a typed conflict such as:

`PLAN_VERSION_STALE`

The client then reloads the latest projection rather than overwriting it.

## 16. Idempotency architecture

Consequential operations should support idempotency keys:

- confirmation
- reconfirmation
- reservation confirmation
- cancellation
- leave/withdrawal
- plan change creation
- safety report submission where duplicate creation is possible
- payment-related operations

The application service records the idempotency key and replays the prior result for safe retries.

## 17. API response architecture

Prefer explicit response projections:

```text
MeetupPrivateProjection
MeetupParticipantProjection
MeetupPublicProjection
ConnectionProjection
SafetyCaseProjection
ReliabilityProjection
```

Do not return raw ORM/database records from controllers.

This keeps authorization and privacy decisions centralized.

## 18. Observability

Every request should have:

- request ID
- authenticated actor ID where available
- operation name
- outcome
- latency

Every consequential domain mutation should emit structured audit/telemetry fields without leaking private content.

Monitor at minimum:

- API error rate
- authorization failures
- stale-plan conflicts
- confirmation conversion
- reservation failures
- notification delivery failures
- AI failures/timeouts
- reliability evaluation failures
- safety workflow failures
- queue lag
- database latency

## 19. Testing architecture

Testing layers:

```text
Unit tests
  ↓
Domain transition tests
  ↓
Application service tests
  ↓
API contract tests
  ↓
Integration tests
  ↓
End-to-end critical flows
```

Highest-priority invariants to test:

- user cannot mutate another user's decision
- one-sided interest never becomes mutuality
- stale plan versions cannot overwrite newer plans
- material changes invalidate required confirmations
- reservation state cannot imply participant consent
- AI cannot perform consequential action without explicit authorization
- blocked users cannot receive normal protected projections
- private feedback is never returned to another participant

## 20. MVP extraction rule

Keep all domains in one deployable backend initially.

Consider service extraction only when there is a demonstrated reason such as:

- independent scaling requirement
- strong isolation requirement
- external-team ownership
- operational reliability boundary
- provider-specific infrastructure need

Do not create microservices merely because the domain list is large.

## 21. Initial implementation order

```text
1. Project scaffolding
2. Authentication / session boundary
3. Database migrations
4. Identity + profile
5. Intent / discovery primitives
6. Match / mutuality
7. Group / connection
8. Meetup + plan versions
9. Confirmation
10. Reservation adapter boundary
11. Safety
12. Plan Reliability Engine
13. Post-Meetup Learning
14. AI orchestration
15. Notifications / workers
16. Analytics / observability
17. Critical end-to-end flows
```

## 22. Architecture acceptance criteria

- No business transition is owned by a screen component.
- No AI output directly mutates domain state.
- All consequential mutations have authorization and current-state validation.
- Plan versions are immutable after creation.
- Confirmation is version-scoped.
- Reservation is independent from participant confirmation.
- Private fields are protected by explicit response projections.
- Domain modules can be tested independently inside the modular monolith.
- External providers are replaceable through adapters.
- The MVP can run without microservices.
- The architecture supports the Plan Reliability Engine and Post-Meetup Learning without introducing parallel sources of truth.
