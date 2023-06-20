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
