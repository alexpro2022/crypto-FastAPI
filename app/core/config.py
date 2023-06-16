from datetime import datetime as dt
from datetime import timedelta

from pydantic import BaseSettings


class Settings(BaseSettings):
    # constants
    DEFAULT_STR = 'To be implemented in .env file'
    DEFAULT_DB_URL = 'sqlite+aiosqlite:///./fastapi.db'
    SCHEDULER_INTERVAL = 60
    SCHEDULER_TRIGGER = 'interval'
    # environment variables
    app_title: str = DEFAULT_STR
    app_description: str = DEFAULT_STR
    secret_key: str = DEFAULT_STR
    database_url: str = DEFAULT_DB_URL
    timedelta: int = 0
    currencies: str = 'BTC ETH'

    class Config:
        env_file = '.env'

    def get_timedelta(self):
        return timedelta(hours=self.timedelta)

    def get_local_time(self):
        return dt.utcnow() + self.get_timedelta()

    def get_currencies(self):
        return list(set([currency.upper()for currency in self.currencies.split()]))


settings = Settings()
