from .data import ALL, client, PREFIX, QUERY_TICKER


def get_url(prefix, endpoint, query, currency, filter=None):
    filter = '' if filter is None else filter
    return prefix + endpoint + query + currency + filter


def get_sorted(arr, each_key: str = 'timestamp', reverse: bool = False):
    return sorted([each for each in arr], key=lambda each: each[each_key], reverse=reverse)


def get_all(currency):
    url = get_url(PREFIX, ALL, QUERY_TICKER, currency)
    return client.get(url)