from contextlib import asynccontextmanager

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Database URL for testing
TEST_DB_URL = "mysql+aiomysql://root:root_bot_buster@localhost:3307/playerdata"

# Create the async engine
engine = create_async_engine(TEST_DB_URL, echo=True)

# Create the session factory
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


@pytest.fixture(scope="session")
async def setup_database():
    """
    Create the test database and drop all tables after the session is done.
    This fixture runs once per test session.
    """
    # Create all tables
    async with engine.connect():
        yield
    await engine.dispose()


@pytest.fixture(scope="function")
@asynccontextmanager
async def session(setup_database):
    """
    Provide a new session for each test function.
    """
    async with AsyncSessionLocal() as session:
        yield session
