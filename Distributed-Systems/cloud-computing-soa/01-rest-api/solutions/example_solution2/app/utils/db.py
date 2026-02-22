from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.constants.const import DATABASE_URL

# (Bonus concurrent programming)
# Initialize Async sqlite DB engine
engine = create_async_engine(
    f"sqlite+aiosqlite:///{DATABASE_URL}",
    connect_args={
        "check_same_thread": False,
        "isolation_level": "IMMEDIATE" # lock: lock writing (allow reading)
    }
)
# Initialize sqliteDB async session
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

async def reset_db():
    """
    Function to reset database by dropping existing tables, creating new ones.
    :return:
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("DB reset on startup")

async def get_db():
    """
    Function to get DB session
    :return: Async DB session
    """
    async with SessionLocal() as db:
        yield db
        await db.close()