import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from osrs_bot_detector_db.repositories.player_repository import PlayerRepository
from osrs_bot_detector_db.schemas.player import PlayerCreate


@pytest.mark.asyncio
async def test_create_player(session: AsyncSession):
    async with session as db_session:
        player_repository = PlayerRepository(db_session=db_session)
        player_create = PlayerCreate(
            name=f"Test_Player_{str(uuid.uuid4())[-4:]}",
            possible_ban=False,
            confirmed_ban=False,
            confirmed_player=True,
            label_id=1,
            label_jagex=2,
            ironman=False,
            hardcore_ironman=False,
            ultimate_ironman=False,
            normalized_name="test player",
        )

        await player_repository.create(player_create)
