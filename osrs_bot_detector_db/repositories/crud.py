from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session


class CRUD:
    def __init__(self, model):
        """
        CRUD class constructor.
        :param model: SQLAlchemy ORM model
        """
        self.model = model

    def create(self, session: Session, **kwargs):
        """
        Create a new record.
        :param session: Database session
        :param kwargs: Field values
        :return: Created model instance
        """
        with session.begin():
            sql = insert(self.model).values(**kwargs).returning(self.model)
            result = session.execute(sql)
            return result.fetchone()

    def read(self, session: Session, **kwargs):
        """
        Read a record based on provided field(s).
        :param session: Database session
        :param kwargs: Field name(s) and value(s) to filter by
        :return: Model instance or None
        """
        if not kwargs:
            raise ValueError("At least one field and value must be provided")

        filters = []
        for field, value in kwargs.items():
            if hasattr(self.model, field):
                filters.append(getattr(self.model, field) == value)
            else:
                raise AttributeError(
                    f"{self.model.__name__} has no attribute '{field}'"
                )

        sql = select(self.model).where(*filters)
        result = session.execute(sql)
        return result.fetchone()

    def update(self, session: Session, id: int, **kwargs):
        """
        Update a record by ID.
        :param session: Database session
        :param id: Model ID
        :param kwargs: Updated field values
        :return: Updated model instance
        """
        with session.begin():
            sql = (
                update(self.model)
                .where(self.model.id == id)
                .values(**kwargs)
                .returning(self.model)
            )
            result = session.execute(sql)
            return result.fetchone()

    def delete(self, session: Session, id: int):
        """
        Delete a record by ID.
        :param session: Database session
        :param id: Model ID
        :return: Boolean indicating success
        """
        with session.begin():
            sql = delete(self.model).where(self.model.id == id).returning(self.model)
            result = session.execute(sql)
            return result.rowcount > 0
