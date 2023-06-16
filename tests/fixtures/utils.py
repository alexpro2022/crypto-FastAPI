from .data import ALL, client, PREFIX, QUERY_TICKER


def get_url(prefix, endpoint, query, currency, filter=None):
    filter = '' if filter is None else filter
    return prefix + endpoint + query + currency + filter


def get_sorted_response(response):
    return sorted([each for each in response.json()], key=lambda each: each['timestamp'])


def get_all(currency):
    url = get_url(PREFIX, ALL, QUERY_TICKER, currency)
    return client.get(url)