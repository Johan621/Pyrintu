from fastapi import FastAPI

from .intent_routes import router as intent_router


app = FastAPI(title="Pyrintu API", version="0.1.0")
app.include_router(intent_router)
