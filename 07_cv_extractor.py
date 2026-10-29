import json
import os
import sys
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_CO_ID_KEY"]
BASE_URL = "https://use.api.co.id"
HEADERS = {"x-api-co-id": API_KEY}

MAX_PDF_BYTES = 5 * 1024 * 1024


def extract_cv_from_pdf(pdf_path: str | Path) -> dict:
    path = Path(pdf_path)
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Hanya mendukung PDF: {path}")
    if path.stat().st_size > MAX_PDF_BYTES:
        raise ValueError(f"Ukuran file melebihi 5 MB: {path}")

    with path.open("rb") as f:
        response = httpx.post(
            f"{BASE_URL}/ocr/upload-cv",
            headers=HEADERS,
            files={"file": (path.name, f, "application/pdf")},
            timeout=120.0,
        )
    response.raise_for_status()
    return response.json()


def extract_cv_from_text(text: str) -> dict:
    response = httpx.post(
        f"{BASE_URL}/ocr/cv-extract",
        headers=HEADERS,
        json={"text": text},
        timeout=120.0,
    )
    response.raise_for_status()
    return response.json()


SAMPLE_CV_TEXT = """John Doe
Senior Software Engineer
Email: john.doe@example.com
Phone: +62 812-3456-7890

Experience:
- Senior Software Engineer at Tech Company Inc (2020-Present)
- Software Engineer at Startup XYZ (2018-2020)

Education:
- Bachelor of Science in Computer Science, University of Indonesia (2014-2018)
"""


if __name__ == "__main__":
    # contoh: `uv run 07_cv_extractor.py cv.pdf` untuk PDF, tanpa argumen pakai teks contoh
    if len(sys.argv) > 1:
        result = extract_cv_from_pdf(sys.argv[1])
    else:
        result = extract_cv_from_text(SAMPLE_CV_TEXT)
    print(json.dumps(result, indent=2, ensure_ascii=False))
