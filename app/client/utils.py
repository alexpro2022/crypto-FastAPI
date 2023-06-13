import logging

from app.core.db import AsyncSessionLocal
from app.models.currency import Currency

logging.basicConfig(
    level='INFO'.upper(),
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


def log(func):
    async def wrapper(*args, **kwargs):
        logger.info('Loading...')
        [logger.info(item) async for item in func(*args, **kwargs)]
        logger.info('Successfully loaded')
    return wrapper


def load(func):
    async def wrapper(*args, **kwargs):
        data = [Currency(name=name, price=price, timestamp=timestamp)
                async for name, price, timestamp in func(*args, **kwargs)]
        yield data
        async with AsyncSessionLocal() as session:
            session.add_all(data)
            await session.commit()
    return wrapper
