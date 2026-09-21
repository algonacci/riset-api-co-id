import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"
HEADERS = {"x-api-co-id": API_KEY}


def list_all_rates() -> dict:
    response = httpx.get(
        f"{BASE_URL}/api/exchange-rates",
        headers=HEADERS,
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


def rates_by_currency(currency: str) -> dict:
    response = httpx.get(
        f"{BASE_URL}/currency/{currency}",
        headers=HEADERS,
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


def rates_by_pair(pair: str) -> dict:
    response = httpx.get(
        f"{BASE_URL}/currency/exchange-rate",
        headers=HEADERS,
        params={"pair": pair},
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # contoh: 1 USD ke IDR (bisa juga "USDIDR,EURIDR")
    result = rates_by_pair("USDIDR")
    print(json.dumps(result, indent=2, ensure_ascii=False))
