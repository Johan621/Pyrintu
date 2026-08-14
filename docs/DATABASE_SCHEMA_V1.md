# PYRINTU — DATABASE SCHEMA v1.0

**Status:** Architecture checkpoint

## Purpose

Define the persistence model for the approved Pyrintu domain and state-transition architecture without tying the product to a framework-specific ORM.

This document defines entities, keys, relationships, invariants, indexes, privacy boundaries, and persistence rules. It does not prescribe a database vendor or migration framework.

## 1. Persistence principles

- Structured domain state is the source of truth.
- Screen-specific UI state is never persisted as business truth.
- Historical facts are append-only where practical; corrections use explicit domain events/versioning.
- Material plan changes create a new `meetup_plan_versions` row rather than overwriting history.
- Participant decisions are scoped to a specific plan version.
- Sensitive data is separated or access-controlled at the persistence boundary.
- Derived AI/recommendation signals never overwrite source facts.
- Idempotency keys are persisted for consequential mutations.
- Timestamps are stored in UTC.

## 2. Core identity tables

### `users`

- `id` UUID PK
- `email` nullable, unique when present
- `phone` nullable, unique when present
- `status`
- `created_at`
- `updated_at`

### `user_profiles`

- `user_id` UUID PK/FK → `users.id`
- `display_name`
- `bio` nullable
- `avatar_url` nullable
- `profile_visibility`
- `created_at`
- `updated_at`

Keep profile presentation separate from authentication identity.

### `user_preferences`

- `user_id` UUID PK/FK → `users.id`
- `preferences_json` or normalized preference tables as implementation requires
- `privacy_settings_json`
- `notification_settings_json`
- `updated_at`

Sensitive preference fields must follow field-level authorization.

## 3. Intent / discovery tables

### `intents`

- `id` UUID PK
- `owner_user_id` UUID FK → `users.id`
- `status`
- `goal_type`
- `raw_input` nullable
- `normalized_goal_json`
- `constraints_json`
- `availability_json`
- `created_at`
- `updated_at`
- `closed_at` nullable

Invariant: only the owner can edit an editable intent.

### `opportunities`

- `id` UUID PK
- `user_id` UUID FK → `users.id`
- `intent_id` UUID FK → `intents.id`
- `candidate_type`
- `candidate_id`
- `visibility_state`
- `evidence_json`
- `created_at`
- `expires_at` nullable

The database should not persist hidden recommendation reasoning that a user is not authorized to receive.

### `matches`

- `id` UUID PK
- `intent_id` UUID FK → `intents.id`
- `status`
- `created_at`
- `updated_at`

### `match_participants`

- `match_id` UUID FK → `matches.id`
- `user_id` UUID FK → `users.id`
- `decision` nullable
- `decided_at` nullable
- `mutuality_reveal_state`
- PK (`match_id`, `user_id`)

Users may write only their own decision row.

## 4. Group / connection tables

### `groups`

- `id` UUID PK
- `status`
- `created_by_user_id` UUID FK → `users.id`
- `purpose_json`
- `created_at`
- `updated_at`

### `group_members`

- `group_id` UUID FK → `groups.id`
- `user_id` UUID FK → `users.id`
- `role`
- `status`
- `joined_at`
- `left_at` nullable
- PK (`group_id`, `user_id`)

### `connections`

- `id` UUID PK
- `status`
- `created_at`
- `updated_at`
- `ended_at` nullable

### `connection_participants`

- `connection_id` UUID FK → `connections.id`
- `user_id` UUID FK → `users.id`
- `participant_state`
- `joined_at`
- `left_at` nullable
- PK (`connection_id`, `user_id`)

### `connection_preferences`

- `connection_id` UUID FK → `connections.id`
- `user_id` UUID FK → `users.id`
- `preference` (`YES`, `MAYBE`, `NO`, `SKIPPED`)
- `created_at`
- `updated_at`
- PK (`connection_id`, `user_id`)

One-sided continuation preference must not be treated as mutuality.

## 5. Activity / meetup tables

### `activities`

- `id` UUID PK
- `name`
- `category`
- `description` nullable
- `metadata_json`
- `status`
- `created_at`
- `updated_at`

### `meetups`

- `id` UUID PK
- `status`
- `created_by_user_id` UUID FK → `users.id`
- `connection_id` UUID FK → `connections.id` nullable
- `group_id` UUID FK → `groups.id` nullable
- `activity_id` UUID FK → `activities.id`
- `current_plan_version_id` UUID nullable FK → `meetup_plan_versions.id` (added after table creation or via deferred constraint)
- `operational_state`
- `created_at`
- `updated_at`
- `started_at` nullable
- `completed_at` nullable
- `cancelled_at` nullable

Invariant: a meetup must have exactly one valid participant context according to domain rules; DB-level checks should prevent impossible combinations where feasible.

### `meetup_participants`

- `meetup_id` UUID FK → `meetups.id`
- `user_id` UUID FK → `users.id`
- `role`
- `status`
- `joined_at`
- `left_at` nullable
- `on_way_at` nullable
- `arrived_at` nullable
- PK (`meetup_id`, `user_id`)

Operational signals are self-authored; no participant may write another participant's arrival state.

## 6. Meetup planning and versioning

### `meetup_plans`

- `id` UUID PK
- `meetup_id` UUID UNIQUE FK → `meetups.id`
- `current_version_id` UUID nullable FK → `meetup_plan_versions.id`
- `status`
- `created_at`
- `updated_at`

### `meetup_plan_versions`

- `id` UUID PK
- `meetup_plan_id` UUID FK → `meetup_plans.id`
- `version_number` integer
- `created_by_user_id` UUID FK → `users.id`
- `activity_id` UUID FK → `activities.id`
- `start_at` nullable
- `end_at` nullable
- `venue_id` UUID nullable FK → `venues.id`
- `area_text` nullable
- `duration_minutes` nullable
- `cost_state`
- `estimated_cost_minor` nullable
- `currency` nullable
- `logistics_json`
- `accessibility_json`
- `change_classification` (`INITIAL`, `MINOR`, `MATERIAL`)
- `review_state`
- `created_at`

Unique constraint: (`meetup_plan_id`, `version_number`).

The current version is immutable after creation. A material change creates a new version.

### `meetup_plan_reviews`

- `plan_version_id` UUID FK → `meetup_plan_versions.id`
- `user_id` UUID FK → `users.id`
- `decision`
- `note` nullable
- `created_at`
- `updated_at`
- PK (`plan_version_id`, `user_id`)

## 7. Venue / reservation tables

### `venues`

- `id` UUID PK
- `name`
- `address_text`
- `area_text` nullable
- `latitude` nullable
- `longitude` nullable
- `verification_state`
- `metadata_json`
- `created_at`
- `updated_at`

Exact participant home locations must never be stored in meetup venue fields.

### `reservations`

- `id` UUID PK
- `meetup_id` UUID FK → `meetups.id`
- `venue_id` UUID FK → `venues.id`
- `status`
- `external_reference` nullable
- `amount_minor` nullable
- `currency` nullable
- `expires_at` nullable
- `created_at`
- `updated_at`

Reservation status is independent from meetup confirmation.

## 8. Participant confirmations

### `participant_confirmations`

- `id` UUID PK
- `meetup_id` UUID FK → `meetups.id`
- `user_id` UUID FK → `users.id`
- `plan_version_id` UUID FK → `meetup_plan_versions.id`
- `decision`
- `confirmed_at` nullable
- `invalidated_at` nullable
- `created_at`
- `updated_at`

Unique active confirmation constraint should prevent two active confirmations for the same (`meetup_id`, `user_id`, `plan_version_id`).

A participant cannot confirm another participant.

## 9. Change requests / operational history

### `meetup_change_requests`

- `id` UUID PK
- `meetup_id` UUID FK → `meetups.id`
- `requested_by_user_id` UUID FK → `users.id`
- `base_plan_version_id` UUID FK → `meetup_plan_versions.id`
- `proposed_plan_version_id` UUID nullable FK → `meetup_plan_versions.id`
- `change_type`
- `reason_text` nullable
- `status`
- `created_at`
- `resolved_at` nullable

This table records intent to change; it is not itself the source of truth for the current plan.

## 10. Conversation / notification tables

### `conversations`

- `id` UUID PK
- `context_type`
- `context_id`
- `status`
- `created_at`
- `updated_at`

### `conversation_members`

- `conversation_id` UUID FK → `conversations.id`
- `user_id` UUID FK → `users.id`
- `joined_at`
- `left_at` nullable
- PK (`conversation_id`, `user_id`)

### `messages`

- `id` UUID PK
- `conversation_id` UUID FK → `conversations.id`
- `sender_user_id` UUID FK → `users.id`
- `body` or encrypted content reference
- `created_at`
- `edited_at` nullable
- `deleted_at` nullable

Messages are conversation data, not structured meetup truth.

### `notifications`

- `id` UUID PK
- `recipient_user_id` UUID FK → `users.id`
- `type`
- `entity_type`
- `entity_id`
- `payload_json`
- `read_at` nullable
- `created_at`

## 11. Post-meetup learning

### `post_meetup_outcomes`

- `id` UUID PK
- `meetup_id` UUID FK → `meetups.id`
- `user_id` UUID FK → `users.id`
- `reflection_state` nullable
- `activity_feedback` nullable
- `venue_feedback` nullable
- `planning_feedback` nullable
- `overall_feedback` nullable
- `safety_signal` nullable
- `continuation_preference` nullable
- `created_at`
- `updated_at`

Unique constraint: (`meetup_id`, `user_id`).

Private feedback is never returned through shared participant projections.

### `user_learning_signals`

- `id` UUID PK
- `user_id` UUID FK → `users.id`
- `signal_type`
- `value_json`
- `confidence` nullable
- `source_meetup_id` UUID nullable FK → `meetups.id`
- `source_outcome_id` UUID nullable FK → `post_meetup_outcomes.id`
- `created_at`
- `expires_at` nullable

Derived signals must remain traceable to authorized source data.

## 12. Plan Reliability Engine

### `plan_reliability_evaluations`

- `id` UUID PK
- `meetup_plan_version_id` UUID FK → `meetup_plan_versions.id`
- `risk_level`
- `availability_check_state`
- `venue_check_state`
- `cost_check_state`
- `participant_constraint_state`
- `logistics_check_state`
- `fallback_count`
- `reasons_json`
- `evaluated_at`
- `expires_at` nullable

The risk decision is deterministic and explainable. AI can explain it but cannot write the risk result as an authority.

### `plan_reliability_fallbacks`

- `id` UUID PK
- `evaluation_id` UUID FK → `plan_reliability_evaluations.id`
- `rank` integer
- `plan_snapshot_json`
- `reason_json`
- `created_at`

Fallback snapshots are recommendations, not confirmed plans.

## 13. Safety tables

### `safety_cases`

- `id` UUID PK
- `reporter_user_id` UUID FK → `users.id`
- `context_type`
- `context_id`
- `category`
- `severity`
- `status`
- `description_encrypted` or secure content reference
- `created_at`
- `updated_at`
- `closed_at` nullable

Safety data requires stricter access controls than normal meetup data.

### `user_blocks`

- `user_id` UUID FK → `users.id`
- `blocked_user_id` UUID FK → `users.id`
- `created_at`
- PK (`user_id`, `blocked_user_id`)

A block must be enforced before normal social projections are returned.

## 14. Idempotency / audit tables

### `idempotency_keys`

- `id` UUID PK
- `user_id` UUID FK → `users.id`
- `key` text
- `operation` text
- `request_hash` text
- `response_status` integer nullable
- `response_body_json` nullable
- `created_at`
- `expires_at`

Unique constraint: (`user_id`, `key`, `operation`).

### `domain_events`

- `id` UUID PK
- `aggregate_type`
- `aggregate_id`
- `event_type`
- `event_version`
- `actor_user_id` nullable FK → `users.id`
- `payload_json`
- `created_at`

Use for auditability and asynchronous projections where necessary. Do not treat arbitrary client-generated events as authoritative state changes.

## 15. Important indexes

Recommended initial indexes:

- `intents(owner_user_id, status)`
- `opportunities(user_id, created_at)`
- `match_participants(user_id, match_id)`
- `group_members(user_id, status)`
- `connection_participants(user_id, participant_state)`
- `meetup_participants(user_id, status)`
- `meetups(status, updated_at)`
- `meetup_plans(meetup_id)`
- `meetup_plan_versions(meetup_plan_id, version_number DESC)`
- `participant_confirmations(meetup_id, user_id, plan_version_id)`
- `reservations(meetup_id, status)`
- `post_meetup_outcomes(user_id, created_at DESC)`
- `user_learning_signals(user_id, signal_type, created_at DESC)`
- `plan_reliability_evaluations(meetup_plan_version_id, evaluated_at DESC)`
- `safety_cases(reporter_user_id, created_at DESC)`
- `notifications(recipient_user_id, read_at, created_at DESC)`
- `domain_events(aggregate_type, aggregate_id, created_at DESC)`

## 16. Foreign key / deletion policy

Prefer soft deletion or state transitions for domain records that affect historical truth.

Examples:

- Do not hard-delete completed meetups as routine product cleanup.
- Do not hard-delete participant confirmations that are part of audit history.
- Do not hard-delete safety cases through normal user APIs.
- User account deletion should follow a separate privacy/retention policy that preserves only legally/operationally required records.

## 17. Transaction boundaries

The database transaction must cover the state changes that need atomicity.

Examples:

### Confirmation

Validate current plan version → create/update participant confirmation → re-evaluate confirmation readiness → transition meetup if eligible.

### Material plan change

Create new plan version → invalidate affected stale confirmations → update current plan pointer → enqueue reliability reevaluation.

### Reservation confirmation

Validate authorization → confirm external reservation result → persist reservation state → update operational readiness.

### Meetup cancellation

Validate actor/state → transition meetup → update reservation when applicable → create notification/domain event.

## 18. Concurrency

Use optimistic concurrency/version checks for plan and meetup writes.

A request carrying stale `plan_version_id` or `updated_at` must fail with a conflict/stale-state error rather than overwrite newer state.

## 19. Privacy / security persistence boundary

Sensitive values should be isolated from standard projections.

At minimum protect:

- private feedback
- safety descriptions/evidence
- payment data or payment tokens
- hidden availability
- exact private locations
- internal recommendation features
- AI context that includes private fields

Encryption-at-rest and secret management are implementation responsibilities, but the schema must make sensitive data identifiable and access-controlled.

## 20. Database truth vs derived data

Authoritative:

- meetup status
- plan versions
- participant confirmations
- reservation status
- membership state
- safety case state

Derived/cacheable:

- recommendation evidence
- plan reliability evaluations
- user learning signals
- notification delivery state
- AI summaries

Derived data may be recomputed from authorized source facts.

## 21. Migration order

Implement migrations in dependency order:

1. users / profiles / preferences
2. intents / opportunities / matches
3. groups / connections
4. activities / venues
5. meetups / participants
6. plans / plan versions / reviews
7. confirmations / reservations
8. conversations / messages / notifications
9. post-meetup outcomes / learning signals
10. reliability evaluations / fallbacks
11. safety / blocks
12. idempotency / domain events

## 22. Acceptance criteria

- All approved domain entities have persistence representations.
- Plan versioning is first-class.
- Participant confirmation is scoped to a plan version.
- Reservation state is independent from meetup confirmation.
- Historical meetup facts remain stable.
- Private feedback and safety data are isolated.
- Reliability outputs are derived, explainable, and non-authoritative.
- Idempotency and optimistic concurrency have persistence support.
- Foreign keys and indexes cover the main authorization/query paths.
- No screen-specific business state is introduced into the schema.
- The schema can support the approved API and state-transition contracts without hidden fields.

## Product / engineering principle

**The database stores canonical domain truth; views, recommendations, AI summaries, and reliability evaluations are projections around that truth, not replacements for it.**
