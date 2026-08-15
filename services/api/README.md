# Pyrintu API Service

First application-facing API slice for Intent creation.

## Scope

- FastAPI route surface under `/api/v1`.
- Owner-scoped Intent creation/read/submit.
- SQLAlchemy persistence boundary using `DATABASE_URL`.
- SQLite is supported for local development/tests; PostgreSQL is the intended deployed database.
- Domain service remains the business-rule authority.
- Bearer JWT verification is the production authentication boundary.
- Development mode can use `X-User-ID` only when `PYRINTU_AUTH_MODE=development`.

## Local setup

```bash
python -m venv .venv
pip install -e .[test]
alembic upgrade head
pytest
uvicorn pyrintu_api.main:app --reload
```

### Authentication

Production mode expects:

```text
Authorization: Bearer <JWT>
```

Required environment:

```text
PYRINTU_JWT_SECRET
```

Optional validation:

```text
PYRINTU_JWT_ISSUER
PYRINTU_JWT_AUDIENCE
```

Tests/dev can explicitly use:

```text
PYRINTU_AUTH_MODE=development
X-User-ID: <user UUID>
```

Do not enable development authentication in production.

### Database migrations

Schema changes are applied through Alembic. Application startup does not call `create_all()`.

```bash
alembic upgrade head
alembic current
```

Set `DATABASE_URL` for the target environment. No secrets are committed.

### MVP activity catalog (Discovery v1)

Discovery reads structured activities from the `activities` table. A fresh environment has no catalog rows until you seed them explicitly.

After migrations:

```bash
pip install -e ../intent -e ../discovery -e .
alembic upgrade head
python scripts/seed_mvp_activities.py
```

The seed is idempotent: existing catalog IDs are not duplicated. `GET /api/v1/opportunities` is read-only and does not seed or mutate opportunities.
