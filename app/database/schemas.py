from __future__ import annotations
from datetime import date
from pydantic import BaseModel
from typing import List


class Game(BaseModel):

    id: int 
    title: str
    release_date: date
    information: str
    characters: List[Character] = None
   

    class Config:
       from_attributes = True

class Archetype(BaseModel):
    id: int
    name: str
    description: str
    characters: List[Character] = None

    class Config:
        from_attributes = True

class Move(BaseModel):
    id: int
    move_name: str
    move_alias: list[str]
    startup_frames: str 
    landing_lag_frames: str
    character_id: int
    total_frames: str
    active_frame: str
    end_active_frame: str
    recovery_frames: str
    start_invincibility_frame: str
    end_invincibility_frame: str
    move_gif_link: str
    move_input: str
    damage: str
    notes: str 
    shield_lag: str # how quickly the user can shield after landing a hit on shield
    shield_stun: str # how quickly the opponent can letgo of shield after getting hit
    extra_information: str
    characters: List[Character] = None

    class Config:
        from_attributes = True

class Character(BaseModel):
    id: int
    game_id: int
    archetype_id: int
    name: str
    release_date: date
    information: str
    games: List[Game] = None
    archetypes: List[Archetype] = None
    moves :  List[Move] = None

    class Config:
        from_attributes = True