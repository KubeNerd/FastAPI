from fastapi import APIRouter
from .endpoints.example_route import exemple_router
from .endpoints.prices_route import prices_route
 
api_router = APIRouter()

api_router.include_router(exemple_router)
api_router.include_router(prices_route)