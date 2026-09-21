import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"


def reverse_geocode(lat: float, lon: float) -> dict:
    response = httpx.get(
        f"{BASE_URL}/location/reverse-geocode",
        headers={"x-api-co-id": API_KEY},
        params={"lat": lat, "lon": lon},
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # contoh: sekitar Monas, Jakarta
    result = reverse_geocode(-6.2088, 106.8456)
    print(json.dumps(result, indent=2, ensure_ascii=False))
