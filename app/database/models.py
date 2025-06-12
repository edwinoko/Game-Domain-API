from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=100)
    release_date: Optional[datetime] = None
    information: Optional[str] = None

class Archetype(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: Optional[str] = None

class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    game_id: Optional[int] = Field(default=None, foreign_key="game.id")
    archetype_id: Optional[int] = Field(default=None, foreign_key="archetype.id")
    name: str = Field(index=True, max_length=100)
    release_date: Optional[datetime] = None
    information: Optional[str] = None

class Move(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    alias: Optional[str] = None
    startup_frames: Optional[str] = None
    landing_lag_frames: Optional[str] = None
    character_id: Optional[int] = Field(default=None, foreign_key="character.id")
    duration_frames: Optional[str] = None
    active_frame: Optional[str] = None
    end_active_frame: Optional[str] = None
    recovery_frames: Optional[str] = None
    start_invincibility_frame: Optional[str] = None
    end_invincibility_frame: Optional[str] = None
    gif_link: Optional[str] = None
    command_input: Optional[str] = None
    damage: Optional[str] = None
    notes: Optional[str] = None
    shield_lag: Optional[str] = None
    shield_stun: Optional[str] = None
    extra_information: Optional[str] = None
    cancellable: Optional[str] = None
