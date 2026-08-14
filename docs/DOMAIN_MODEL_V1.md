# PYRINTU — CANONICAL DOMAIN MODEL v1.0

**Status:** Architecture checkpoint

## Purpose
Define the canonical domain entities and relationships that implement the approved UX and state-machine decisions without creating screen-specific business models.

## Core entities
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
- `PostMeetupOutcome`
- `UserLearningSignal`
- `PlanReliabilityEvaluation`

## Entity responsibilities

### User
Identity and user-owned profile/preferences. Must not contain transient meetup state.

### Intent
A user's current desired connection or experience, including goal, constraints, availability, and lifecycle state.

### Opportunity
A candidate experience or people/group opportunity surfaced from matching/discovery logic.

### Match
A candidate relationship between participants plus explicit mutuality state/signals.

### Group
A shared participant context for coordinated interaction, activity selection, planning, and conversation.

### Connection
A post-mutuality relationship state independent of any single meetup.

### Activity
Canonical catalog/domain representation of an activity and its requirements.

### Meetup
The real-world interaction lifecycle object. It references the canonical plan, participants, confirmation state, reservation state, operational state, and outcome.

### MeetupPlan
The current structured plan for a meetup: activity, date/time, venue, cost, duration, logistics, and readiness.

### MeetupPlanVersion
Immutable versioned representation of a plan revision. Material changes create a new version and can invalidate prior final-review/confirmation state.

### Proposal
A user-initiated proposal for a new meetup idea or material change to an existing meetup plan. A proposal is not automatically a confirmed meetup.

### Reservation
External/operational reservation state for a venue/activity. Reservation status is independent from participant confirmation.

### ParticipantConfirmation
Explicit participant decision against a specific meetup-plan version. Material plan changes can invalidate prior confirmations.

### Conversation
Structured communication context. Conversation text never outranks canonical structured state.

### SafetyCase
Cross-cutting safety/reporting record associated with a user, meetup, connection, group, or other supported context.

### Notification
User-facing delivery record derived from authoritative product events and user preferences.

### PostMeetupOutcome
Private post-meetup reflection, feedback, continuation preference, and safety signals linked to a completed/disrupted/cancelled meetup.

### UserLearningSignal
Derived recommendation signal produced from authorized history/outcomes. Must not rewrite historical facts and should include provenance/confidence.

### PlanReliabilityEvaluation
Evaluation of a meetup plan version across availability, venue certainty, cost stability, participant constraints, logistics, change risk, and fallback readiness.

## Canonical meetup dimensions
Do not overload one status field with every concept. Keep these dimensions separate:

```text
Meetup.status
MeetupPlanVersion.state
ParticipantConfirmation[]
Reservation.status
Meetup.operational_state
Meetup.outcome_state
```

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

## Material plan changes
Material changes include:
- activity
- date
- substantial time change
- venue
- significant cost change
- material participant-composition change

Material changes create a new `MeetupPlanVersion` and require the canonical reconfirmation rules to be evaluated again.

Minor operational updates may update the current plan context without invalidating confirmation when explicitly allowed by product rules.

## Confirmation model
A meetup is not confirmed because a client button was pressed. Confirmation is valid only when the server-authoritative rules determine that the current plan version and required participant confirmations satisfy the canonical eligibility conditions.

Recommended records:

```text
ParticipantConfirmation
- meetup_id
- participant_id
- plan_version_id
- decision
- decided_at
- invalidated_at
```

## Reservation model
Reservation remains independent:

```text
NOT_REQUIRED
PENDING
CONFIRMED
FAILED
CANCELLED
EXPIRED
```

A participant can confirm a meetup while reservation remains pending only where the product rules explicitly permit that intermediate state.

## Connection model
Connection state is independent of meetup lifecycle:

```text
NO_CONNECTION
MUTUAL_INTEREST
ACTIVE
QUIET
PAUSED
ENDED
BLOCKED
```

A completed meetup does not automatically create an active connection.

## Post-meetup learning
`PostMeetupOutcome` stores private historical reflection. `UserLearningSignal` is derived and used for future recommendations.

Example:

```text
PostMeetupOutcome
→ "quiet venue preferred"
→ UserLearningSignal(preference=quiet_environment)
```

Historical meetup facts remain immutable.

## Plan Reliability Engine
`PlanReliabilityEvaluation` should explain plan fragility instead of exposing an unexplained compatibility score.

Example:

```text
risk_level = MEDIUM
reasons = [
  venue_availability_low_confidence,
  flexible_participant_time,
  no_verified_fallback
]
```

Fallback plans should be modeled as alternate `MeetupPlanVersion`/proposal candidates rather than hidden AI state.

## Source-of-truth hierarchy
When surfaces disagree:

1. Current server-authoritative meetup state
2. Current `MeetupPlanVersion`
3. Current participant-confirmation state
4. Current reservation/operational verification
5. Conversation messages
6. AI-generated summaries

## Privacy boundaries
The domain model must support enforcement preventing exposure of:
- home address
- exact private location
- hidden availability
- private intent notes
- safety reports
- private participant hesitation
- private payment credentials

## Safety architecture
Safety is a cross-cutting service/domain area. It must not be implemented independently per screen.

Supported contexts can include:
- meetup
- group
- connection
- user interaction
- post-meetup report

## AI architecture boundary
AI consumes authorized structured context and produces explanations, suggestions, proposals, or drafts.

AI must not directly own or silently mutate authoritative domain state.

```text
Structured Domain State
        ↓
AI Orchestration
        ↓
Suggestion / Explanation / Draft
        ↓
Explicit User Action
        ↓
Validated Domain Command
        ↓
Authoritative State Change
```

## Recommended relationships

```text
User ──< Intent
User ──< Match participant
Match ──> Group / Connection
Group ──< User membership
Group ──< Meetup
Meetup ──1 MeetupPlan
MeetupPlan ──< MeetupPlanVersion
Meetup ──< Proposal
Meetup ──< ParticipantConfirmation
Meetup ──0..1 Reservation
Meetup ──< Conversation event/context
Meetup ──< SafetyCase
Meetup ──0..1 PostMeetupOutcome per participant
PostMeetupOutcome ──> UserLearningSignal
MeetupPlanVersion ──0..1 PlanReliabilityEvaluation
```

## Implementation constraints
Do not create:
- screen-specific databases
- duplicate planning engines
- duplicate confirmation engines
- duplicate day-of state models
- screen-specific safety logic
- AI-owned authoritative state

## Required next architecture artifacts
Before application implementation:

1. state-transition specification
2. authorization matrix
3. API contracts
4. persistence schema
5. event/notification model
6. frontend route/view map
7. AI tool contracts
8. idempotency/error strategy
9. audit logging policy
10. transition test matrix
