from datetime import datetime as dt
from http import HTTPStatus
from typing import Any

from fastapi import HTTPException
from sqlalchemy import and_, desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.db import Base
from app.models.currency import Currency
from app.schemas.currency import CurrencyResponse


class CRUD:
    NOT_FOUND = 'Object(s) not found.'
    BAD_REQUEST = 'Query params are out of order.'

    def __init__(self, model: Base) -> None:
        self.model = model

    async def __get_by_attribute(
        self,
        session: AsyncSession,
        attr_name: str,
        attr_value: Any,
    ):
        return await session.scalars(
            select(self.model).where(
                getattr(self.model, attr_name) == attr_value
            ).order_by(desc(self.model.timestamp))
        )

    async def _get_all_by_attr(
        self,
        session: AsyncSession,
        attr_name: str,
        attr_value: Any,
        exception: bool = False
    ) -> list[Base] | None:
        """Raises `NOT_FOUND` exception if
           no objects are found and `exception=True`."""
        objs = await self.__get_by_attribute(
            session, attr_name, attr_value)
        objects = objs.all()
        if not objects and exception:
            raise HTTPException(HTTPStatus.NOT_FOUND, self.NOT_FOUND)
        return objects

    async def _get_by_attr(
        self,
        session: AsyncSession,
        attr_name: str,
        attr_value: Any,
        exception: bool = False
    ) -> Base | None:
        """Raises `NOT_FOUND` exception if
           no object is found and `exception=True`."""
        objs = await self.__get_by_attribute(
            session, attr_name, attr_value)
        object = objs.first()
        if object is None and exception:
            raise HTTPException(HTTPStatus.NOT_FOUND, self.NOT_FOUND)
        return object


class CurrencyCRUD(CRUD):
    NOT_FOUND = 'Введен неверный тикер валюты - проверьте параметры запроса.'
    BAD_REQUEST = 'Введены неверные даты - проверьте параметры запроса.'

    def __init__(self) -> None:
        super().__init__(Currency)

    def _validate_currency(self, currency: str) -> None:
        if currency not in settings.get_currencies():
            raise HTTPException(HTTPStatus.NOT_FOUND, self.NOT_FOUND)

    def _validate_dates(
            self, from_date: str, to_date: str) -> tuple[int, int]:
        try:
            from_date = dt.fromisoformat(from_date) - settings.get_timedelta()
            to_date = dt.fromisoformat(to_date) - settings.get_timedelta()
        except ValueError:
            raise HTTPException(HTTPStatus.BAD_REQUEST, self.BAD_REQUEST)
        now = dt.utcnow()
        if from_date > to_date or from_date > now or to_date > now:
            raise HTTPException(HTTPStatus.BAD_REQUEST, self.BAD_REQUEST)
        return [int(item.timestamp()) for item in (from_date, to_date)]

    async def get_currency_data(
        self, session: AsyncSession, currency: str
    ) -> list[CurrencyResponse]:
        self._validate_currency(currency)
        return await self._get_all_by_attr(
            session, 'name', currency, exception=True)

    async def get_last_price(
            self, session: AsyncSession, currency: str) -> float:
        self._validate_currency(currency)
        last = await self._get_by_attr(
            session, 'name', currency, exception=True)
        return last.price

    async def get_filtered_prices(
        self, session: AsyncSession, currency: str,
        from_date: str, to_date: str,
    ) -> list[float]:
        self._validate_currency(currency)
        res = await session.scalars(
            select(self.model).where(
                and_(
                    self.model.name == currency,
                    self.model.timestamp.between(
                        *self._validate_dates(from_date, to_date))
                )
            ).order_by(desc(self.model.timestamp))
        )
        return [res.price for res in res.all()]


currency_crud = CurrencyCRUD()
