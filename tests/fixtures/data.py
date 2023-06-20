from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

PREFIX = '/currency'
ALL = '/all'
LAST_PRICE = '/last-price'
PRICES = '/prices'
TICKER = 'ticker'
GET = 'GET'
FROM_DATE = 'from_date'
TO_DATE = 'to_date'
NOW = settings.get_local_time()

client = TestClient(app)


'''FILTER_BY_DATES = '&from_date={}&to_date={}'
QUERY_TICKER = '?ticker='

ENDPOINTS = (
    (PRICES, FILTER_BY_DATES.format(NOW, NOW)),
    (ALL, None),
    (LAST_PRICE, None),
)'''