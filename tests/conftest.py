import pytest_asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base, get_async_session
from app.main import app
from app.models.currency import Currency

from .fixtures.test_db_data import TEST_DB_DATA

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(
    class_=AsyncSession, autocommit=False, autoflush=False, bind=engine)


async def load_db():
    async with TestingSessionLocal() as session:
        test_data = set([Currency(**data) for data in TEST_DB_DATA])
        session.add_all(test_data)
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

app.dependency_overrides[get_async_session] = override_get_async_session