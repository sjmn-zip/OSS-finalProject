import io
import urllib.error
import urllib.parse
from unittest import mock

import pytest

import lost_client


class FakeResponse(io.BytesIO):
    status = 200


@pytest.fixture(autouse=True)
def no_env_file(monkeypatch):
    # Do not read a real .env on the developer machine.
    monkeypatch.setattr(lost_client, "load_env", lambda: None)


def sent_params(urlopen):
    url = urlopen.call_args.args[0]
    return {k: v[0] for k, v in urllib.parse.parse_qs(urllib.parse.urlparse(url).query).items()}


def test_url_has_all_params(monkeypatch):
    monkeypatch.setenv("LOST_FOUND_API_KEY", "abc%2B123")
    with mock.patch("urllib.request.urlopen", return_value=FakeResponse(b"<xml/>")) as urlopen:
        assert lost_client.fetch_items("20261127", "20261101", page=3, rows=10, region="LCA000") == b"<xml/>"
    assert sent_params(urlopen) == {
        "serviceKey": "abc+123",
        "START_YMD": "20261101",  # swapped because start > end
        "END_YMD": "20261127",
        "N_FD_LCT_CD": "LCA000",
        "pageNo": "3",
        "numOfRows": "10",
    }
    assert urlopen.call_args.kwargs["timeout"] == 15


def test_nationwide_omits_region(monkeypatch):
    monkeypatch.setenv("LOST_FOUND_API_KEY", "k")
    with mock.patch("urllib.request.urlopen", return_value=FakeResponse(b"<xml/>")) as urlopen:
        lost_client.fetch_items("20261101", "20261127")
    assert "N_FD_LCT_CD" not in sent_params(urlopen)


def test_missing_key_sends_nothing(monkeypatch):
    monkeypatch.delenv("LOST_FOUND_API_KEY", raising=False)
    with mock.patch("urllib.request.urlopen") as urlopen:
        with pytest.raises(RuntimeError, match="API 키"):
            lost_client.fetch_items("20261101", "20261127")
    urlopen.assert_not_called()


@pytest.mark.parametrize("error, message", [
    (TimeoutError(), "시간 초과"),
    (urllib.error.URLError("no route"), "연결 실패"),
    (urllib.error.HTTPError("u", 500, "Internal Server Error", None, None), "HTTP 500"),
])
def test_network_errors_raise_readable(monkeypatch, error, message):
    monkeypatch.setenv("LOST_FOUND_API_KEY", "k")
    with mock.patch("urllib.request.urlopen", side_effect=error):
        with pytest.raises(RuntimeError, match=message):
            lost_client.fetch_items("20261101", "20261127")
