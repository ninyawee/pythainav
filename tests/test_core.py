"""Live-API tests for the Finnomena source.

These hit the real Finnomena endpoints and so are marked `network`; CI runs
`-m 'not network'` to skip them (Finnomena returns non-JSON to datacenter IPs).
Run them locally with `pytest -m network` to catch upstream API drift. The
hermetic equivalents live in test_finnomena_unit.py.
"""

import pytest

import pythainav as nav


@pytest.mark.network
def test_get_nav():
    kt_nav = nav.get("KT-PRECIOUS")
    print(kt_nav)
    assert kt_nav.value >= 0


@pytest.mark.network
def test_get_nav_with_date():
    oil_nav = nav.get("KT-PRECIOUS", date="1 week ago")
    print(oil_nav)
    assert oil_nav.value >= 0


@pytest.mark.network
def test_get_all():
    kt_navs = nav.get_all("KT-PRECIOUS")
    print(kt_navs)
    assert len(kt_navs) >= 0


@pytest.mark.network
def test_get_all_pandas():
    import pandas as pd

    df = nav.get_all("KT-PRECIOUS", asDataFrame=True)
    assert isinstance(df, pd.DataFrame)


@pytest.mark.skip(reason="For dev only, required real api key")
def test_sec_source():
    from decouple import config

    subs_key = {
        "fundfactsheet": config("FUND_FACTSHEET_KEY"),
        "funddailyinfo": config("FUND_DAILY_INFO_KEY"),
    }

    # should auto convert to friday if it is a weekend
    # kt_nav = nav.get("KT-PRECIOUS", source="sec", subscription_key=subs_key)
    # print(kt_nav)
    # assert kt_nav.value >= 0

    kt_nav = nav.get(
        "KT-PRECIOUS",
        source="sec",
        subscription_key=subs_key,
        date="03/04/2020",
    )
    print(kt_nav)
    assert kt_nav.value >= 0


@pytest.mark.network
def test_no_name_collide():
    f = nav.sources.Finnomena()
    funds = f.list()
    codes = list(funds.keys())
    assert len(codes) == len({code.lower() for code in codes})


@pytest.mark.network
def test_case_insensitive():
    kt_nav = nav.get("kt-precious")
    print(kt_nav)
    assert kt_nav.value >= 0
