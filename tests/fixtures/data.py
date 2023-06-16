from fastapi.testclient import TestClient

from app.core.config import settings
from app.api.endpoints.currency import ALL, LAST_PRICE, PREFIX, PRICES  # noqa
from app.main import app
from app.models.currency import Currency

from .fake_db_data import FAKE_DB_DATA

FILTER_BY_DATES = '&from_date={}&to_date={}'
QUERY_TICKER = '?ticker='
NOW = settings.get_local_time()
ENDPOINTS = (
    (PRICES, FILTER_BY_DATES.format(NOW, NOW)),
    (ALL, None),
    (LAST_PRICE, None),
)


db_data = [Currency(name=d['name'], price=d['price'], timestamp=d['timestamp']) for d in FAKE_DB_DATA]

client = TestClient(app)