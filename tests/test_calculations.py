from datetime import datetime as dt

from http import HTTPStatus

from app.core.config import settings

from .fixtures.data import ALL, GET, FROM_DATE, TO_DATE, PREFIX, PRICES, LAST_PRICE, TICKER
from .fixtures.endpoints_testlib import assert_response
from .utils import check_data, check_item, get_sorted, get_randome_timestamps, get_test_data, get_test_prices


def test_get_all_for_currency():
    for currency in settings.get_currencies():
        all = assert_response(HTTPStatus.OK, GET, PREFIX + ALL, query_params={TICKER: currency}).json()
        assert isinstance(all, list)
        assert all == get_sorted(all, reverse=True)
        for each in all:
            check_item(each, currency)
        check_data(all, get_test_data(currency))


def test_last_price_for_currency():
    for currency in settings.get_currencies():
        response = assert_response(HTTPStatus.OK, GET, PREFIX + LAST_PRICE, query_params={TICKER: currency})
        last_price = response.json()
        assert isinstance(last_price, float), last_price
        all = assert_response(HTTPStatus.OK, GET, PREFIX + ALL, query_params={TICKER: currency}).json()
        assert last_price == all[0]['price'], last_price


def test_prices():
    for currency in settings.get_currencies():
        for _ in range(10):
            from_, to_ = get_randome_timestamps(get_test_data(currency))
            prices = assert_response(HTTPStatus.OK, GET, PREFIX + PRICES, query_params={
                TICKER: currency, FROM_DATE: dt.fromtimestamp(from_), TO_DATE: dt.fromtimestamp(to_)}).json()
            assert isinstance(prices, list)
            assert prices == get_test_prices(currency, from_, to_)