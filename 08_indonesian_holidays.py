import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"
HEADERS = {"x-api-co-id": API_KEY}

# nilai valid untuk parameter `type`
HOLIDAY_TYPES = ("Public Holiday", "Joint Holiday", "National Holiday", "Observance")


def _get(path: str, **params) -> dict:
    response = httpx.get(
        f"{BASE_URL}/holidays/indonesia{path}",
        headers=HEADERS,
        params={k: v for k, v in params.items() if v is not None},
        timeout=30.0,
    )
    response.raise_for_status()
    return response.json()


def list_holidays(**params) -> dict:
    # filter: year, month, type, start_date, end_date, page (size tetap 100)
    return _get("/", **params)


def holiday_by_id(holiday_id: int) -> dict:
    # id numerik (mis. 1213), bukan format "holiday_2025_01_01" seperti di docs
    return _get(f"/{holiday_id}")


def check_date(date: str) -> dict:
    return _get("/check/date", date=date)


def check_range(start_date: str, end_date: str, type: str | None = None) -> dict:
    return _get("/check/range", start_date=start_date, end_date=end_date, type=type)


# per 2026-10-30 endpoint di bawah ini selalu 400 "Invalid holiday ID":
# di server, path satu segmen ketangkap route /{id} duluan
def next_holiday(type: str | None = None) -> dict:
    return _get("/next", type=type)


def upcoming_holidays(limit: int | None = None, type: str | None = None) -> dict:
    return _get("/upcoming", limit=limit, type=type)


def holiday_stats(year: int) -> dict:
    return _get("/stats", year=year)


def holiday_calendar(year: int, month: int) -> dict:
    return _get("/calendar", year=year, month=month)


def available_years() -> dict:
    return _get("/years")


def holiday_types() -> dict:
    return _get("/types")


if __name__ == "__main__":
    result = {
        "list_dec_2026": list_holidays(year=2026, month=12),
        "check_date": check_date("2026-12-25"),
        "check_range": check_range("2026-12-01", "2026-12-31", type="Public Holiday"),
        "by_id": holiday_by_id(1213),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
