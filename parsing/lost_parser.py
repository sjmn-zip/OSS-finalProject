"""Parse found-item list XML into dicts. No network calls.

Usage: python parsing/lost_parser.py list.xml
"""
import json
import sys
import xml.etree.ElementTree as ET

# Photos in these categories may show personal information.
HIDE_PHOTO = ("카드", "증명서", "신분증", "여권", "면허", "통장", "서류")

FIELDS = {
    "atcId": "id",
    "fdSn": "sn",
    "fdPrdtNm": "name",
    "fdSbjt": "title",
    "prdtClNm": "category",
    "clrNm": "color",
    "fdYmd": "foundDate",
    "depPlace": "storedAt",
    "fdFilePathImg": "photo",
}


def _photo(url, category):
    if not url or "no_img" in url or any(w in category for w in HIDE_PHOTO):
        return ""
    return url


def parse_items(xml: bytes | str) -> tuple[list[dict], int]:
    """Return (items, total_count) from a list response. Raise RuntimeError on API errors."""
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        raise RuntimeError(f"XML 형식이 올바르지 않습니다: {e}") from e

    auth = root.findtext(".//returnAuthMsg")
    if auth:
        raise RuntimeError(f"인증 오류: {auth.strip()} (키가 맞는지, 활용신청이 승인됐는지 확인하세요)")
    code = (root.findtext(".//resultCode") or "").strip()
    if code not in ("", "00", "0"):
        raise RuntimeError(f"API 오류 {code}: {(root.findtext('.//resultMsg') or '').strip()}")

    items = []
    for el in root.iter("item"):
        item = {key: (el.findtext(tag) or "").strip() for tag, key in FIELDS.items()}
        if not item["id"] or not item["name"]:
            continue
        item["sn"] = item["sn"] or "1"
        item["photo"] = _photo(item["photo"], item["category"])
        items.append(item)

    total = (root.findtext(".//totalCount") or "").strip()
    return items, int(total) if total.isdigit() else len(items)


if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        items, total = parse_items(f.read())
    print(json.dumps({"totalCount": total, "items": items}, ensure_ascii=False, indent=2))
