import asyncio
from typing import Any, Generator
from urllib.parse import urljoin

import aiohttp

from app.core.config import settings

from .utils import load, log

BASE_URL = 'https://test.deribit.com/api/v2/'
TICKER_ENDPOINT = 'public/ticker?instrument_name='
CURRENCIES = [item + '-PERPETUAL' for item in settings.get_currencies()]


async def get_ticker(session, url):
    async with session.get(url) as response:
        return await response.json()


async def get_tickers(
        currencies: list[str] = CURRENCIES) -> asyncio.Future[list[Any]]:
    url = urljoin(BASE_URL, TICKER_ENDPOINT)
    async with aiohttp.ClientSession() as session:
        tasks = [get_ticker(session, url + currency)
                 for currency in currencies]
        return await asyncio.gather(*tasks)


@log
@load
async def get_data_from_tickers() -> Generator[str, float, int]:
    for ticker in await get_tickers():
        name: str = ticker.get('result').get('instrument_name').split('-')[0]
        price: float = ticker.get('result').get('index_price')
        timestamp: int = ticker.get('result').get('timestamp')
        yield name, price, int(timestamp / 1000)
