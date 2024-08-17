from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.player import Player
from ..schemas.player import PlayerCreate, PlayerResponse, PlayerUpdate
from ..utils import helpers


class PlayerRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = Player

    async def get(
        self, player_id: int = None, player_name: str = None
    ) -> PlayerResponse:
        sql = select(self.model)

        if player_id:
            sql = sql.where(self.model.id == player_id)
        elif player_name:
            player_name = helpers.to_jagex_name(name=player_name)
            sql = sql.where(self.model.name == player_name)
        else:
            raise Exception("either player_id or player_name must be given")

        async with self.db_session() as session:
            session: AsyncSession
            async with session.begin():
                result = await session.execute(sql)
                player = result.mappings().first()
        if not player:
            return None
        return PlayerResponse(**player)

    async def create(self, player_create: PlayerCreate) -> None:
        sql = insert(self.model).values(player_create.model_dump())
        async with self.db_session() as session:
            session: AsyncSession
            async with session.begin():
                _ = await session.execute(sql)
                await session.commit()
        return None

    async def update(self, player_id: int, player_update: PlayerUpdate) -> None:
        sql = (
            update(self.model)
            .where(self.model.id == player_id)
            .values(player_update.model_dump())
        )
        async with self.db_session() as session:
            session: AsyncSession
            async with session.begin():
                await session.execute(sql)
                await session.commit()
        return None

    async def delete(self, player_id: int) -> None:
        sql = delete(self.model).where(self.model.id == player_id)
        async with self.db_session() as session:
            session: AsyncSession
            async with session.begin():
                await session.execute(sql)
        return None
