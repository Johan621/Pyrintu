from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .auth import AuthPrincipal
from .db import get_session
from .dependencies import get_current_principal
from .discovery_application import DiscoveryApplicationService, NoSubmittedIntentError
from .opportunity_schemas import OpportunitiesListResponse


router = APIRouter(prefix="/api/v1/opportunities", tags=["opportunities"])

_application_service = DiscoveryApplicationService()


@router.get("", response_model=OpportunitiesListResponse)
async def list_opportunities(
    principal: AuthPrincipal = Depends(get_current_principal),
    session: AsyncSession = Depends(get_session),
) -> OpportunitiesListResponse:
    try:
        opportunities = await _application_service.list_opportunities(session, principal.user_id)
    except NoSubmittedIntentError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="INVALID_STATE") from None

    return OpportunitiesListResponse(opportunities=opportunities)
