from http import HTTPStatus


from app.core.config import settings

from .fixtures.data import ALL, client, PREFIX, PRICES, LAST_PRICE, QUERY_TICKER
from .fixtures.utils import get_url


def test_get_all_for_currency():
    for currency in settings.get_currencies():
        url = get_url(PREFIX, ALL, QUERY_TICKER, currency)
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, url
        assert isinstance(response.json(), list)
        for each in response.json():
            assert isinstance(each, dict)
            assert isinstance(each['id'], int)
            assert each['name'] == currency, url
            assert isinstance(each['price'], float), url
            assert isinstance(each['timestamp'], int), url


def test_last_price_for_currency():
    for currency in settings.get_currencies():
        url = get_url(PREFIX, LAST_PRICE, QUERY_TICKER, currency)
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, url
        price = response.json()
        assert isinstance(price, float), url
        url = get_url(PREFIX, ALL, QUERY_TICKER, currency)
        response = client.get(url)
        assert price == sorted([each for each in response.json()], key=lambda each: each['timestamp'])[-1]['price'], url


'''def test_prices():
    for currency in settings.get_currencies():
        url = get_url(PREFIX, PRICES, QUERY_TICKER, currency)'''