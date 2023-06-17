from fastapi.testclient import TestClient

from app.core.config import settings
from app.api.endpoints.currency import ALL, LAST_PRICE, PREFIX, PRICES  # noqa
from app.main import app

FILTER_BY_DATES = '&from_date={}&to_date={}'
QUERY_TICKER = '?ticker='
NOW = settings.get_local_time()
ENDPOINTS = (
    (PRICES, FILTER_BY_DATES.format(NOW, NOW)),
    (ALL, None),
    (LAST_PRICE, None),
)

client = TestClient(app)