import asyncio
from urllib.parse import urljoin

import aiohttp

from .utils import log, load

BASE_URL = 'https://test.deribit.com/api/v2/'
TICKER_ENDPOINT = 'public/ticker?instrument_name='
CURRENCIES = ('BTC-PERPETUAL', 'ETH-PERPETUAL')


async def get_ticker(session, url):
    async with session.get(url) as response:
        return await response.json()


async def get_tickers(currencies: tuple[str] = CURRENCIES) -> None:
    url = urljoin(BASE_URL, TICKER_ENDPOINT)
    async with aiohttp.ClientSession() as session:
        tasks = [get_ticker(session, url + currency)
                 for currency in currencies]
        return await asyncio.gather(*tasks)


@log
@load
async def get_data_from_tickers():
    for ticker in await get_tickers():
        name = ticker.get('result').get('instrument_name').split('-')[0]
        price = ticker.get('result').get('index_price')
        timestamp = ticker.get('result').get('timestamp')
        yield name, price, int(timestamp/1000)
