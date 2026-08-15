from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from pyrintu_api.auth import AuthPrincipal
from pyrintu_api.db import get_session
from pyrintu_api.dependencies import get_current_principal
from pyrintu_api.match_application import MatchApplicationService
from pyrintu_api.match_repository import MatchNotFoundError
from pyrintu_api.match_schemas import (
    MatchResponse,
    MatchDecisionRequest,
    MutualityResponse,
)
from pyrintu_matching.service import MatchingService


router = APIRouter(prefix="/api/v1/matches", tags=["matches"])


def get_match_application_service() -> MatchApplicationService:
    """Dependency for match application service."""
    matching_service = MatchingService(decision_window_hours=48)
    return MatchApplicationService(matching_service=matching_service)


@router.get("/{match_id}", response_model=MatchResponse)
async def get_match(
    match_id: UUID,
    principal: AuthPrincipal = Depends(get_current_principal),
    session: AsyncSession = Depends(get_session),
    application_service: MatchApplicationService = Depends(get_match_application_service),
) -> MatchResponse:
    """
    Get a match by ID.
    
    Authorization: User must be a participant in the match.
    """
    try:
        return await application_service.get_match(
            session=session,
            match_id=match_id,
            requesting_user_id=principal.user_id,
        )
    except MatchNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e),
        )
    except Exception as e:
        # Internal server error for datetime/state errors (not 404)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal error: {e}",
        )


@router.post("/{match_id}/decision", response_model=MatchResponse)
async def record_decision(
    match_id: UUID,
    request: MatchDecisionRequest,
    principal: AuthPrincipal = Depends(get_current_principal),
    session: AsyncSession = Depends(get_session),
    application_service: MatchApplicationService = Depends(get_match_application_service),
) -> MatchResponse:
    """
    Record a participant's decision for a match.
    
    Authorization: User must be a participant in the match.
    
    Decision options: INTERESTED, MAYBE, NOT_INTERESTED
    """
    try:
        return await application_service.record_decision(
            session=session,
            match_id=match_id,
            requesting_user_id=principal.user_id,
            request=request,
        )
    except MatchNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e),
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception as e:
        # Internal server error for datetime/state errors (not 404)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal error: {e}",
        )


@router.get("/{match_id}/mutuality", response_model=MutualityResponse)
async def get_mutuality_state(
    match_id: UUID,
    principal: AuthPrincipal = Depends(get_current_principal),
    session: AsyncSession = Depends(get_session),
    application_service: MatchApplicationService = Depends(get_match_application_service),
) -> MutualityResponse:
    """
    Get mutuality state for a match.
    
    Authorization: User must be a participant in the match.
    
    Individual decisions are not exposed before mutuality is achieved.
    """
    try:
        return await application_service.get_mutuality_state(
            session=session,
            match_id=match_id,
            requesting_user_id=principal.user_id,
        )
    except MatchNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e),
        )
    except Exception as e:
        # Internal server error for datetime/state errors (not 404)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal error: {e}",
        )
