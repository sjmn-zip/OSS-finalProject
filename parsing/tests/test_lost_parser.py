from pathlib import Path

import pytest

from lost_parser import FIELDS, parse_items

FIXTURES = Path(__file__).parent / "fixtures"


def read(name):
    return (FIXTURES / name).read_bytes()


def test_skips_malformed_and_keeps_order():
    items, total = parse_items(read("items_mixed.xml"))
    assert [i["id"] for i in items] == ["F2026112000001", "F2026112200003", "F2026112300004"]
    assert total == 57


def test_output_keys_and_cleanup():
    items, _ = parse_items(read("items_mixed.xml"))
    assert all(set(i) == set(FIELDS.values()) for i in items)
    assert items[0]["name"] == "검정색 반지갑"
    assert items[0]["sn"] == "2"
    assert items[1]["sn"] == "1"
    assert items[1]["color"] == ""


def test_photo_filter():
    items, _ = parse_items(read("items_mixed.xml"))
    assert items[0]["photo"] == "https://example.com/img/wallet.jpg"
    assert items[1]["photo"] == ""
    assert items[2]["photo"] == ""


def test_accepts_str():
    assert parse_items(read("items_mixed.xml").decode("utf-8")) == parse_items(read("items_mixed.xml"))


def test_total_count_fallback():
    xml = "<response><body><items><item><atcId>A</atcId><fdPrdtNm>우산</fdPrdtNm></item></items></body></response>"
    assert parse_items(xml)[1] == 1


def test_auth_error():
    with pytest.raises(RuntimeError, match="SERVICE_KEY_IS_NOT_REGISTERED_ERROR"):
        parse_items(read("auth_error.xml"))


def test_result_code_error():
    with pytest.raises(RuntimeError, match="INVALID REQUEST PARAMETER ERROR"):
        parse_items(read("result_error.xml"))


def test_broken_xml():
    with pytest.raises(RuntimeError, match="XML"):
        parse_items("<response><body>")


def test_sample_json_matches_parser_output():
    import json
    sample = json.loads((Path(__file__).parent.parent / "sample.json").read_text(encoding="utf-8"))
    assert sample and all(set(i) == set(FIELDS.values()) for i in sample)


def test_live_sample():
    # Trimmed real response (nationwide, 2026-11-20 ~ 2026-11-26, numOfRows=3).
    items, total = parse_items(read("live_sample.xml"))
    assert total == 11754
    assert [i["id"] for i in items] == ["V0007756L11250002", "V0007751L11260002", "V0007746L11230004"]
    assert items[0]["photo"] == ""                    # card category
    assert items[1]["photo"] == ""                    # no_img placeholder
    assert items[2]["photo"].startswith("https://")
    assert items[2]["foundDate"] == "2026-11-22"
