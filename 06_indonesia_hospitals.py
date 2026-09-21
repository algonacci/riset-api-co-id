import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"
HEADERS = {"x-api-co-id": API_KEY}


def list_hospitals(**params) -> dict:
    response = httpx.get(
        f"{BASE_URL}/hospitals/indonesia/",
        headers=HEADERS,
        params=params,
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


def hospital_by_code(code: str) -> dict:
    response = httpx.get(
        f"{BASE_URL}/hospitals/indonesia/{code}",
        headers=HEADERS,
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # filter: code, name, type, class, blu_status, ownership, province_code, regency_code
    result = list_hospitals(name="RSUD", page=1, size=10)
    print(json.dumps(result, indent=2, ensure_ascii=False))
