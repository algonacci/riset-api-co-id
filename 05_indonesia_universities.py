import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"
HEADERS = {"x-api-co-id": API_KEY}


def list_universities(**params) -> dict:
    response = httpx.get(
        f"{BASE_URL}/regional/indonesia/universities",
        headers=HEADERS,
        params=params,
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # page fixed 100 item. filter: province_code, regency_code, name, group, university_type
    result = list_universities(name="UNIVERSITAS INDONESIA", page=1)
    print(json.dumps(result, indent=2, ensure_ascii=False))
