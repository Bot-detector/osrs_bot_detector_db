import pytest
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from osrs_bot_detector_db.repositories.label_repository import LabelRepository
from osrs_bot_detector_db.schemas.label import LabelCreate, LabelResponse, LabelUpdate


@pytest.mark.asyncio
async def test_create_label(session: AsyncSession):
    label_repo = LabelRepository(db_session=session)
    await label_repo.create(model=LabelCreate(label="Tester"))


@pytest.mark.asyncio
async def test_read_label(session: AsyncSession):
    label_repo = LabelRepository(db_session=session)
    label = await label_repo.request(label="Tester")
    print(f"{label=}")


# @pytest.mark.asyncio
# async def test_update_label(session: AsyncSession):
#     label_crud = LabelRepository(db_session=session)
#     create_model = LabelCreate(label="OldLabel")

#     created_label = await label_crud.create(model=create_model)

#     update_model = LabelUpdate(label="NewLabel")
#     updated_label = await label_crud.update(
#         id_value=created_label.id, model=update_model
#     )

#     assert updated_label is not None
#     assert updated_label.label == "NewLabel"


# @pytest.mark.asyncio
# async def test_delete_label(session: AsyncSession):
#     label_crud = LabelRepository(db_session=session)
#     create_model = LabelCreate(label="DeleteMe")

#     created_label = await label_crud.create(model=create_model)

#     deletion_success = await label_crud.delete(id_value=created_label.id)

#     assert deletion_success is True

#     # Ensure the label is actually deleted
#     try:
#         await label_crud.read(label="DeleteMe")
#         assert False, "Label was not deleted"
#     except Exception:
#         pass
