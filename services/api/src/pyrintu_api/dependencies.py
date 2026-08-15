from __future__ import annotations

from fastapi import Header

from .auth import AuthPrincipal, authenticate


async def get_current_principal(
    authorization: str | None = Header(default=None, alias="Authorization"),
    x_user_id: str | None = Header(default=None, alias="X-User-ID"),
) -> AuthPrincipal:
    return authenticate(authorization, x_user_id)
