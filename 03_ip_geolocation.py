import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"
HEADERS = {"x-api-co-id": API_KEY}


def ip_geolocation(ip: str) -> dict:
    response = httpx.get(
        f"{BASE_URL}/location/ip-geolocation",
        headers=HEADERS,
        params={"ip": ip},
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    result = ip_geolocation("103.59.160.126")
    print(json.dumps(result, indent=2, ensure_ascii=False))
