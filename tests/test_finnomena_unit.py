"""Hermetic tests for the Finnomena source.

These mock the HTTP layer so they run anywhere (CI included) and pin the
response-parsing contract that broke when Finnomena retired the nav/latest
endpoint. The live-API counterparts live in test_core.py (marked `network`).
"""

import responses

import pythainav as nav

LIST_URL = "https://www.finnomena.com/fn3/api/fund/public/list"
RANGE_URL = "https://www.finnomena.com/fn3/api/fund/v2/public/funds/F0001/nav/q"


def _register():
    responses.add(
        responses.GET,
        LIST_URL,
        json=[{"id": "F0001", "short_code": "KT-TEST", "name_th": "ทดสอบ"}],
    )
    responses.add(
        responses.GET,
        RANGE_URL,
        json={
            "status": True,
            "data": {
                "navs": [
                    {
                        "date": "2024-01-01T00:00:00Z",
                        "value": 10.0,
                        "amount": 100,
                    },
                    {
                        "date": "2024-01-02T00:00:00Z",
                        "value": 11.0,
                        "amount": 110,
                    },
                ]
            },
        },
    )


@responses.activate
def test_get_latest_returns_most_recent():
    _register()
    n = nav.get("KT-TEST")
    assert n.value == 11.0
    assert n.tags == {"latest"}
    assert n.updated.day == 2


@responses.activate
def test_get_all_returns_full_series():
    _register()
    navs = nav.get_all("KT-TEST")
    assert [n.value for n in navs] == [10.0, 11.0]


@responses.activate
def test_get_with_date_picks_on_or_before():
    _register()
    n = nav.get("KT-TEST", date="2024-01-01")
    assert n.value == 10.0


@responses.activate
def test_get_is_case_insensitive():
    _register()
    assert nav.get("kt-test").value == 11.0
