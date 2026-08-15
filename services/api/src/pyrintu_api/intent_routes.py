from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .auth import AuthPrincipal
from .db import get_session
from .dependencies import get_current_principal
from .models import IntentRecord
from .schemas import IntentCreateRequest, IntentResponse, IntentSubmitRequest

try:
    from pyrintu_intent.service import IntentInterpreter, IntentValidationError
except ModuleNotFoundError:  # pragma: no cover - deployment packaging supplies the domain package
    IntentInterpreter = None  # type: ignore[assignment,misc]
    IntentValidationError = ValueError  # type: ignore[assignment,misc]


router = APIRouter(prefix="/api/v1/intents", tags=["intents"])


def _parse(text: str):
    if IntentInterpreter is None:
        raise HTTPException(status_code=500, detail="INTENT_DOMAIN_PACKAGE_UNAVAILABLE")
    try:
        return IntentInterpreter().parse(text)
    except IntentValidationError as exc:
        raise HTTPException(status_code=422, detail="VALIDATION_ERROR") from exc


def _response(record: IntentRecord) -> IntentResponse:
    return IntentResponse(
        id=record.id,
        owner_user_id=record.owner_user_id,
        status=record.status,
        goal_type=record.goal_type,
        raw_input=record.raw_input,
        normalized_goal=record.normalized_goal_json,
        constraints=record.constraints_json,
        availability=record.availability_json,
        version=record.version,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


@router.post("", response_model=IntentResponse, status_code=status.HTTP_201_CREATED)
async def create_intent(
    payload: IntentCreateRequest,
    principal: AuthPrincipal = Depends(get_current_principal),
    session: AsyncSession = Depends(get_session),
) -> IntentResponse:
    parsed = _parse(payload.text)
    record = IntentRecord(
        owner_user_id=principal.user_id,
        status="DRAFT",
        goal_type="experience",
        raw_input=payload.text.strip(),
        normalized_goal_json={"goal": parsed.goal},
        constraints_json={
            "experience": parsed.experience,
            "group_size": parsed.group_size,
            "budget_max": parsed.budget_max,
            "location": parsed.location,
        },
        availability_json={"time_window": parsed.time_window},
        version=1,
    )
    session.add(record)
    await session.commit()
    await session.refresh(record)
    return _response(record)


@router.get("/{intent_id}", response_model=IntentResponse)
async def get_intent(
    intent_id: UUID,
    principal: AuthPrincipal = Depends(get_current_principal),
    session: AsyncSession = Depends(get_session),
) -> IntentResponse:
    record = await session.scalar(
        select(IntentRecord).where(IntentRecord.id == intent_id, IntentRecord.owner_user_id == principal.user_id)
    )
    if record is None:
        raise HTTPException(status_code=404, detail="NOT_FOUND")
    return _response(record)


@router.post("/{intent_id}/submit", response_model=IntentResponse)
async def submit_intent(
    intent_id: UUID,
    payload: IntentSubmitRequest,
    principal: AuthPrincipal = Depends(get_current_principal),
    session: AsyncSession = Depends(get_session),
) -> IntentResponse:
    record = await session.scalar(
        select(IntentRecord).where(IntentRecord.id == intent_id, IntentRecord.owner_user_id == principal.user_id)
    )
    if record is None:
        raise HTTPException(status_code=404, detail="NOT_FOUND")
    if record.version != payload.expected_version:
        raise HTTPException(status_code=409, detail="INTENT_VERSION_STALE")
    if record.status != "DRAFT":
        raise HTTPException(status_code=409, detail="INVALID_STATE")

    record.status = "SUBMITTED"
    record.version += 1
    record.updated_at = datetime.now(timezone.utc)
    await session.commit()
    await session.refresh(record)
    return _response(record)
