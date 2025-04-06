from fastapi import APIRouter

health_check_router = APIRouter()


@health_check_router.get("/health")

def check():
    return {"status": "ok"}
