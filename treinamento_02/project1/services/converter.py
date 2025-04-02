# https://www.postman.com/api-evangelist/alpha-vantage/request/113zz8j/currency-exchange-rates
# Documentação do AlphaVantage API 
# https://www.alphavantage.co/documentation/
# https://www.alphavantage.co/documentation/#currency-exchange

import requests
import os
from fastapi import HTTPException


def sync_converter(from_currency: str, to_currency: str, price: float):

    ALPHAVANTAGE_APIKEY = os.getenv("ALPHAVANTAGE_APIKEY")

    if not ALPHAVANTAGE_APIKEY:
        raise Exception("ALPHAVANTAGE_APIKEY are not provided")
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&{from_currency}=USD&{to_currency}=JPY&apikey=={ALPHAVANTAGE_APIKEY}'
    
    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)

    data = response.json()

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Realtime Currency Exchange Rate no in response")
    
    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchange_rate