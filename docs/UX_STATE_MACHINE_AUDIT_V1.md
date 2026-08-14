# PYRINTU — UX STATE MACHINE AUDIT v1.0

**Status:** Architecture checkpoint

## Audit basis
This audit reviews the approved UX specifications in `docs/UX_SCREEN_*.md`, with particular attention to the later lifecycle screens and their handoffs. The purpose is to prevent duplicate application logic before implementation.

## Executive conclusion
The 30 documents should **not** become 30 independent application modules. Several are different views/states of the same underlying product objects and lifecycle transitions.

The architecture should be driven by a canonical state machine and shared domain entities. Screens are presentation surfaces over those states.

## Key overlap findings

### 1. Screen 17 ↔ Screen 26 — planning
Screen 17 defines the canonical Activity Plan: activity, date, time, venue, cost, logistics, participant review, versioning, and handoff to confirmation.

Screen 26 defines collaborative shared planning for a second meetup, but explicitly reuses Activity Selection, Activity Plan, venue verification, cost, safety, and confirmation systems.

**Decision:** keep one `MeetupPlan` domain model and one planning engine. Screen 26 is a collaborative planning view over the same planning primitives, not a second planner implementation.

### 2. Screen 19 ↔ Screen 27 — confirmation
Screen 19 defines canonical final confirmation semantics: explicit participant confirmation, deterministic eligibility, reservation/payment boundaries, version revalidation, and confirmed state.

Screen 27 defines synchronized two-person final review but explicitly says to reuse the canonical confirmation semantics.

**Decision:** maintain one confirmation state machine. Screen 27 is a shared-review presentation of the same confirmation boundary, not a second definition of `Confirmed`.

### 3. Screen 20 ↔ Screen 28 — upcoming/operational meetup
Screen 20 is the participant's operational home after confirmation. Screen 28 is a deeper operations/change surface for the same confirmed meetup, including material changes, reconfirmation, reservation state, and logistics.

**Decision:** one `Meetup` operational domain. Screens 20 and 28 should become route/view variants over the same canonical meetup state, not separate backend concepts.

### 4. Screen 21 ↔ Screen 29 — day-of
Screen 21 defines the calm day-of operational surface. Screen 29 expands the same concern into live execution: arrival signals, running late, venue problems, safety exit, and completion handoff.

**Decision:** one day-of state machine. The implementation should not create duplicate `DayOfMeetup` logic. Screen 21 can be the day-of entry view; Screen 29 can be the richer live-execution state for the same meetup.

### 5. Screen 22 ↔ Screen 30 — post-meetup
Screen 22 defines post-meetup reflection, safety reporting, continued-interest signals, historical stability, and transition to connection/discovery.

Screen 30 intentionally narrows the same lifecycle endpoint: completed state, private reflection, safety, continued connection, history, and return to the product.

**Decision:** one `PostMeetup` lifecycle state and one historical record. Screen 30 should be treated as the final consolidated presentation state rather than an independent completion engine.

## Canonical domain entities

The implementation should center on these entities:

- `User`
- `Intent`
- `Opportunity`
- `Match`
- `Group`
- `Connection`
- `Activity`
- `Meetup`
- `MeetupPlan`
- `MeetupPlanVersion`
- `Proposal`
- `Reservation`
- `ParticipantConfirmation`
- `Conversation`
- `SafetyCase`
- `Notification`

These are domain concepts, not screen concepts.

## Canonical meetup lifecycle

```text
DRAFT / DISCOVERY
    ↓
MATCH / MUTUALITY
    ↓
GROUP / CONNECTION
    ↓
ACTIVITY SELECTION
    ↓
MEETUP PLAN
    ↓
SHARED REVIEW / PROPOSAL
    ↓
FINAL REVIEW
    ↓
PARTICIPANT CONFIRMATIONS
    ↓
OPERATIONAL VALIDATION
    ↓
CONFIRMED
    ↓
UPCOMING
    ↓
DAY_OF
    ↓
IN_PROGRESS
    ↓
COMPLETED / DISRUPTED / CANCELLED
    ↓
POST_MEETUP
    ↓
CONTINUED_CONNECTION / DISCOVERY / CLOSED
```

## Confirmation state rule

The word **Confirmed** should have one canonical meaning across the product.

Participant intent, plan agreement, reservation status, and operational readiness are related but distinct dimensions.

Recommended shape:

```text
Meetup.status
Plan.version
ParticipantConfirmation[]
Reservation.status
OperationalState
```

Do not encode all of these as one overloaded boolean.

## Planning state rule

Use one versioned plan model.

Example:

```text
MeetupPlan v3
  activity = board_games
  date = 2030-08-30
  time = 18:30
  venue = venue_123
  cost = estimated

v3 → ready_for_review
v4 → needs_review after material change
```

A material change invalidates stale final-review state according to the canonical confirmation rules.

## Change classification

### Material changes
- activity
- date
- substantial time change
- venue
- significant cost change
- material participant composition change

### Minor operational changes
- parking note
- entrance note
- contact-note update
- other non-material logistics

Material changes may require reconfirmation. Minor changes should not unless product rules say otherwise.

## Source-of-truth hierarchy

When surfaces disagree, use this precedence:

1. Current server-authoritative meetup state
2. Current `MeetupPlanVersion`
3. Current participant confirmation state
4. Current reservation/operational verification
5. Conversation messages
6. AI-generated summaries

Chat and AI must never outrank structured state.

## Privacy boundaries

Never use a screen as justification to expose:

- home address
- exact private location
- hidden availability
- private intent notes
- safety reports
- private participant hesitation
- private payment credentials

Only expose decision-relevant information.

## AI boundary

AI is an advisory/interpretation layer.

AI may:
- summarize structured state
- explain changes
- suggest options
- translate natural language into explicit proposals
- draft messages

AI may not:
- infer consent
- declare mutuality without verified signals
- invent operational facts
- confirm/book/pay autonomously
- silently mutate structured state
- expose private participant data

## Safety boundary

Safety is cross-cutting and must not be screen-specific.

The same domain/service should power:
- report
- block
- safety case
- leave/cancel
- post-meetup reporting

Safety controls remain available across meetup states.

## Navigation model recommendation

The final implementation should use a small number of canonical product surfaces with state-driven rendering rather than 30 isolated routes.

Suggested high-level surfaces:

```text
/onboarding
/discovery
/match
/group
/plan
/confirmation
/meetup/:id
/connection/:id
/history
/safety
```

Within `/meetup/:id`, the UI changes based on meetup state instead of creating separate backend systems for upcoming, operations, and day-of.

## Implementation implications

### Reuse
- one meetup entity
- one plan/version model
- one confirmation engine
- one reservation state model
- one notification service
- one safety service
- one AI orchestration layer

### Avoid
- duplicate confirmation logic
- duplicate venue verification
- duplicate plan models
- duplicate day-of state
- duplicate post-meetup completion state
- screen-specific business rules embedded in components

## Architecture checkpoint

Before application code begins, define:

1. domain model and state transitions
2. authorization matrix
3. API contracts
4. persistence schema
5. frontend route/view map
6. event/notification model
7. AI tool boundaries
8. error/idempotency strategy
9. audit logging requirements
10. test matrix for state transitions

## Verdict

The 30-screen UX phase is directionally coherent, but implementation should treat the documents as **UX views over a smaller canonical domain/state model**.

This resolves the overlap concern without discarding the approved UX work.

**Next phase:** domain/state architecture before feature implementation.
