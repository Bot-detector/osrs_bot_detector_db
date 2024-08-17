from pydantic import BaseModel
from typing import Optional

class PlayerBase(BaseModel):
    name: str
    possible_ban: Optional[bool] = False
    confirmed_ban: Optional[bool] = False
    confirmed_player: Optional[bool] = False
    label_id: Optional[int] = None
    label_jagex: Optional[int] = None
    ironman: Optional[bool] = False
    hardcore_ironman: Optional[bool] = False
    ultimate_ironman: Optional[bool] = False
    normalized_name: Optional[str] = None

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(PlayerBase):
    pass

class PlayerResponse(PlayerBase):
    id: int
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True