import asyncio

import pytest

from app.client.deribit import get_tickers


@pytest.mark.asyncio
async def test_aiohttp_client(event_loop):
    assert event_loop is asyncio.get_running_loop()
    for ticker in await get_tickers():
        assert ticker.get('result').get('instrument_name').split('-')[0] in ('BTC', 'ETH')
        assert isinstance(ticker.get('result').get('index_price'), float)
        assert isinstance(ticker.get('result').get('timestamp'), int)
