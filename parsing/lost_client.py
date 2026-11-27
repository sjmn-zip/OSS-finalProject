"""Fetch raw found-item XML from the National Police Agency API.

Usage: python parsing/lost_client.py 20261101 20261127 > list.xml
"""
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

URL = "https://apis.data.go.kr/1320000/LosPtfundInfoInqireService/getPtLosfundInfoAccToClAreaPd"
TIMEOUT = 15


def load_env(path=Path(__file__).parent.parent / ".env"):
    """Load KEY=VALUE lines from .env. Existing environment variables win."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def api_key():
    """Return the service key. Raise RuntimeError if it is missing."""
    key =os.environ.get("LOST_FOUND_API_KEY", "").strip()
    if not key:
        raise RuntimeError("API 키가 없습니다. 환경변수 LOST_FOUND_API_KEY 나 .env 에 넣어 주세요.")
    # Decode the portal's "Encoding" key once; urlencode re-encodes it.
    return urllib.parse.unquote(key) if "%" in key else key


def fetch_items(start: str, end: str, page: int = 1, rows: int = 20, region: str | None = None) -> bytes:
    """Return the raw list XML. region is an area code such as "LCA000" (Seoul); None means nationwide.

    Raise RuntimeError on a missing key, network error, timeout or non-200 response.
    """
    load_env()
    params = {
        "serviceKey": api_key(),
        "START_YMD": min(start, end),
        "END_YMD": max(start, end),
        "pageNo": page,
        "numOfRows": rows,
    }
    if region:
        params["N_FD_LCT_CD"] = region
    url = f"{URL}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
            if r.status != 200:
                raise RuntimeError(f"API 응답 오류: HTTP {r.status}")
            return r.read()
    except urllib.error.HTTPError as e:  # subclass of URLError, so catch it first
        raise RuntimeError(f"API 응답 오류: HTTP {e.code} {e.reason}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"API 연결 실패: {e.reason}") from e
    except TimeoutError as e:
        raise RuntimeError(f"API 응답 시간 초과 ({TIMEOUT}초)") from e


if __name__ == "__main__":
    sys.stdout.buffer.write(fetch_items(*sys.argv[1:3]))
