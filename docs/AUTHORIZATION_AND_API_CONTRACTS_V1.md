# PYRINTU — AUTHORIZATION MATRIX + API CONTRACTS v1.0

**Status:** Architecture checkpoint

## Purpose
Define authorization rules and the first canonical API contract surface from the approved UX/state-machine, domain-model, and transition specifications. No database schema or framework-specific implementation is fixed here.

## Principles
- Deny by default.
- Server state, not UI state, is authoritative for authorization.
- Ownership, membership, relationship state, object state, and field visibility are enforced server-side.
- Safety access is cross-cutting.
- AI has no independent authority for consequential actions.

## Roles
- **User:** authenticated account.
- **Participant:** user attached to an Intent, Match, Group, Connection, or Meetup.
- **Group member:** active Group participant.
- **Connection participant:** user on one side of an established Connection.
- **Staff / safety operator:** privileged, audited moderation role.
- **System service:** trusted backend service operating through explicit invariants.

## Authorization matrix

| Capability | Owner / requester | Participant / member | Connection participant | Staff |
|---|---|---|---|---|
| Read/update own profile | Allow | Allow | Allow | Policy-controlled |
| Create/read/edit own Intent | Allow while editable | N/A | N/A | Policy-controlled |
| View Opportunity / Match | Returned-to-user scope | Eligible participant scope | N/A | Policy-controlled |
| Record own Match decision | Allow | Allow | N/A | No normal override |
| Read mutuality | Own authorized projection | Own authorized projection | Per mutuality rules | Policy-controlled |
| Read Group | N/A | Active members | N/A | Policy-controlled |
| Update Group | Authorized group role | Authorized role | N/A | Policy-controlled |
| Leave Group | Own membership | Own membership | N/A | Policy-controlled |
| Create/edit MeetupPlan | Eligible planning participant | Eligible planning participant | Eligible connection participant | Policy-controlled |
| Review plan | Own decision | Own decision | Own decision | Policy-controlled |
| Confirm/reconfirm | Own confirmation only | Own confirmation only | Own confirmation only | No normal-user override |
| Read another participant's private confirmation | Deny | Deny | Deny | Policy-controlled |
| Read aggregate readiness | Authorized meetup participant | Authorized meetup participant | Authorized meetup participant | Policy-controlled |
| Reservation read | Authorized participant; filtered | Same | Same | Policy-controlled |
| Payment authorization | Paying user only | Paying user only | Paying user only | No normal-user override |
| Propose plan change | Authorized participant | Authorized participant | Authorized participant | Policy-controlled |
| Cancel own participation | Own participant record | Own participant record | Own participant record | Policy-controlled |
| Read Meetup / day-of | Authorized participant/context | Authorized participant/context | Authorized connection context | Policy-controlled |
| Mark self on-way/arrived | Own signal only | Own signal only | Own signal only | No normal override |
| Report SafetyCase | Eligible reporter | Eligible reporter | Eligible reporter | Staff can process |
| Read SafetyCase | Own limited status only | Own limited status only | Own limited status only | Authorized safety staff |
| Block user | Own block list | Own block list | Own block list | Policy-controlled |
| End/pause Connection | Own side only | N/A | Own side only | Policy-controlled |
| Read own history | Allow | Allow for own records | Shared fields only | Policy-controlled |
| Submit post-meetup feedback | Own feedback only | Own feedback only | Own feedback only | No normal override |
| Read another user's private feedback | Deny | Deny | Deny | Policy-controlled |
| Ask AI | Authorized user | Authorized user | Authorized user | Policy-controlled |
| Ask AI to execute consequential action | Not directly allowed | Not directly allowed | Not directly allowed | Explicit service workflow only |

## Field-level privacy

Never expose by default: exact home address, exact private location, hidden availability, private intent notes, private participant hesitation, private safety report contents, payment credentials, private feedback text, or internal risk/recommendation features.

Shared fields should be modeled as deliberate safe projections.

## Domain authorization rules

- **Intent:** owner or explicit staff role.
- **Opportunity/Match:** requester-scoped and visibility-filtered.
- **Group:** membership required unless a public discovery projection is explicitly defined.
- **Connection:** valid connection state required for direct connection APIs.
- **Meetup:** participant/context authorization plus valid meetup state.
- **MeetupPlan:** eligible planning participation plus mutable plan state.
- **ParticipantConfirmation:** self-only writes.
- **Reservation:** participant-scoped reads; payment credentials excluded.
- **SafetyCase:** stricter policy than ordinary meetup access.

## Canonical API

Base path: `/api/v1`

Use resource-oriented HTTP with explicit domain actions where CRUD would hide invariants. Identity-provider choice remains intentionally unspecified.

### Identity
- `GET /api/v1/me`
- `PATCH /api/v1/me`

### Intent
- `POST /api/v1/intents`
- `GET /api/v1/intents/:intentId`
- `PATCH /api/v1/intents/:intentId`
- `POST /api/v1/intents/:intentId/submit`
- `POST /api/v1/intents/:intentId/close`

### Opportunity / Match
- `GET /api/v1/opportunities`
- `GET /api/v1/matches/:matchId`
- `POST /api/v1/matches/:matchId/decision`
- `GET /api/v1/matches/:matchId/mutuality`

### Group
- `POST /api/v1/groups`
- `GET /api/v1/groups/:groupId`
- `PATCH /api/v1/groups/:groupId`
- `POST /api/v1/groups/:groupId/leave`
- `GET /api/v1/groups/:groupId/members`

### Connection
- `GET /api/v1/connections/:connectionId`
- `POST /api/v1/connections/:connectionId/pause`
- `POST /api/v1/connections/:connectionId/resume`
- `POST /api/v1/connections/:connectionId/end`
- `POST /api/v1/connections/:connectionId/block`

### Meetup
- `POST /api/v1/meetups`
- `GET /api/v1/meetups/:meetupId`
- `POST /api/v1/meetups/:meetupId/cancel-participation`
- `POST /api/v1/meetups/:meetupId/leave`
- `POST /api/v1/meetups/:meetupId/mark-on-way`
- `POST /api/v1/meetups/:meetupId/mark-arrived`

### MeetupPlan
- `GET /api/v1/meetups/:meetupId/plan`
- `POST /api/v1/meetups/:meetupId/plan/versions`
- `POST /api/v1/meetups/:meetupId/plan/change-request`
- `POST /api/v1/meetups/:meetupId/plan/versions/:versionId/review`
- `GET /api/v1/meetups/:meetupId/plan/changes`

### Confirmation
- `GET /api/v1/meetups/:meetupId/confirmation-status`
- `POST /api/v1/meetups/:meetupId/confirm`
- `POST /api/v1/meetups/:meetupId/reconfirm`

`confirm` must verify eligibility, current plan version, required fields, compatible meetup state, and no stale material change.

### Reservation / payment
- `GET /api/v1/meetups/:meetupId/reservation`
- `POST /api/v1/meetups/:meetupId/reservation/prepare`
- `POST /api/v1/meetups/:meetupId/reservation/confirm`
- `POST /api/v1/meetups/:meetupId/reservation/cancel`

Payment credentials are never returned through generic domain objects.

### Post-meetup
- `POST /api/v1/meetups/:meetupId/complete`
- `POST /api/v1/meetups/:meetupId/post-meetup/reflection`
- `POST /api/v1/meetups/:meetupId/post-meetup/feedback`
- `POST /api/v1/meetups/:meetupId/post-meetup/continuation`
- `GET /api/v1/history/meetups`

### Safety
- `POST /api/v1/safety/reports`
- `GET /api/v1/safety/cases/:caseId`
- `POST /api/v1/users/:userId/block`
- `DELETE /api/v1/users/:userId/block`

### AI
- `POST /api/v1/ai/ask`
- `POST /api/v1/ai/proposals`

AI receives only authorized structured context and cannot directly write core state.

### Plan Reliability
- `GET /api/v1/meetups/:meetupId/reliability`
- `POST /api/v1/meetups/:meetupId/reliability/evaluate`

Return risk level, reasons, unresolved checks, and fallbacks without private participant constraints. AI may explain but does not determine the risk level.

## Error contract

```json
{"error":{"code":"PLAN_VERSION_STALE","message":"The meetup plan changed while you were reviewing it.","requestId":"req_123"}}
```

Recommended codes: `UNAUTHENTICATED`, `FORBIDDEN`, `NOT_FOUND`, `INVALID_STATE`, `VALIDATION_ERROR`, `PLAN_VERSION_STALE`, `CONFIRMATION_STALE`, `RESERVATION_UNAVAILABLE`, `PAYMENT_REQUIRED`, `CONFLICT`, `RATE_LIMITED`, `DEPENDENCY_UNAVAILABLE`, `INTERNAL_ERROR`.

Do not leak sensitive authorization details.

## Idempotency

Consequential mutation endpoints should support idempotency keys: confirmation, reconfirmation, reservation confirmation/cancellation, safety report creation, meetup cancellation, plan-version creation, and post-meetup feedback.

Repeated requests using the same key must produce one logical outcome or a safe conflict.

## Concurrency

State-changing APIs validate current version/state before commit. Optimistic concurrency can use:

```json
{"expectedPlanVersion":4}
```

Stale requests return `PLAN_VERSION_STALE` or `CONFLICT` instead of silently overwriting newer state.

## Source of truth

Server-authoritative structured state outranks client state, chat text, and AI output. AI suggestions become domain state only through explicit user action and domain validation.

## Response projections

Use safe projections such as `UserSummary`, `OpportunitySummary`, `MatchSummary`, `GroupSummary`, `ConnectionSummary`, `MeetupSummary`, `MeetupPlanView`, `ConfirmationStatusView`, `ReservationView`, `PostMeetupView`, `ReliabilityView`, and `SafetyView`. Never return raw database rows.

## Authorization middleware

Reusable services must evaluate ownership, participant/member state, connection eligibility, field visibility, and transition eligibility. UI visibility is never an authorization mechanism.

## Audit logging

Audit confirmations, reconfirmations, cancellations, reservation changes, payment authorization results, SafetyCase changes, blocks, material plan changes, and staff moderation actions. Exclude secrets and unnecessary sensitive content.

## Rate limiting and abuse controls

Rate-limit authentication-sensitive endpoints, AI calls, opportunity/match queries, notification-triggering proposal creation, and safety reporting as appropriate. Safety reporting remains accessible while automated abuse is controlled.

## AI security boundary

AI cannot bypass authorization, execute arbitrary endpoints, write directly to persistence, confirm another participant, make payment decisions, or bypass safety controls. Consequential AI behavior returns typed proposals to an application service.

## Versioning

API prefix is `/api/v1`. Breaking semantic changes require a new API version; non-breaking additions remain backward compatible.

## Initial implementation order

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

## Acceptance criteria

- Server-side deny-by-default authorization.
- Users mutate only their own private decisions.
- Private participant state is protected.
- Confirmation is version-aware and idempotent.
- Reservation state is independent from participant confirmation.
- Material plan changes invalidate stale confirmation as defined by the state machine.
- Safety access is cross-cutting and policy-controlled.
- AI receives authorized context only and cannot directly mutate core state.
- API responses use safe projections.
- Consequential actions are auditable.
- Concurrency conflicts are explicit.
- Errors are consistent and do not leak sensitive information.

## Product / architecture principle

**The client may request an action; only the server can authorize and commit it.**
