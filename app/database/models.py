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
    startup_frames = Column(Integer)
    landing_lag_frames = Column(Integer)
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
    damage = Column(Integer)
    notes = Column(String)
    shield_lag = Column(Integer)
    shield_stun = Column(Integer)
    extra_information = Column(String)

    character = relationship("Character", back_populates="moves")

class Archetype(Base):
    __tablename__ = "archetype"

    id = Column(Integer, primary_key=True, index=True)
    archetype_name = Column(String, unique=True, index=True)
    description = Column(String)

    character = relationship("Character", back_populates="archetypes")