from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/health")
def health_check():
    return{
        "status": "ok",
        "service": "DocIQ",
        "version": "0.1.0",
    }