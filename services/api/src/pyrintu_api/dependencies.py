from __future__ import annotations

from uuid import UUID

from fastapi import Header, HTTPException, status


async def get_current_user_id(x_user_id: str | None = Header(default=None, alias="X-User-ID")) -> UUID:
    """Temporary development identity boundary.

    Production authentication will replace this dependency. The route remains
    owner-scoped and does not accept owner IDs from request bodies.
    """
    if not x_user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHENTICATED")
    try:
        return UUID(x_user_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHENTICATED") from exc
