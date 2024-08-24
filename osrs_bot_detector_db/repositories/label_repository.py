from typing import Any, Dict, Type

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.label import Label as LabelTable
from ..schemas.label import LabelCreate, LabelResponse, LabelUpdate
from .crud import CRUD


class LabelRepository(CRUD):
    def __init__(self, db_session: AsyncSession):
        """
        Label class constructor, initializing with the LabelTable model and session.
        :param db_session: Asynchronous database session factory
        """
        super().__init__(LabelTable, db_session)

    def _convert_to_kwargs(self, model: BaseModel) -> Dict[str, Any]:
        """
        Convert a Pydantic model to a dictionary of keyword arguments.
        :param model: Pydantic model
        :return: Dictionary of keyword arguments
        """
        return model.model_dump(exclude_none=True, exclude_unset=True)

    async def create(self, model: LabelCreate) -> LabelTable:
        """
        Asynchronously create a new record using a Pydantic model.
        :param model: Pydantic model for creation
        :return: Created LabelTable instance
        """
        kwargs = model.model_dump(exclude_none=True, exclude_unset=True)
        return await super().create(**kwargs)

    async def request(self, limit: int = 100, **kwargs) -> LabelTable:
        """
        Asynchronously read a record based on provided field(s).
        :param kwargs: Field name(s) and value(s) to filter by
        :return: LabelTable instance or None
        """
        labels = await super().request(limit=limit, **kwargs)
        print(labels)
        return [LabelResponse(**l) for l in labels]

    async def update(self, id_value: int, model: LabelUpdate) -> LabelTable:
        """
        Asynchronously update a record using a Pydantic model.
        :param id_value: ID of the record to update
        :param model: Pydantic model with updated values
        :return: Updated LabelTable instance
        """
        kwargs = self._convert_to_kwargs(model)
        return await super().update(id_value, **kwargs)

    async def delete(self, id_value: int) -> bool:
        """
        Asynchronously delete a record by ID.
        :param id_value: ID of the record to delete
        :return: Boolean indicating success
        """
        return await super().delete(id_value)
