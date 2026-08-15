from fastapi import FastAPI

from .intent_routes import router as intent_router
from .match_routes import router as match_router
from .opportunity_routes import router as opportunity_router
from .profile_routes import router as profile_router


app = FastAPI(title="Pyrintu API", version="0.1.0")
app.include_router(intent_router)
app.include_router(profile_router)
app.include_router(opportunity_router)
app.include_router(match_router)
