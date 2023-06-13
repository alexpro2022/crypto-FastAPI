from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.api.routers import main_router
from app.core.config import settings
from app.client.deribit import get_data_from_tickers

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)

app.include_router(main_router)


@app.on_event('startup')
def startup():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        get_data_from_tickers,
        settings.SCHEDULER_TRIGGER,
        seconds=settings.SCHEDULER_INTERVAL,
    )
    scheduler.start()
