import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"
HEADERS = {"x-api-co-id": API_KEY}


def list_schools(**params) -> dict:
    response = httpx.get(
        f"{BASE_URL}/regional/indonesia/schools",
        headers=HEADERS,
        params=params,
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # page fixed 100 item. filter: province_code, regency_code, district_code,
    # npsn, name, status (N/S), grade. accreditation/lat/long = premium.
    result = list_schools(name="SD NEGERI", province_code="31", page=1)
    print(json.dumps(result, indent=2, ensure_ascii=False))
