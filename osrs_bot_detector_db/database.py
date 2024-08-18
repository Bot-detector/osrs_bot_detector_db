from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class Database:
    def __init__(self, database_url: str):
        # Create async engine
        self.engine = create_async_engine(database_url, echo=True)
        # Create session factory
        self.SessionLocal = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )
        # Create scoped session
        self.scoped_session = scoped_session(self.SessionLocal)

    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Provides an async context manager for the session.
        Yields:
            AsyncSession: An asynchronous SQLAlchemy session.
        """
        async with self.scoped_session() as session:
            yield session

    async def close(self) -> None:
        """
        Dispose of the SQLAlchemy engine.
        """
        await self.engine.dispose()
