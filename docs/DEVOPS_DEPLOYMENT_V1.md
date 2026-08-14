# PYRINTU — DEVELOPMENT / DEVOPS / DEPLOYMENT v1.0

**Status:** Architecture checkpoint

## 1. Purpose

Define the engineering workflow, environments, CI/CD, configuration, secrets, migrations, deployment, rollback, and release controls required to move Pyrintu from architecture into implementation.

This document does not prescribe a single cloud vendor. Provider-specific choices can be made during implementation without changing product semantics.

## 2. Environments

Use three primary environments:

- **Local** — developer machines; safe test integrations and seeded data.
- **Staging** — production-like environment for integration, E2E, AI evaluation, migrations, and release candidate validation.
- **Production** — live user traffic and production data.

Optional preview environments may be created per pull request when the frontend/deployment platform supports them.

Never use real production user data in local or staging environments.

## 3. Repository workflow

Canonical workflow:

```text
main
  ↓
feature/<scope>
  ↓
commit + tests
  ↓
Pull Request
  ↓
review / approval
  ↓
merge to main
  ↓
staging deployment
  ↓
release verification
  ↓
production deployment
```

Direct pushes to `main` should be disabled once implementation begins unless required for emergency repository administration.

## 4. Branch conventions

Examples:

- `feature/meetup-planning`
- `fix/stale-plan-confirmation`
- `security/authorization-boundary`
- `chore/dependency-update`
- `docs/architecture-update`

Keep branches short-lived and scoped to one logical change.

## 5. Pull request gates

Every implementation PR should normally include:

- tests relevant to changed behavior
- migration notes when persistence changes
- API contract changes when applicable
- security/privacy impact when applicable
- screenshots or recordings for user-facing changes
- rollback considerations for risky changes

The PR must not merge when required CI checks fail.

## 6. CI pipeline

Recommended pipeline stages:

```text
Checkout
  ↓
Dependency restore
  ↓
Formatting / lint
  ↓
Type checks
  ↓
Unit tests
  ↓
Domain transition tests
  ↓
API contract tests
  ↓
Security / dependency scan
  ↓
Build
  ↓
Migration validation
  ↓
Artifact creation
```

Additional staging-only gates:

- integration tests
- E2E critical flows
- AI evaluation suite
- reliability-engine regression tests

## 7. Backend deployment

Start with a containerized backend and worker.

```text
Backend container
Worker container
        ↓
Managed database
Queue / cache
External providers
```

The backend and worker share application code where appropriate but have separate process responsibilities.

## 8. Frontend deployment

Frontend should be independently deployable from the backend.

Build pipeline:

```text
Source
 ↓
Install
 ↓
Lint / typecheck / tests
 ↓
Production build
 ↓
Static/app hosting
```

Frontend runtime configuration must contain only public configuration. No private provider credentials belong in browser-exposed environment variables.

## 9. Database migrations

All schema changes must be migration-based.

Rules:

- migrations are versioned
- migrations run automatically only in controlled deployment stages
- production migration execution must be observable
- destructive migrations require explicit rollout planning
- application and migration compatibility must be considered for rolling deployments

Prefer expand → migrate/backfill → contract rather than destructive one-step schema changes.

## 10. Configuration

Separate configuration categories:

### Public configuration

Examples:

- frontend API base URL
- feature identifiers safe for clients
- public map identifiers where required

### Server configuration

Examples:

- database URL
- queue connection
- provider credentials
- authentication secrets
- encryption keys
- payment configuration
- AI provider credentials

Server secrets must never be committed to Git.

## 11. Secret management

Use environment-level secret management provided by the deployment platform or dedicated secret manager.

Rules:

- no secrets in source control
- no secrets in client bundles
- no secrets in logs
- rotate credentials periodically and after suspected exposure
- use least-privilege provider credentials
- separate staging and production credentials

## 12. Authentication configuration

Authentication provider configuration must be environment-specific.

Local and staging may use test identities or sandbox providers.

Production uses production identity configuration.

Session/token validation remains server-side according to the authorization architecture.

## 13. External providers

Providers remain behind adapters:

```text
MapProvider
VenueProvider
ReservationProvider
PaymentProvider
NotificationProvider
AIProvider
```

Provider credentials and endpoints are environment-specific.

External sandbox/test credentials must never be reused accidentally in production.

## 14. Queue / background jobs

Background jobs should have:

- durable job identity
- retry policy
- backoff
- dead-letter handling where appropriate
- idempotent handlers
- observable success/failure state

High-risk jobs such as reservation or payment reconciliation require especially strong idempotency and reconciliation behavior.

## 15. Deployment order

For a normal production release:

```text
1. CI green
2. Build immutable artifacts
3. Validate migrations
4. Apply compatible database migration
5. Deploy backend
6. Deploy worker
7. Deploy frontend
8. Run smoke tests
9. Verify critical metrics
10. Declare release healthy
```

For schema changes that require backwards compatibility, deploy in multiple phases rather than breaking old code immediately.

## 16. Rollback

Application rollback should be possible by redeploying the previous known-good artifact.

Database rollback should not rely on blindly reversing migrations in production. Prefer forward-compatible repair migrations when data has already been transformed.

For risky releases:

- record previous artifact version
- record migration version
- define rollback trigger
- define owner for the rollback decision

## 17. Feature flags

Use feature flags for risky or staged capabilities such as:

- Plan Reliability Engine
- AI-assisted proposals
- new recommendation logic
- new reservation provider
- experimental onboarding

Feature flags must be server-governed for security-sensitive functionality.

Do not use client-only flags to bypass authorization or safety checks.

## 18. Observability

Collect:

- structured logs
- request metrics
- latency metrics
- queue metrics
- database metrics
- external-provider metrics
- deployment health
- AI latency/error metrics
- safety workflow metrics

Never log:

- passwords
- authentication tokens
- payment credentials
- private safety report contents
- hidden participant data
- unrestricted model context

## 19. Health checks

Backend should expose separate concepts where useful:

- liveness — process is running
- readiness — dependencies required for serving are available

External optional dependencies should not necessarily make the whole service appear dead.

Workers should expose observable job-processing health.

## 20. Backups / recovery

Production database must have:

- automated backups
- tested restore procedure
- defined retention policy
- recovery point objective (RPO)
- recovery time objective (RTO)

Do not claim a backup strategy is complete until restore has been tested.

## 21. Data retention

Retention must be defined separately for:

- account data
- meetup history
- private feedback
- safety cases
- audit events
- analytics
- logs

Do not retain sensitive data indefinitely by default.

## 22. Staging data policy

Use synthetic or anonymized data.

Seed data should exercise:

- users
- matches
- groups
- connections
- meetup versions
- confirmation changes
- reservation failures
- safety flows
- reliability failures
- AI uncertainty cases

## 23. AI-specific deployment controls

AI provider configuration must be isolated by environment.

Staging may use separate models/providers for evaluation.

AI changes require regression evaluation before production rollout.

Prompt templates, tool definitions, and policy configuration are versioned artifacts.

## 24. Reliability Engine deployment controls

Reliability rules are versioned with the application.

Changes to risk classification or fallback logic require:

- deterministic test cases
- regression comparison
- explicit release notes

Do not silently change the meaning of historical reliability evaluations.

## 25. Security release gates

A production release should block on:

- known critical dependency vulnerabilities unless explicitly accepted through security process
- failed authorization tests
- failed privacy projection tests
- failed migration validation
- failed critical E2E flows
- leaked secrets detected by scanning

## 26. Incident response

The production process must define:

- incident owner
- severity levels
- communication path
- rollback/mitigation procedure
- evidence preservation
- post-incident review

Safety incidents require the stricter safety escalation path defined by product policy.

## 27. Repository protection

Once implementation starts:

- protect `main`
- require PR reviews as appropriate
- require required status checks
- restrict force pushes
- restrict branch deletion where needed
- keep production secrets outside Git

## 28. Local developer bootstrap

The eventual repository should provide a documented bootstrap path such as:

```text
clone
→ install dependencies
→ configure .env.example
→ start local database/cache
→ run migrations
→ seed development data
→ start backend
→ start worker
→ start frontend
```

Exact commands belong in implementation documentation once the technology stack is finalized.

## 29. Release definition of done

A feature is release-ready when:

- product behavior matches the approved domain/UX contract
- tests pass
- security/privacy checks pass
- migrations are reviewed
- observability is present
- rollback impact is understood
- staging validation succeeds
- required documentation is updated

## 30. Architecture acceptance criteria

- development, staging, and production are isolated
- CI is mandatory before merge
- migrations are versioned
- secrets are never committed or browser-exposed
- deployments use immutable artifacts where practical
- rollback is documented
- backups and restore are testable
- AI and reliability changes have dedicated evaluation gates
- production `main` is protected
- the deployment architecture supports the modular monolith without forcing premature microservices
