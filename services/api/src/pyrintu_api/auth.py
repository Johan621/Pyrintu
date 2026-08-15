from __future__ import annotations

import os
from dataclasses import dataclass
from uuid import UUID

import jwt
from fastapi import HTTPException, status


@dataclass(frozen=True)
class AuthPrincipal:
    user_id: UUID


def _mode() -> str:
    return os.getenv("PYRINTU_AUTH_MODE", "production").lower()


def authenticate(authorization: str | None, development_user_id: str | None) -> AuthPrincipal:
    mode = _mode()

    if mode == "development":
        if not development_user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHENTICATED")
        try:
            return AuthPrincipal(UUID(development_user_id))
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHENTICATED") from exc

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHENTICATED")

    token = authorization[7:].strip()
    secret = os.getenv("PYRINTU_JWT_SECRET")
    issuer = os.getenv("PYRINTU_JWT_ISSUER")
    audience = os.getenv("PYRINTU_JWT_AUDIENCE")
    if not secret:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="AUTH_NOT_CONFIGURED")

    options = {"require": ["sub"]}
    kwargs: dict[str, object] = {"algorithms": ["HS256"], "options": options}
    if issuer:
        kwargs["issuer"] = issuer
    if audience:
        kwargs["audience"] = audience

    try:
        claims = jwt.decode(token, secret, **kwargs)
        return AuthPrincipal(UUID(str(claims["sub"])))
    except (jwt.PyJWTError, ValueError, KeyError) as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHENTICATED") from exc
