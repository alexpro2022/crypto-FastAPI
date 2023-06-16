import pytest_asyncio

from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base, get_async_session
from app.main import app
from app.models.currency import Currency

from .fixtures.fake_db_data import FAKE_DB_DATA
# from .fixtures.data import db_data

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(
    class_=AsyncSession, autocommit=False, autoflush=False, bind=engine)


# Base.metadata.create_all(bind=engine)
async def load_db():
    data = [Currency(name=d['name'], price=d['price'], timestamp=d['timestamp']) for d in FAKE_DB_DATA]
    async with TestingSessionLocal() as session:
        session.add_all(data)
        await session.commit()


@pytest_asyncio.fixture(autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await load_db()
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def override_get_async_session():
    async with TestingSessionLocal() as session:
        yield session


'''    try:
        session = TestingSessionLocal()
        yield session
    finally:
        session.close()'''


app.dependency_overrides[get_async_session] = override_get_async_session


client = TestClient(app)


'''
async def load_db():
    data = []
    for _ in range(2):
        for ticker in await get_tickers():
            name: str = ticker.get('result').get('instrument_name').split('-')[0]
            price: float = ticker.get('result').get('index_price')
            timestamp: int = ticker.get('result').get('timestamp')
            data.append(Currency(name=name, price=price, timestamp=timestamp))
        sleep(1)
    with TestingSessionLocal() as session:
        session.add_all(data)
        session.commit()
'''