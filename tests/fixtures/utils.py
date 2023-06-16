def get_url(prefix, endpoint, query, currency, filter=None):
    filter = '' if filter is None else filter
    return prefix + endpoint + query + currency + filter