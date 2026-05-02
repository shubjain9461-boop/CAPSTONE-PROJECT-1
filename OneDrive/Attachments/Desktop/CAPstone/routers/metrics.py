from fastapi import APIRouter
from services.metrics_service import get_system
from fastapi import HTTPException
router = APIRouter()

@router.get("/metrics",status_code=200)
def get_metrics():
    try:
        metrics = get_system()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )