# PYRINTU — AUTHORIZATION MATRIX + API CONTRACTS v1.0

**Status:** Architecture checkpoint

## Purpose

This document defines who may perform which domain actions, the authorization rules that must hold before a transition, and the first canonical HTTP API contract surface. It is derived from the approved UX/state-machine audit, domain model, and state-transition specification.

No database schema is defined here. No framework-specific implementation is prescribed.

## 1. Authorization principles

1. Deny by default.
2. Authorization is evaluated on current server state, not client-provided UI state.
3. Object ownership, participant membership, connection state, meetup state, and action-specific rules are all enforced server-side.
4. Private data is returned only when the requester is authorized for that field.
5. A screen being able to render an action does not itself grant permission.
6. Safety actions remain available independently of normal social state where applicable.
7. AI has no independent authority to perform consequential actions.

## 2. Roles

### User

A normal authenticated Pyrintu account.

### Participant

A user attached to a relevant Intent, Match, Group, Connection, or Meetup.

### Group member

A participant with active membership in a Group.

### Connection participant

A user on one side of an established Connection.

### Staff / safety operator

A separately authorized operational role for safety/moderation workflows. Staff access is outside ordinary user APIs and must be audited.

### System service

Trusted backend services may perform domain transitions only through explicit service permissions and invariants. AI is not a system authority role.

## 3. Core authorization matrix

| Action | User owner | Participant | Group member | Connection participant | Staff |
|---|---|---|---|---|---|
| Read own profile | Allow | Allow | Allow | Allow | Policy-controlled |
| Update own profile | Allow | Allow | Allow | Allow | Policy-controlled |
| Create own Intent | Allow | N/A | N/A | N/A | Policy-controlled |
| Read own Intent | Allow | N/A | N/A | N/A | Policy-controlled |
| Edit own Intent | Allow while editable | N/A | N/A | N/A | Policy-controlled |
| View Opportunity | Allow if returned to user | N/A | N/A | N/A | Policy-controlled |
| Read Match | Allow if member | Allow if member | N/A | N/A | Policy-controlled |
| Express Match decision | Allow on own decision | Allow on own decision | N/A | N/A | No |
| Read mutuality state | Own side only until revealable | Own side only until revealable | N/A | Per mutuality rules | Policy-controlled |
| Create Group | Allow when eligible | Allow when eligible | N/A | N/A | No |
| Read Group | Member only | Member only | Allow | N/A | Policy-controlled |
| Update Group settings | Authorized group role only | Authorized group role only | Role-dependent | N/A | Policy-controlled |
| Leave Group | Allow | Allow | Allow | N/A | Policy-controlled |
| Create MeetupPlan | Authorized planner participant | Authorized planner participant | Authorized member | Authorized connection participant | Policy-controlled |
| Edit MeetupPlan | Authorized planner participant | Authorized planner participant | Authorized member | Authorized connection participant | Policy-controlled |
| Create PlanVersion | Authorized planner participant | Authorized planner participant | Authorized member | Authorized connection participant | Policy-controlled |
| Review proposed plan | Required participant only | Required participant only | Required participant only | Required participant only | Policy-controlled |
| Confirm participation | Own confirmation only | Own confirmation only | Own confirmation only | Own confirmation only | No normal-user override |
| Read another participant's private confirmation | No | No by default | No by default | No | Policy-controlled |
| Read aggregate confirmation readiness | Authorized meetup participant | Authorized meetup participant | Authorized meetup participant | Authorized meetup participant | Policy-controlled |
| Create reservation | Authorized service / explicit user action | Authorized user when allowed | N/A | N/A | Policy-controlled |
| Read reservation details | Authorized participant; sensitive fields filtered | Same | Same | Same | Policy-controlled |
| Approve payment | Paying user only | Paying user only | Paying user only | Paying user only | No normal-user override |
| Propose meetup change | Authorized participant | Authorized participant | Authorized participant | Authorized connection participant | Policy-controlled |
| Accept own required change/reconfirmation | Own decision only | Own decision only | Own decision only | Own decision only | No normal-user override |
| Cancel own participation | Participant only | Participant only | Participant only | Participant only | Policy-controlled |
| Cancel entire Meetup | Requires domain rule/authorized actor | Requires domain rule/authorized actor | Requires domain rule/authorized actor | Requires domain rule/authorized actor | Policy-controlled |
| Read Meetup | Authorized participant | Authorized participant | Authorized participant | Authorized connection participant where applicable | Policy-controlled |
| Open Meetup day-of state | Authorized participant | Authorized participant | Authorized participant | Authorized connection participant where applicable | Policy-controlled |
| Mark self on-way/arrived | Own participant record only | Own participant record only | Own participant record only | Own participant record only | No normal-user override |
| Report SafetyCase | Any eligible reporter | Any eligible reporter | Any eligible reporter | Any eligible reporter | Staff can process |
| Read SafetyCase | Reporter only for own limited status; subject access denied by default | Same | Same | Same | Authorized safety staff |
| Block user | User acting on own block list | Same | Same | Same | Policy-controlled |
| End Connection | Connection participant on own side | N/A | N/A | Allow on own side | Policy-controlled |
| Pause Connection | Connection participant on own side | N/A | N/A | Allow on own side | Policy-controlled |
| Read post-meetup history | User's own history; authorized shared history only | Same | Same | Shared fields only | Policy-controlled |
| Submit post-meetup feedback | Own feedback only | Own feedback only | Own feedback only | Own feedback only | No normal-user override |
| Read another participant's private feedback | No | No | No | No | Policy-controlled |
| Update learning preferences/signals | Derived from authorized own data | N/A | N/A | N/A | Policy-controlled |
| Ask AI factual question | Authorized user | Authorized user | Authorized user | Authorized user | Policy-controlled |
| Ask AI to perform consequential action | Not directly allowed | Not directly allowed | Not directly allowed | Not directly allowed | Through explicit service workflow only |

## 4. Field-level privacy rules

The API must distinguish object authorization from field authorization.

Never expose by default:

- exact home address
- exact private location
- hidden availability
- private intent notes
- private participant hesitation
- private safety report contents
- payment credentials
- private feedback text
- internal risk/recommendation features

Allowed shared fields should be deliberately modeled as public/shared projections rather than filtering sensitive fields ad hoc in every endpoint.

## 5. Authorization checks by domain

### Intent

Requester must own the Intent or have an explicitly authorized staff role.

### Opportunity / Match

Requester can only read opportunities returned to that user and fields permitted by match visibility rules.

### Group

Read requires active membership unless the endpoint explicitly exposes a discovery-level public projection.

Mutating group settings requires the group role defined by the domain model.

### Connection

Direct connection APIs require a currently valid connection relationship. One-sided private interest is not sufficient.

### Meetup

Read requires valid participant/group/connection authorization for the meetup context.

Mutations require both authorization and valid meetup state.

### MeetupPlan

Mutating a plan requires authorization as an eligible planning participant and a plan state that permits the mutation.

### ParticipantConfirmation

A user can create/update only their own confirmation record.

No user can write another participant's confirmation.

### Reservation

Reservation reads are filtered by participant authorization. Payment data is never returned through ordinary meetup endpoints.

### SafetyCase

Safety access is intentionally stricter than ordinary meetup access. Reporter and staff visibility are policy-controlled.

## 6. Canonical API style

Base path:

`/api/v1`

Authentication uses the platform's authenticated session/token mechanism. The exact identity provider is intentionally not fixed here.

Resource-oriented HTTP APIs are preferred. Domain transitions should be represented as explicit actions where a normal CRUD update would obscure invariants.

## 7. Identity / profile APIs

### GET `/api/v1/me`

Returns the authenticated user's safe profile projection.

### PATCH `/api/v1/me`

Updates fields the authenticated user owns.

Must not accept server-owned fields such as trust state, moderation state, or derived learning signals.

## 8. Intent APIs

### POST `/api/v1/intents`

Creates an Intent owned by the authenticated user.

Request contains explicit goal/preferences/constraints.

### GET `/api/v1/intents/:intentId`

Authorized owner read.

### PATCH `/api/v1/intents/:intentId`

Owner-only while the Intent is editable.

### POST `/api/v1/intents/:intentId/submit`

Transitions an editable Intent into the domain's submitted/active state after validation.

### POST `/api/v1/intents/:intentId/close`

Closes the user's Intent according to lifecycle rules.

## 9. Opportunity / match APIs

### GET `/api/v1/opportunities`

Returns opportunities authorized for the requester.

### GET `/api/v1/matches/:matchId`

Returns the requester's authorized match projection.

### POST `/api/v1/matches/:matchId/decision`

Records the requester's own decision.

Request example:

```json
{
  "decision": "CONTINUE"
}
```

Server evaluates whether mutuality is reached.

### GET `/api/v1/matches/:matchId/mutuality`

Returns only the mutuality state that the requester is authorized to know.

## 10. Group APIs

### POST `/api/v1/groups`

Creates a Group when domain eligibility permits.

### GET `/api/v1/groups/:groupId`

Member-authorized projection.

### PATCH `/api/v1/groups/:groupId`

Role-based group update.

### POST `/api/v1/groups/:groupId/leave`

Authenticated member leaves their own membership.

### GET `/api/v1/groups/:groupId/members`

Returns only member fields permitted by group privacy rules.

## 11. Connection APIs

### GET `/api/v1/connections/:connectionId`

Authorized connection participant projection.

### POST `/api/v1/connections/:connectionId/pause`

Pauses the requester's side according to connection rules.

### POST `/api/v1/connections/:connectionId/resume`

Resumes when the domain allows it.

### POST `/api/v1/connections/:connectionId/end`

Ends the requester's side according to lifecycle rules.

### POST `/api/v1/connections/:connectionId/block`

Creates/updates the requester's block relationship.

## 12. Meetup APIs

### POST `/api/v1/meetups`

Creates a Meetup aggregate only through an authorized planning flow.

This endpoint must not bypass matching, mutuality, participant eligibility, or planning invariants.

### GET `/api/v1/meetups/:meetupId`

Returns the authorized meetup projection.

### POST `/api/v1/meetups/:meetupId/cancel-participation`

Cancels only the authenticated participant's participation unless the domain transition makes the whole meetup cancelled.

### POST `/api/v1/meetups/:meetupId/leave`

Leaves a meetup where the lifecycle permits departure.

### POST `/api/v1/meetups/:meetupId/mark-on-way`

Creates/updates only the authenticated participant's operational signal.

### POST `/api/v1/meetups/:meetupId/mark-arrived`

Creates/updates only the authenticated participant's arrival signal.

## 13. Meetup plan APIs

### GET `/api/v1/meetups/:meetupId/plan`

Returns the current authorized plan version.

### POST `/api/v1/meetups/:meetupId/plan/versions`

Creates a candidate plan version. Server classifies material change impact.

### POST `/api/v1/meetups/:meetupId/plan/change-request`

Records a structured change request.

### POST `/api/v1/meetups/:meetupId/plan/versions/:versionId/review`

Records the authenticated participant's review/decision where eligible.

### GET `/api/v1/meetups/:meetupId/plan/changes`

Returns decision-relevant change history authorized for the requester.

## 14. Confirmation APIs

### GET `/api/v1/meetups/:meetupId/confirmation-status`

Returns aggregate confirmation readiness and the requester's own state.

It must not expose private individual hesitation by default.

### POST `/api/v1/meetups/:meetupId/confirm`

Records the authenticated participant's explicit confirmation against the current plan version.

Required server checks:

- requester is an eligible participant
- current plan version is still valid
- required fields are complete
- requester has not already confirmed this exact version
- material changes have not invalidated the review
- meetup has not transitioned to an incompatible state

### POST `/api/v1/meetups/:meetupId/reconfirm`

Explicit reconfirmation after a material change.

## 15. Reservation APIs

### GET `/api/v1/meetups/:meetupId/reservation`

Returns authorized reservation status and safe reference information.

### POST `/api/v1/meetups/:meetupId/reservation/prepare`

Prepares a reservation operation. Must not silently charge.

### POST `/api/v1/meetups/:meetupId/reservation/confirm`

Confirms a reservation after required user authorization and external verification.

### POST `/api/v1/meetups/:meetupId/reservation/cancel`

Cancels a reservation only where permitted by reservation and meetup rules.

Payment credentials are never accepted or returned through generic domain objects.

## 16. Post-meetup APIs

### POST `/api/v1/meetups/:meetupId/complete`

Completes the meetup only when the domain rules permit completion.

### POST `/api/v1/meetups/:meetupId/post-meetup/reflection`

Writes only the authenticated participant's private reflection.

### POST `/api/v1/meetups/:meetupId/post-meetup/feedback`

Writes private feedback owned by the authenticated participant.

### POST `/api/v1/meetups/:meetupId/post-meetup/continuation`

Records only the authenticated participant's continuation preference.

### GET `/api/v1/history/meetups`

Returns the user's authorized historical meetup projection.

## 17. Safety APIs

### POST `/api/v1/safety/reports`

Creates a SafetyCase for the authenticated reporter.

### GET `/api/v1/safety/cases/:caseId`

Returns only the subset the requester is entitled to receive. Staff processing uses a separate privileged boundary.

### POST `/api/v1/users/:userId/block`

Creates/updates the authenticated user's block relationship.

### DELETE `/api/v1/users/:userId/block`

Removes the authenticated user's block where allowed.

Safety reporting must remain possible after a meetup is completed or cancelled if policy permits.

## 18. AI APIs

### POST `/api/v1/ai/ask`

Request includes a user question and optional authorized context reference.

The service retrieves structured domain state first and applies field-level authorization before context reaches the model.

Example:

```json
{
  "question": "What changed in our meetup plan?",
  "context": {
    "type": "MEETUP",
    "id": "m_123"
  }
}
```

### POST `/api/v1/ai/proposals`

Generates a structured suggestion that remains uncommitted until a user explicitly applies it.

AI output must use a typed proposal format rather than directly writing domain records.

## 19. Plan Reliability APIs

### GET `/api/v1/meetups/:meetupId/reliability`

Returns the authorized current reliability evaluation for the current plan version.

Response should emphasize:

- risk level
- reasons
- unresolved checks
- available fallback options

Do not expose private participant constraints.

### POST `/api/v1/meetups/:meetupId/reliability/evaluate`

Requests a fresh deterministic evaluation when inputs changed or the previous evaluation is stale.

AI may explain the result but does not decide the risk level.

## 20. Error contract

All APIs should use a consistent error envelope.

Example:

```json
{
  "error": {
    "code": "PLAN_VERSION_STALE",
    "message": "The meetup plan changed while you were reviewing it.",
    "requestId": "req_123"
  }
}
```

Recommended categories:

- `UNAUTHENTICATED`
- `FORBIDDEN`
- `NOT_FOUND`
- `INVALID_STATE`
- `VALIDATION_ERROR`
- `PLAN_VERSION_STALE`
- `CONFIRMATION_STALE`
- `RESERVATION_UNAVAILABLE`
- `PAYMENT_REQUIRED`
- `CONFLICT`
- `RATE_LIMITED`
- `DEPENDENCY_UNAVAILABLE`
- `INTERNAL_ERROR`

Do not leak sensitive authorization details in error messages.

## 21. Idempotency

All consequential mutation endpoints should support idempotency keys where duplicate effects are possible.

Examples:

- confirm
- reconfirm
- reservation confirm
- reservation cancel
- safety report creation
- meetup cancellation
- plan version creation
- post-meetup feedback submission

Repeated requests with the same idempotency key must return the same logical outcome or a safe conflict.

## 22. Concurrency control

State-changing endpoints must validate the current version/state before commit.

Recommended request fields include:

```json
{
  "expectedPlanVersion": 4
}
```

If stale, return `PLAN_VERSION_STALE` or `CONFLICT` rather than silently overwriting newer data.

## 23. Source of truth

Server-authoritative structured state is always above:

1. Client state
2. Chat text
3. AI output

AI-generated content is advisory until explicitly applied through a domain service.

## 24. API response projections

Prefer purpose-specific safe projections:

- `UserSummary`
- `OpportunitySummary`
- `MatchSummary`
- `GroupSummary`
- `ConnectionSummary`
- `MeetupSummary`
- `MeetupPlanView`
- `ConfirmationStatusView`
- `ReservationView`
- `PostMeetupView`
- `ReliabilityView`
- `SafetyView`

Do not return database rows directly to clients.

## 25. Authorization middleware

Authentication identifies the requester.

Authorization services answer:

- Does this user own this object?
- Is the user a participant?
- Is the user a group member?
- Is the connection still active/eligible?
- Is this field visible to this requester?
- Does the current domain state allow the requested transition?

These checks must be reusable domain/application services.

## 26. Audit logging

Audit consequential actions such as:

- confirmation
- reconfirmation
- cancellation
- reservation changes
- payment authorization result
- SafetyCase creation/status changes
- block actions
- material plan changes
- staff moderation actions

Audit records must exclude secrets and unnecessary sensitive content.

## 27. Rate limiting and abuse controls

At minimum, rate-limit:

- authentication-sensitive endpoints
- AI endpoints
- opportunity/match queries
- message-adjacent proposal creation
- safety report creation where abuse controls are appropriate
- notification-triggering actions

Safety reporting must remain accessible while still protecting against automated abuse.

## 28. AI security boundary

The AI service receives only authorized context.

The model cannot:

- choose another user's private fields
- bypass authorization
- execute arbitrary endpoints
- write directly to persistence
- confirm another participant
- make payment decisions
- bypass safety controls

Consequential actions must return typed proposals to an application service.

## 29. Versioning strategy

API prefix:

`/api/v1`

Breaking changes should require a new API version rather than silently changing semantics.

Non-breaking additions should remain backward compatible.

## 30. Initial API implementation order

1. Authentication/session boundary
2. `/me`
3. Intent
4. Opportunity/Match
5. Group/Connection
6. Meetup/Plan
7. Confirmation
8. Reservation
9. Safety
10. Post-meetup learning
11. Plan Reliability
12. AI orchestration

## 31. Acceptance criteria

- Authorization is server-side and deny-by-default.
- Users can only mutate their own private decisions.
- Private participant state is never exposed by generic endpoints.
- Meetup confirmation is version-aware and idempotent.
- Reservation state is independent from participant confirmation.
- Material plan changes invalidate stale confirmation as defined by the state machine.
- Safety access is cross-cutting and policy-controlled.
- AI only receives authorized context and cannot directly mutate core state.
- API responses use safe projections rather than raw database rows.
- Consequential actions are auditable.
- Concurrency conflicts are explicit.
- API errors are consistent and do not leak sensitive information.

## Product/architecture principle

**The client may request an action; only the server can authorize and commit it.**

This keeps Pyrintu's most important properties—mutuality, trust, safety, plan reliability, and privacy—inside enforceable domain rules rather than UI assumptions.
