from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from models import Base


class DataBase:
    def __init__(self) -> None:
        db_url = URL(
            drivername="postgresql+asyncpg",
            username="rashed",
            password="R@shedu1",
            host="localhost",
            port=5432,
            database="demo_db",
            query={
                "ssl": "disable"
            }
        )
        self.engine = create_async_engine(url=db_url)
        self.async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)
    
    @property
    def get_session(self):
        return self.async_session

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
