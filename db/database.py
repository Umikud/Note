from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.util._compat_py3k import asynccontextmanager

Base = declarative_base()

engine = create_async_engine(
    'sqlite+aiosqlite:///base.db',
    future=True
)


async def create_base():
    """
    Функкция создание базы данных
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def get_session():
    try:
        async with sessionmaker(engine, class_=AsyncSession)() as session:
            yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
