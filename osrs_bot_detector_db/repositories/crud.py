from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class CRUD:
    def __init__(self, model, db_session: AsyncSession):
        """
        CRUD class constructor.
        :param model: SQLAlchemy ORM model
        :param db_session: Asynchronous database session factory
        """
        self.model = model
        self.db_session = db_session

    async def create(self, **kwargs):
        """
        Asynchronously create a new record.
        :param kwargs: Field values
        :return: Created model instance
        """
        async with self.db_session() as session:
            session: AsyncSession
            async with session.begin():
                sql = insert(self.model).values(**kwargs).returning(self.model)
                result = await session.execute(sql)
                return result.fetchone()

    async def read(self, **kwargs):
        """
        Asynchronously read a record based on provided field(s).
        :param kwargs: Field name(s) and value(s) to filter by
        :return: Model instance or None
        """
        filters = []
        for field, value in kwargs.items():
            if not hasattr(self.model, field):
                raise AttributeError(
                    f"{self.model.__name__} has no attribute '{field}'"
                )
            filters.append(getattr(self.model, field) == value)

        async with self.db_session() as session:
            session: AsyncSession

            sql = select(self.model).where(*filters)
            result = await session.execute(sql)
            return result.fetchone()

    async def update(self, id: int, **kwargs):
        """
        Asynchronously update a record by ID.
        :param id: Model ID
        :param kwargs: Updated field values
        :return: Updated model instance
        """
        async with self.db_session() as session:
            session: AsyncSession
            async with session.begin():
                sql = (
                    update(self.model)
                    .where(self.model.id == id)
                    .values(**kwargs)
                    .returning(self.model)
                )
                result = await session.execute(sql)
                return result.fetchone()

    async def delete(self, id: int):
        """
        Asynchronously delete a record by ID.
        :param id: Model ID
        :return: Boolean indicating success
        """
        async with self.db_session() as session:
            session: AsyncSession
            async with session.begin():
                sql = (
                    delete(self.model).where(self.model.id == id).returning(self.model)
                )
                result = await session.execute(sql)
                return result.rowcount > 0
