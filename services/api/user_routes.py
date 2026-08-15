from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .auth import AuthenticatedUser
from .db import get_session
from .dependencies import get_current_user
from .models import UserProfileRecord
from .schemas import ProfileResponse, ProfileUpsertRequest

router = APIRouter(prefix="/api/v1/me", tags=["profile"])


def _response(record: UserProfileRecord) -> ProfileResponse:
    return ProfileResponse(
        user_id=record.user_id,
        display_name=record.display_name,
        bio=record.bio,
        avatar_url=record.avatar_url,
        profile_visibility=record.profile_visibility,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


@router.get("/profile", response_model=ProfileResponse)
async def get_profile(
    current_user: AuthenticatedUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> ProfileResponse:
    record = await session.get(UserProfileRecord, current_user.user_id)
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PROFILE_NOT_FOUND")
    return _response(record)


@router.put("/profile", response_model=ProfileResponse)
async def upsert_profile(
    payload: ProfileUpsertRequest,
    current_user: AuthenticatedUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> ProfileResponse:
    record = await session.get(UserProfileRecord, current_user.user_id)
    if record is None:
        record = UserProfileRecord(user_id=current_user.user_id)
        session.add(record)
    record.display_name = payload.display_name
    record.bio = payload.bio
    record.avatar_url = payload.avatar_url
    record.profile_visibility = payload.profile_visibility
    await session.commit()
    await session.refresh(record)
    return _response(record)
