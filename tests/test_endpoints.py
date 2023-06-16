from datetime import timedelta
from http import HTTPStatus

from .fixtures.data import client, FILTER_BY_DATES, PREFIX, PRICES, QUERY_TICKER, NOW, ENDPOINTS
from .fixtures.utils import get_url


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


def test_invalid_prefix():
    invalid_prefix = PREFIX[:-1] if PREFIX else ' '
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            url = get_url(invalid_prefix, endpoint, QUERY_TICKER, currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.NOT_FOUND, url


def test_invalid_endpoint():
    for endpoint, filter in ENDPOINTS:
        invalid_endpoint = endpoint[:-1] if endpoint else ' '
        for currency in CURRENCIES:
            url = get_url(PREFIX, invalid_endpoint, QUERY_TICKER, currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.NOT_FOUND, url


def test_invalid_query_sintax():
    invalid_ticker = QUERY_TICKER.replace('c', '') if QUERY_TICKER else ' '
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            url = get_url(PREFIX, endpoint, invalid_ticker, currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, url


def test_invalid_currency():
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            invalid_currency = currency[:-1] if currency else ' '
            url = get_url(PREFIX, endpoint, QUERY_TICKER, invalid_currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.NOT_FOUND, url
            assert response.json() == {'detail': 'Введен неверный тикер валюты - проверьте параметры запроса.'}, url


def test_invalid_filter_sintax():
    invalid_filter = FILTER_BY_DATES.format(NOW, NOW).replace('_', '')
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
            assert response.json() is list or float
