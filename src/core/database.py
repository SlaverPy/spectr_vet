from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from .config import config

engine = create_async_engine(
    str(config.DATABASE_URL),
    echo=config.DB_ECHO,
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db():
    """Генератор сессии базы данных."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
