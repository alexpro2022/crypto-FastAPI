from typing import Any, Iterable

from httpx import Response

from .data import ALL, client, PREFIX, QUERY_TICKER


def get_url(prefix: str, endpoint: str, query: str, currency: str, filter=None) -> str:
    filter = '' if filter is None else filter
    return prefix + endpoint + query + currency + filter


def get_sorted(arr: Iterable, each_key: str = 'timestamp', reverse: bool = False) -> list[Any]:
    return sorted([each for each in arr], key=lambda each: each[each_key], reverse=reverse)


def get_all(currency: str) -> Response:
    url = get_url(PREFIX, ALL, QUERY_TICKER, currency)
    return client.get(url)