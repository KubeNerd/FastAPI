from fastapi import APIRouter, Path, Query
from services.converter import sync_converter, async_converter
from asyncio import gather
from schema import ConverterInput

prices_route: APIRouter = APIRouter(prefix="/converter")

@prices_route.get("/{from_currency}")
def converter(from_currency: str, to_currencies: str, price: float):
    
    to_currencies = to_currencies.split(",")


    result = []

    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency, 
            to_currency=currency, 
            price=price
    )
    
    result.append(response)

    return result

@prices_route.get("/async/{from_currency}")
async def convert_prices_async(
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'), 
    to_currencies: str =  Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'), 
    price: float = Query(gt=0)
    ):
    
    to_currencies = to_currencies.split(",")

    coroutines = [
        async_converter(from_currency=from_currency, to_currency=currency.strip(), price=price)
        for currency in to_currencies
    ]

    results = await gather(*coroutines)
    return results


@prices_route.get("/async/v2/{from_currency}")
async def convert_prices_async(
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
 ):
    
    tasks = [
        async_converter(from_currency, to_currency, price)
        for to_currency in to_currencies
    ]

    to_currencies = body.to_currencies
    price = body.price
    
    return await gather(*tasks)