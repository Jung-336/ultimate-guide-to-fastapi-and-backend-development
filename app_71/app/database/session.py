from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from config import database_settings, security_setting

# Create a database engine to connect with database
engine = create_async_engine(
    # database type/dialect and file name
    url=database_settings.POSTGRES_URL,
    # Log sql queries
    echo=True,
)


async def create_db_tables():
    async with engine.begin() as connection:
        from database.models import Shipment  # noqa: F401
        await connection.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False,
    )

    async with async_session() as session:
        yield session


