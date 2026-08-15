from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db import init_db
from .intent_routes import router as intent_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="Pyrintu API", version="0.1.0", lifespan=lifespan)
app.include_router(intent_router)
