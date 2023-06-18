from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

PREFIX = '/currency'
ALL = '/all'
LAST_PRICE = '/last-price'
PRICES = '/prices'

FILTER_BY_DATES = '&from_date={}&to_date={}'
QUERY_TICKER = '?ticker='
NOW = settings.get_local_time()
ENDPOINTS = (
    (PRICES, FILTER_BY_DATES.format(NOW, NOW)),
    (ALL, None),
    (LAST_PRICE, None),
)

client = TestClient(app)