import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from osrs_bot_detector_db.database import get_db
from osrs_bot_detector_db.models.player import Player
from osrs_bot_detector_db.repositories.player_repository import PlayerRepository
from osrs_bot_detector_db.schemas.player import (
    PlayerCreate,
    PlayerResponse,
    PlayerUpdate,
)


@pytest.fixture
def player_repository(db_session: AsyncSession):
    return PlayerRepository(db_session=db_session)


@pytest.mark.asyncio
async def test_create_player(
    player_repository: PlayerRepository, db_session: AsyncSession
):
    player_create = PlayerCreate(
        name="Test_Player",
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
    async with db_session() as session:
        result = await session.execute(
            select(Player).where(Player.name == "Test_Player")
        )
        player = result.scalar_one_or_none()
    assert player is not None
    assert player.name == "Test_Player"


@pytest.mark.asyncio
async def test_get_player_by_id(
    player_repository: PlayerRepository, db_session: AsyncSession
):
    player_create = PlayerCreate(
        name="Test_Player",
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
    async with db_session() as session:
        result = await session.execute(
            select(Player).where(Player.name == "Test_Player")
        )
        player = result.scalar_one()
        player_id = player.id
    player_response = await player_repository.get(player_id=player_id)
    assert player_response is not None
    assert isinstance(player_response, PlayerResponse)
    assert player_response.name == "Test_Player"


@pytest.mark.asyncio
async def test_update_player(
    player_repository: PlayerRepository, db_session: AsyncSession
):
    player_create = PlayerCreate(
        name="Test_Player",
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
    async with db_session() as session:
        result = await session.execute(
            select(Player).where(Player.name == "Test_Player")
        )
        player = result.scalar_one()
        player_id = player.id
    player_update = PlayerUpdate(name="Updated_Player")
    await player_repository.update(player_id=player_id, player_update=player_update)
    updated_player_response = await player_repository.get(player_id=player_id)
    assert updated_player_response.name == "Updated_Player"


@pytest.mark.asyncio
async def test_delete_player(
    player_repository: PlayerRepository, db_session: AsyncSession
):
    player_create = PlayerCreate(
        name="Test_Player",
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
    async with db_session() as session:
        result = await session.execute(
            select(Player).where(Player.name == "Test_Player")
        )
        player = result.scalar_one()
        player_id = player.id
    await player_repository.delete(player_id=player_id)
    deleted_player_response = await player_repository.get(player_id=player_id)
    assert deleted_player_response is None
