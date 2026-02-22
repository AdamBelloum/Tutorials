from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.settings import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@db:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
print("DATABASE_URL", DATABASE_URL)
engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

async def create_tables_if_not_exist():
    """
    Function to reset database by creating new tables if they do not exist.
    :return:
    """
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("DB reset on startup")
    except Exception as e:
        print(f"Error - Creating tables: {e}")

async def get_db():
    """
    Function to get DB session
    :return: Async DB session
    """
    async with SessionLocal() as db:
        yield db