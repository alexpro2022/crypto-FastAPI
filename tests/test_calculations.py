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
            assert 'id' in each, url
            assert each['name'] == currency, url
            assert 'price' in each, url
            assert 'timestamp' in each, url


def test_last_price_for_currency():
    for currency in settings.get_currencies():
        url = get_url(PREFIX, LAST_PRICE, QUERY_TICKER, currency)
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, url
        assert isinstance(response.json(), float)