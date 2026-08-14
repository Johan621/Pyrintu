# PYRINTU — CANONICAL STATE TRANSITIONS v1.0

**Status:** Architecture checkpoint

## Purpose

Define the allowed lifecycle transitions for Pyrintu's canonical domain objects before API or persistence implementation. UI screens are views over these transitions; they do not create separate business rules.

## 1. Intent lifecycle

```text
DRAFT → ACTIVE → MATCHING → PAUSED
                     ↓
                  EXPIRED
                     ↓
                  CLOSED
```

Allowed transitions:

- `DRAFT → ACTIVE`: required intent fields are valid and the user submits the intent.
- `ACTIVE → MATCHING`: the system begins generating/evaluating opportunities.
- `MATCHING → PAUSED`: the owner pauses the intent.
- `PAUSED → ACTIVE`: the owner resumes the intent.
- `ACTIVE/MATCHING/PAUSED → EXPIRED`: an explicit product expiration rule is reached.
- `ACTIVE/MATCHING/PAUSED → CLOSED`: the owner closes the intent.

No AI operation may close, expire, or activate an intent without an explicit product-authorized action.

## 2. Opportunity lifecycle

```text
GENERATED → AVAILABLE → VIEWED → RESPONDED
                               ↘ EXPIRED
```

An opportunity is derived from eligible signals and does not itself create mutuality.

## 3. Match / mutuality lifecycle

```text
CANDIDATE
   ↓
SHOWN
   ↓
USER_INTEREST
   ↓
MUTUAL_INTEREST
   ↓
CONNECTION_ELIGIBLE
```

Negative or stale outcomes terminate the candidate path without creating a connection.

Rules:

- One-sided interest must remain private unless product policy explicitly says otherwise.
- `MUTUAL_INTEREST` requires independently recorded compatible signals.
- Chat tone, AI inference, or recommendation scores cannot create mutuality.

## 4. Connection lifecycle

```text
NONE → ACTIVE → QUIET → PAUSED → ENDED
         ↘                    ↘
          BLOCKED              BLOCKED
```

Allowed transitions:

- `NONE → ACTIVE`: verified mutuality creates an eligible connection.
- `ACTIVE → QUIET`: inactivity threshold or explicit product classification.
- `QUIET → ACTIVE`: authorized interaction resumes the connection.
- `ACTIVE/QUIET → PAUSED`: participant pauses the connection.
- `PAUSED → ACTIVE`: participant explicitly resumes it.
- `ACTIVE/QUIET/PAUSED → ENDED`: participant explicitly ends the connection or a policy-driven termination occurs.
- Any non-ended state → `BLOCKED`: participant blocks the other party.

A completed meetup does not automatically create an active connection.

## 5. Group lifecycle

```text
CREATING → ACTIVE → PLANNING → MEETUP_CONFIRMED → COMPLETED
                           ↘             ↘
                            DISBANDED     CANCELLED
```

Group rules:

- Membership changes that affect meetup eligibility require revalidation.
- Group chat is a coordination surface; structured meetup state remains authoritative.
- A group can be archived after completion without deleting historical meetup facts.

## 6. Meetup lifecycle

Canonical states:

```text
DRAFT
  ↓
PLANNING
  ↓
READY_FOR_REVIEW
  ↓
AWAITING_CONFIRMATION
  ↓
CONFIRMED
  ↓
UPCOMING
  ↓
DAY_OF
  ↓
IN_PROGRESS
  ↓
COMPLETED
```

Exception states:

```text
PLANNING / READY_FOR_REVIEW / AWAITING_CONFIRMATION
    ↓
CANCELLED

CONFIRMED / UPCOMING / DAY_OF / IN_PROGRESS
    ↓
DISRUPTED
    ↓
COMPLETED or CANCELLED
```

Transition rules:

### `DRAFT → PLANNING`
A meetup object is created from an approved intent/proposal and enters collaborative planning.

### `PLANNING → READY_FOR_REVIEW`
All required plan fields are present and the plan passes deterministic readiness checks.

### `READY_FOR_REVIEW → AWAITING_CONFIRMATION`
The current plan version is locked for participant final review.

### `AWAITING_CONFIRMATION → CONFIRMED`
All required participant confirmations are valid for the current plan version and required operational conditions are satisfied.

### `CONFIRMED → UPCOMING`
The confirmed meetup is scheduled for a future point in time.

### `UPCOMING → DAY_OF`
The meetup enters its operational day window according to deterministic product rules.

### `DAY_OF → IN_PROGRESS`
The meetup begins according to explicit operational rules; do not infer this solely from passive location data.

### `IN_PROGRESS → COMPLETED`
The meetup satisfies the defined completion rule or an authorized participant ends it where supported.

### Material-change rule

A material change to activity, date, substantial time, venue, significant cost, or material participant composition invalidates stale final-review state.

Canonical pattern:

```text
CONFIRMED
   ↓ material change
CHANGE_REVIEW
   ↓
AWAITING_RECONFIRMATION
   ↓
CONFIRMED
```

The prior confirmation must not silently carry forward.

### Minor-change rule

Non-material logistics updates may keep the meetup confirmed if product policy classifies them as minor and no safety/eligibility rule is affected.

## 7. Meetup plan lifecycle

```text
DRAFT → PROPOSED → READY_FOR_REVIEW → AGREED → CONFIRMED
```

`MeetupPlanVersion` is immutable after publication. A material edit creates a new version.

Example:

```text
v3 → READY_FOR_REVIEW
v4 → NEEDS_REVIEW after venue change
```

Only the current version may receive final confirmation.

## 8. Participant confirmation lifecycle

```text
PENDING → CONFIRMED
PENDING → DECLINED
CONFIRMED → INVALIDATED
```

`CONFIRMED → INVALIDATED` occurs when the confirmed plan version becomes stale because of a material change or participant eligibility change.

A participant confirmation is always tied to:

- meetup
- participant
- plan version
- decision time

## 9. Reservation lifecycle

```text
NOT_REQUIRED

PENDING → CONFIRMED
PENDING → FAILED
PENDING → EXPIRED
CONFIRMED → CANCELLED
```

Reservation state is independent from participant confirmation.

`CONFIRMED` meetup status must never be inferred from reservation state alone.

## 10. Operational state

Operational readiness is a separate dimension:

```text
NOT_CHECKED → READY
NOT_CHECKED → ATTENTION_REQUIRED
READY → ATTENTION_REQUIRED
ATTENTION_REQUIRED → READY
```

Examples of `ATTENTION_REQUIRED`:

- venue unavailable
- reservation failure
- material verified disruption
- participant eligibility changed

## 11. Post-meetup lifecycle

```text
NONE → AVAILABLE → REVIEWED → CLOSED
```

Post-meetup state is available after `COMPLETED`, `DISRUPTED`, or permitted `CANCELLED` outcomes.

Reflection is optional. Safety reporting can remain available after the post-meetup state is closed according to policy.

## 12. Learning-signal lifecycle

Learning signals are derived, not historical rewrites:

```text
OBSERVED → VALIDATED → ACTIVE_SIGNAL → SUPERSEDED
```

A new signal does not mutate the original meetup record.

Example:

```text
Past meetup: Badminton
Outcome: venue too crowded
↓
Learning signal: prefer quieter venues
↓
Future recommendation uses the signal
```

## 13. Plan Reliability Engine lifecycle

```text
NOT_EVALUATED → EVALUATING → EVALUATED
                            ↘ FAILED_TO_EVALUATE
```

An evaluation should include explicit reasons, not just a scalar score.

Possible risk classification:

```text
LOW_RISK
MEDIUM_RISK
HIGH_RISK
BLOCKED
```

Risk classification does not itself change meetup state. A deterministic product rule maps blocking conditions to the appropriate transition.

## 14. Safety case lifecycle

```text
OPEN → TRIAGED → IN_REVIEW → RESOLVED
                         ↘ ESCALATED
```

Safety controls are cross-cutting. Creating a safety case must not silently fabricate meetup state or expose the reporter.

## 15. Source-of-truth rule

When surfaces disagree, precedence is:

1. server-authoritative canonical domain state
2. current `MeetupPlanVersion`
3. participant confirmation state
4. reservation/operational verification
5. conversation content
6. AI-generated interpretation

Conversation and AI may propose changes but cannot outrank structured state.

## 16. Authorization rule

Every transition must validate authorization for the actor and current state.

Examples:

- only the intent owner can close their intent
- only eligible participants can confirm their participation
- only authorized participants can modify shared planning inputs
- only authorized users/services can create or update reservations
- safety reports remain private to authorized safety workflows

## 17. Idempotency rule

State-changing commands must be idempotent.

Repeated requests must not create:

- duplicate meetup confirmations
- duplicate reservations
- duplicate charges
- duplicate safety cases
- duplicate notifications
- duplicate plan versions

## 18. Concurrency rule

State transitions must use current server state and version checks.

If a user acts on a stale version:

```text
STALE_REQUEST
   ↓
REJECT_STALE_MUTATION
   ↓
RETURN_CURRENT_STATE
```

The client must then re-render from canonical state.

## 19. AI transition boundary

AI may:

- explain current state
- suggest a transition
- translate natural language into a proposed change
- draft communications

AI may not directly perform consequential state transitions unless the product explicitly exposes an authorized action and the user confirms it.

## 20. Final transition matrix requirement

Before API implementation, each command must have:

- actor
- current state
- target state
- preconditions
- authorization rule
- side effects
- idempotency key
- audit event
- failure behavior

The next architecture artifact should formalize this command-level matrix for the API layer.

## Verdict

This document establishes one canonical transition model across the product. Screens are presentation surfaces; domain services own transitions. The next step is the authorization matrix and API contract specification.