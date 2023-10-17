from typing import Union
from datetime import datetime
from pydantic import BaseModel


class Game(BaseModel):
    id: int
    release_date = datetime
    information: str

    class Config:
        orm_mode = True

class Character(BaseModel):
    id: int
    game_id: int
    archetype_id: int
    name: str
    release_date = datetime
    information: str

    class Config:
        orm_mode = True

class Move(BaseModel):
    id: int
    move_name: str
    move_alias: str
    character_id: int
    move_duration_frames: int
    active_frame: int
    end_active_frame: int
    recovery_frames: int
    start_invincibility_frame: int
    end_invincibility_frame: int
    move_gif_link: str
    move_input: str
    extra_information: str

    class Config:
        orm_mode = True

class Archetype(BaseModel):
    id: int
    game_name: str
    release_date: datetime
    information: str

    class Config:
        orm_mode = True