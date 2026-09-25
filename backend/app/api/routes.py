from fastapi import APIRouter

from app.schemas.response import APIResponse

router = APIRouter(prefix="/api")


@router.get("/health", response_model=APIResponse)
def health_check():
    return APIResponse(
        status="success",
        message="DocIQ API is running.",
        data={
            "service": "DocIQ",
            "version": "0.1.0",
        },
    )