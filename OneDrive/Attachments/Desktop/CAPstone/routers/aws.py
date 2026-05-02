from fastapi import APIRouter
from fastapi import HTTPException
from services.aws_service import get_bucket_info
router = APIRouter() 

@router.get("/bucket-info",status_code=200)
def read_bucket_info():
    try:
        return get_bucket_info()
    except :
        raise HTTPException(status_code=500, 
                            detail="Internal Server Error"
                            )