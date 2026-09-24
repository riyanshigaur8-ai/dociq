from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "DocIQ API",
    description = "AI - powered business transaction intelligence platform",
    version = "0.1.0",
)

app.include_router(router)