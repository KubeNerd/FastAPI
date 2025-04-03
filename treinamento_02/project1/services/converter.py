# https://www.postman.com/api-evangelist/alpha-vantage/request/113zz8j/currency-exchange-rates
# Documentação do AlphaVantage API 
# https://www.alphavantage.co/documentation/
# https://www.alphavantage.co/documentation/#currency-exchange

import requests
import os
from fastapi import HTTPException, Path
import aiohttp

ALPHAVANTAGE_APIKEY = os.getenv("ALPHAVANTAGE_APIKEY")


def sync_converter(from_currency: str, to_currency: str, price: float):

    if not ALPHAVANTAGE_APIKEY:
        raise Exception("ALPHAVANTAGE_APIKEY are not provided")
    
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}'
    try:
        response = requests.get(url=url, verify=False)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)

    data = response.json()

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Realtime Currency Exchange Rate no in response")
    
    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchange_rate

async def async_converter(from_currency: str, to_currency: str, price: float):
    if not ALPHAVANTAGE_APIKEY:
        raise Exception("ALPHAVANTAGE_APIKEY not provided")

    url = (
        f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
        f'&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}'
    )

    try:
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                data = await response.json()
    except aiohttp.ClientError as error:
        raise HTTPException(status_code=502, detail=str(error))

    if "Note" in data:
        raise HTTPException(status_code=429, detail=data["Note"])

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Realtime Currency Exchange Rate not present in response")

    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "price": price,
        "exchange_rate": exchange_rate,
        "converted_price": price * exchange_rate
    }