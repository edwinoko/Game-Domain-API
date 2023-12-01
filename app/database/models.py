from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.database.setup import Base
from sqlalchemy.orm import relationship


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    release_date = Column(DateTime)
    information = Column(String)

    character = relationship("Character", back_populates="games")

# Combination of game ID and name should be the unique  constraint. Still need to figure out how to fix this

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("game.id"))
    archetype_id = Column(Integer, ForeignKey("archetype.id"))
    name = Column(String)
    release_date = Column(DateTime)
    information = Column(String)

    games = relationship("Game", back_populates="character")
    archetypes = relationship("Archetype", back_populates="character")
    moves = relationship("Move", back_populates="character")

class Move(Base):
    __tablename__ = "move"

    id = Column(Integer, primary_key=True, index=True)
    move_name = Column(String)
    move_alias = Column(String)
    startup_frames = Column(String)
    landing_lag_frames = Column(String)
    character_id = Column(Integer, ForeignKey("character.id"))
    move_duration_frames = Column(String)
    active_frame = Column(String)
    end_active_frame = Column(String)
    recovery_frames = Column(String)
    start_invincibility_frame = Column(String)
    end_invincibility_frame = Column(String)
    move_gif_link = Column(String)
    move_input = Column(String)
    damage = Column(String)
    notes = Column(String)
    shield_lag = Column(String)
    shield_stun = Column(String)
    extra_information = Column(String)

    character = relationship("Character", back_populates="moves")

class Archetype(Base):
    __tablename__ = "archetype"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    character = relationship("Character", back_populates="archetypes")