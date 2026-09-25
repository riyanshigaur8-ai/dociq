from fastapi import FastAPI

from app.api.routes import router
from app.core.errors import generic_exception_handler

app = FastAPI(
    title="DocIQ API",
    description="AI-powered business transaction intelligence platform",
    version="0.1.0",
)

app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(router)