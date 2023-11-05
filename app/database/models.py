from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database.setup import Base

class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    release_date = Column(DateTime)
    information = Column(String)

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("game.id"))
    archetype_id = Column(Integer, ForeignKey("archetype.id"))
    name = Column(String)
    release_date = Column(DateTime)
    information = Column(String)

class Move(Base):
    __tablename__ = "move"

    id = Column(Integer, primary_key=True, index=True)
    move_name = Column(String)
    move_alias = Column(String)
    character_id = Column(Integer, ForeignKey("character.id"))
    move_duration_frames = Column(Integer)
    startup_frame = Column(Integer)
    active_frame = Column(Integer)
    end_active_frame = Column(Integer)
    recovery_frames = Column(Integer)
    start_invincibility_frame = Column(Integer)
    end_invincibility_frame = Column(Integer)
    move_gif_link = Column(String)
    move_input = Column(String)
    extra_information = Column(String)

class Archetype(Base):
    __tablename__ = "archetype"

    id = Column(Integer, primary_key=True, index=True)
    archetype_name = Column(String, unique=True, index=True)
    description = Column(String)