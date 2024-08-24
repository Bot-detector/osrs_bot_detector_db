import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from osrs_bot_detector_db.repositories.label_repository import LabelRepository
from osrs_bot_detector_db.schemas.label import LabelCreate


@pytest.mark.asyncio
async def test_create_label(session: AsyncSession):
    async with session as db_session:
        label_repo = LabelRepository(db_session=db_session)
        label_create = LabelCreate(label="tester")

        await label_repo.create(label_create)
