from fastapi import APIRouter
from api.v1.endpoints import cursos
from api.v1.endpoints import  healthcheck

api_router = APIRouter()

api_router.include_router(cursos.router, prefix='/cursos', tags=['cursos'])
api_router.include_router(healthcheck.router, prefix='/healthcheck')