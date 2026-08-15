# Profile MVP Scope

Pyrintu user profile is the presentation/preferences layer; authentication identity remains separate.

## MVP
- Authenticated `GET /api/v1/me/profile`
- Authenticated `PUT /api/v1/me/profile`
- Owner-only writes
- Fields: display_name, bio, avatar_url, profile_visibility
- PostgreSQL/SQLite via existing SQLAlchemy boundary
- Alembic migration required

## Explicitly out of scope
- Social-media follower/following graph
- Public user search
- Recommendations
- Exact location storage
- Authentication credential storage
