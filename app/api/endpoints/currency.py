from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.db import get_async_session
from app.crud.currency import currency_crud
from app.schemas.currency import CurrencyResponse

PREFIX = '/currency'
ALL = '/all'
LAST_PRICE = '/last-price'
PRICES = '/prices'

router = APIRouter(prefix=PREFIX, tags=['Currencies'])


@router.get(
    ALL,
    response_model=list[CurrencyResponse],
    summary='Получение всех сохраненных данных по указанной валюте.',
    description='Получение всех сохраненных данных по указанной валюте.',
)
async def get_currency_data_(
    ticker: str = Query(example='btc'),
    session: AsyncSession = Depends(get_async_session),
):
    return await currency_crud.get_currency_data(session, ticker.upper())


@router.get(
    LAST_PRICE,
    response_model=float,
    summary='Получение последней цены валюты.',
    description='Получение последней цены валюты.',
)
async def get_last_price_(
    ticker: str = Query(example='btc'),
    session: AsyncSession = Depends(get_async_session),
):
    return await currency_crud.get_last_price(session, ticker.upper())


@router.get(
    PRICES,
    response_model=list[float],
    summary='Получение цены валюты с фильтром по дате.',
    description='Получение цены валюты с фильтром по дате.',
)
async def get_filtered_prices_(
    ticker: str = Query(example='btc'),
    from_date: str = Query(example=settings.get_local_time()),
    to_date: str = Query(example=settings.get_local_time()),
    session: AsyncSession = Depends(get_async_session),
):
    return await currency_crud.get_filtered_prices(
        session, ticker.upper(), from_date, to_date)