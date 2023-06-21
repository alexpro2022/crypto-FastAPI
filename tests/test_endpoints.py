from datetime import timedelta

from http import HTTPStatus

from .fixtures.data import ALL, GET, FROM_DATE, TO_DATE, LAST_PRICE, NOW, PREFIX, PRICES, TICKER
from .fixtures.endpoints_testlib import assert_response, invalid_methods_test, valid_values_standard_tests

# === VALID_DATA ===
PAST = NOW - timedelta(seconds=10)
FUTURE = NOW + timedelta(seconds=10)
VALID_CURRENCIES = ('BTC', 'ETH', 'bTc', 'EtH')
VALID_DATES = (
    (PAST, PAST),
    (PAST, NOW),
    (NOW, NOW),
)
# === INVALID_DATA ===
INV_METHODS = ('post', 'put', 'patch', 'delete')
INVALID_METHODS_TO_ENDPOINTS = (
    (INV_METHODS, PREFIX + ALL),
    (INV_METHODS, PREFIX + LAST_PRICE),
    (INV_METHODS, PREFIX + PRICES),
)
INVALID_CURRENCIES = (None, 'BT', 'ethC', 'ASD', '', ' ')
INVALID_DATES = (
    (None, None),
    ('', ' '),
    (NOW, ''),
    (' ', NOW),
    (str(NOW)[:7], NOW),
    (NOW, str(NOW)[:7]),
    (NOW, PAST),
    (FUTURE, NOW),
    (PAST, FUTURE),
    (NOW, FUTURE),
    (FUTURE, FUTURE),
)


def test_valid_currencies_valid_dates_standard_cases():

    def check_func(response_json):
        assert isinstance(response_json, list | float)
        return 'DONE'

    for currency in VALID_CURRENCIES:
        for from_, to_ in VALID_DATES:
            for case in (
                (GET, PREFIX + ALL, None, {TICKER: currency}, None, check_func),
                (GET, PREFIX + LAST_PRICE, None, {TICKER: currency}, None, check_func),
                (GET, PREFIX + PRICES, None, {TICKER: currency, FROM_DATE: from_, TO_DATE: to_}, None, check_func),
            ):
                valid_values_standard_tests(*case)


def test_invalid_currency():
    msg = 'Введен неверный тикер валюты - проверьте параметры запроса.'
    for currency in INVALID_CURRENCIES:
        for case in (
            (GET, PREFIX + ALL, None, {TICKER: currency}, None),
            (GET, PREFIX + LAST_PRICE, None, {TICKER: currency}, None),
            (GET, PREFIX + PRICES, None, {TICKER: currency, FROM_DATE: PAST, TO_DATE: NOW}, None),
        ):
            response = assert_response(HTTPStatus.NOT_FOUND, *case)
            assert response.json() == {'detail': msg}, response.json()


def test_invalid_dates():
    msg = 'Введены неверные даты - проверьте параметры запроса.'
    currency = 'BTC'
    for from_, to_ in INVALID_DATES:
        for case in (
            (GET, PREFIX + PRICES, None, {TICKER: currency, FROM_DATE: from_, TO_DATE: to_}, None),
        ):
            response = assert_response(HTTPStatus.BAD_REQUEST, *case)
            assert response.json() == {'detail': msg}, response.json()


def test_invalid_methods():
    for case in INVALID_METHODS_TO_ENDPOINTS:
        invalid_methods_test(*case)