from datetime import timedelta
from http import HTTPStatus

from .fixtures.data import client, FILTER_BY_DATES, PREFIX, PRICES, QUERY_TICKER, NOW, ENDPOINTS
from .utils import get_invalid, get_url


CURRENCIES = ('BTC', 'ETH', 'bTc', 'EtH')

PAST = NOW - timedelta(seconds=10)
FUTURE = NOW + timedelta(seconds=10)

INVALID_DATES = (
    ('', ' '),
    (NOW, ''),
    (' ', NOW),
    (str(NOW)[:7], NOW),
    (NOW, str(NOW)[:7]),
    (NOW, PAST),
    (FUTURE, NOW),
    (PAST, FUTURE),
    (FUTURE, FUTURE),
)


def test_currency_invalid_methods():
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            url = get_url(PREFIX, endpoint, QUERY_TICKER, currency, filter)
            for invalid_method in (client.put, client.patch, client.delete, client.post):
                assert invalid_method(url).status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_invalid_prefix():
    for invalid_prefix in get_invalid(PREFIX):
        for endpoint, filter in ENDPOINTS:
            for currency in CURRENCIES:
                url = get_url(invalid_prefix, endpoint, QUERY_TICKER, currency, filter)
                response = client.get(url)
                assert response.status_code == HTTPStatus.NOT_FOUND, url


def test_invalid_endpoint():
    for endpoint, filter in ENDPOINTS:
        for invalid_endpoint in get_invalid(endpoint):
            for currency in CURRENCIES:
                url = get_url(PREFIX, invalid_endpoint, QUERY_TICKER, currency, filter)
                response = client.get(url)
                assert response.status_code == HTTPStatus.NOT_FOUND, url


def test_invalid_query_sintax():
    invalid_tickers = get_invalid(QUERY_TICKER)
    for invalid_ticker in invalid_tickers:
        for endpoint, filter in ENDPOINTS:
            for currency in CURRENCIES:
                url = get_url(PREFIX, endpoint, invalid_ticker, currency, filter)
                response = client.get(url)
                if invalid_ticker == invalid_tickers[-1]:
                    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, url
                else:
                    assert response.status_code == HTTPStatus.NOT_FOUND, url


def test_invalid_currency():
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            for invalid_currency in get_invalid(currency):
                url = get_url(PREFIX, endpoint, QUERY_TICKER, invalid_currency, filter)
                response = client.get(url)
                assert response.status_code == HTTPStatus.NOT_FOUND, url
                assert response.json() == {'detail': 'Введен неверный тикер валюты - проверьте параметры запроса.'}, url


def test_invalid_filter_sintax():
    for invalid_filter in get_invalid(FILTER_BY_DATES):
        for currency in CURRENCIES:
            url = get_url(PREFIX, PRICES, QUERY_TICKER, currency, invalid_filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, url


def test_invalid_dates():
    for currency in CURRENCIES:
        for dates in INVALID_DATES:
            url = get_url(PREFIX, PRICES, QUERY_TICKER, currency, FILTER_BY_DATES.format(*dates))
            response = client.get(url)
            assert response.status_code == HTTPStatus.BAD_REQUEST, url
            assert response.json() == {'detail': 'Введены неверные даты - проверьте параметры запроса.'}, url


def test_valid_urls():
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            url = get_url(PREFIX, endpoint, QUERY_TICKER, currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.OK, url
            assert isinstance(response.json(), list | float)
