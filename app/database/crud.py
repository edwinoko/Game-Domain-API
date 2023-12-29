from sqlalchemy.orm import Session
from .models import Game, Archetype, Move, Character

# GAMES
def get_games(db: Session, skip: int = 0, limit: int = 100):
    games = db.query(Game).offset(skip).limit(limit).all()
    return games

def get_game_by_id(db: Session, game_id: int):
    return db.query(Game).filter(Game.id == game_id).first()

def get_game_by_name(db: Session, title: str):
    return db.query(Game).filter(Game.title == title).first()


# CHARACTERS
def get_all_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Character).offset(skip).limit(limit).all()

def get_character_by_id(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()

def get_character_by_name(db: Session, character_name: int):
    return db.query(Character).filter(Character.name == character_name).first()

def get_character_by_archetype(db: Session, archetype_id: int):
    return db.query(Character).filter(Character.archetype_id == archetype_id).all()


# MOVES
def get_all_moves(db: Session, character_id: int ,skip: int = 0, limit: int = 100):
    return db.query(Move).filter(Move.character_id == character_id).offset(skip).limit(limit)

def get_move(db: Session, move_id: int):
    return db.query(Move).filter(Move.id == move_id).first()


# ARCHETYPES
def get_all_archetypes(db: Session ,skip: int = 0, limit: int = 100):
    return db.query(Archetype).offset(skip).limit(limit).all()

def get_archetype_by_id(db: Session, archetype_id: int):
    return db.query(Archetype).filter(Archetype.id == archetype_id).first()

def get_archetype_by_name(db: Session, name: int):
    return db.query(Archetype).filter(Archetype.name == name).first()
