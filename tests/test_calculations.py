from http import HTTPStatus


from app.core.config import settings

from .fixtures.data import client, FILTER_BY_DATES, NOW, PREFIX, PRICES, LAST_PRICE, QUERY_TICKER
from .fixtures.utils import get_all, get_sorted, get_url


def test_get_all_for_currency():
    for currency in settings.get_currencies():
        response = get_all(currency)
        assert response.status_code == HTTPStatus.OK
        all = response.json()
        assert isinstance(all, list)
        assert all == get_sorted(all, reverse=True)
        for each in all:
            assert isinstance(each, dict)
            assert isinstance(each['id'], int)
            assert each['name'] == currency
            assert isinstance(each['price'], float)
            assert isinstance(each['timestamp'], int)


def test_last_price_for_currency():
    for currency in settings.get_currencies():
        url = get_url(PREFIX, LAST_PRICE, QUERY_TICKER, currency)
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, url
        price = response.json()
        assert isinstance(price, float), url
        response = get_all(currency).json()
        assert price == get_sorted(response)[-1]['price'], url


def test_prices():
    for currency in settings.get_currencies():
        for dates in (
            (NOW, NOW),
        ):
            url = get_url(PREFIX, PRICES, QUERY_TICKER, currency, FILTER_BY_DATES.format(*dates))
            response = client.get(url)
            assert response.status_code == HTTPStatus.OK
            prices = response.json()
            assert isinstance(prices, list)
