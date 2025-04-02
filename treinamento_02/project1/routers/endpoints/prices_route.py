from fastapi import APIRouter, HTTPException

# Documentação do AlphaVantage API 
# https://www.alphavantage.co/documentation/
# https://www.alphavantage.co/documentation/#currency-exchange


prices_route: APIRouter = APIRouter()

@prices_route.get("/converter/{from_currency}")
def converter(from_currency: str, to_currencies: str, price: float):
    return "it works"