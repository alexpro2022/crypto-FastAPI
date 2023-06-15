from fastapi.testclient import TestClient

from app.api.endpoints.currency import ENDPOINTS, PRICES
from app.main import app

CURRENCIES = ('BTC', 'ETH', 'bTc', 'EtH')
FILTER_BY_DATES = f'&from_date=2023-06-16T02%3A11%3A30.784878&to_date=2023-06-16T02%3A11%3A30.784894'

client = TestClient(app)


def test_invalid_currency():
    for endpoint in ENDPOINTS:
        endpoint += '?ticker=' + 'ASD'
        response = client.get(endpoint)
        if PRICES in endpoint:
            assert response.status_code == 422
            endpoint += FILTER_BY_DATES
            response = client.get(endpoint)
            assert response.status_code == 404
        else:
            assert response.status_code == 404


'''def test_valid_currencies():
    for endpoint in ENDPOINTS:
        for currency in CURRENCIES:
            response = client.get(endpoint + '?ticker=' + currency)
            assert response.status_code == 200, f'{endpoint}'
    '''