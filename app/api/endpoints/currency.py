from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.db import get_async_session
from app.crud.currency import currency_crud
from app.schemas.currency import CurrencyResponse

router = APIRouter(prefix='/currency', tags=['Currencies'])


@router.get(
    '/all',
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
    '/last-price',
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
    '/prices',
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
