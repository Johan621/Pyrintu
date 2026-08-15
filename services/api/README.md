# Pyrintu API Service

First application-facing API slice for Intent creation.

## Scope

- FastAPI route surface under `/api/v1`.
- Owner-scoped Intent creation/read/update/submit.
- SQLAlchemy persistence boundary using `DATABASE_URL`.
- SQLite is supported for local development/tests; PostgreSQL is the intended deployed database.
- Domain service remains the business-rule authority.

## Local setup

```bash
python -m venv .venv
pip install -e .[test]
pytest
uvicorn pyrintu_api.main:app --reload
```

Set `DATABASE_URL` for a persistent database. No secrets are committed.
