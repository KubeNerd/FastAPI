from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1")
async def index_router():
    return 0