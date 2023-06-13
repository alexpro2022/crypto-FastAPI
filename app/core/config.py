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

    class Config:
        env_file = '.env'


settings = Settings()
