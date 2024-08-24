from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect


class CRUD:
    def __init__(self, model, db_session: AsyncSession):
        """
        CRUD class constructor.
        :param model: SQLAlchemy ORM model
        :param db_session: Asynchronous database session factory
        """
        self.model = model
        self.db_session = db_session

    def _get_primary_key_column(self):
        """
        Get the primary key column of the model.
        :return: Primary key column object
        """
        mapper = inspect(self.model)
        if not mapper.primary_key:
            raise AttributeError(f"{self.model.__name__} does not have a primary key")
        return mapper.primary_key[0]

    async def create(self, **kwargs):
        """
        Asynchronously create a new record.
        :param kwargs: Field values
        :return: Created model instance
        """
        async with self.db_session.begin():
            sql = insert(self.model).values(**kwargs).prefix_with("ignore")
            _ = await self.db_session.execute(sql)
            await self.db_session.commit()

    async def request(self, limit: int, **kwargs):
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

        sql = select(self.model).where(*filters).limit(limit)
        result = await self.db_session.execute(sql)
        return result.mappings().all()  # i don't understand why this is not good

    async def update(self, id_value, **kwargs):
        """
        Asynchronously update a record by ID.
        :param id_value: Value of the primary key
        :param kwargs: Updated field values
        :return: Updated model instance
        """
        primary_key_column = self._get_primary_key_column()
        async with self.db_session.begin():
            sql = (
                update(self.model)
                .where(primary_key_column == id_value)
                .values(**kwargs)
            )
            _ = await self.db_session.execute(sql)
            await self.db_session.commit()

    async def delete(self, id_value):
        """
        Asynchronously delete a record by ID.
        :param id_value: Value of the primary key
        :return: Boolean indicating success
        """
        primary_key_column = self._get_primary_key_column()
        async with self.db_session.begin():
            sql = delete(self.model).where(primary_key_column == id_value)
            _ = await self.db_session.execute(sql)
            await self.db_session.commit()
