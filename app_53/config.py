from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar
from pathlib import Path

class DatabaseSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    # Class variable for .env file path
    env_file: ClassVar[Path] = Path(__file__).parent / ".env"
    
    @property
    def POSTGRES_URL(self) -> str:
        """Construct and return the PostgreSQL connection URL."""
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding='utf-8',
        env_ignore_empty=True,
        extra="ignore"
    )



settings = DatabaseSettings()
print(settings.POSTGRES_USER)
print(settings.POSTGRES_PASSWORD)
print(settings.POSTGRES_SERVER)
print(settings.POSTGRES_PORT)
print(settings.POSTGRES_DB)


