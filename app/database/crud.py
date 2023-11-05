from sqlalchemy.orm import Session
from .models import Game, Archetype, Move, Character
from datetime import datetime


def get_games(db: Session, skip: int = 0, limit: int = 100):

    games = db.query(Game).offset(skip).limit(limit).all()

    if len(games) == 0:
        games = create_dummy(Game, db)
        return games

    return games

def create_dummy(model_name, db):
     
    new_entry = model_name(
         id=1,
         title="super smeshy bros",
         release_date=datetime.now().date(),
         information="This is the first game "
    )

    db.add(new_entry)
    db.commit()

    return new_entry


def get_game(db: Session, game_id: int):
    return db.query(Game).filter(Game.id == game_id).first()

def get_all_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Character).offset(skip).limit(limit).all()

#Picking the first from the list wont necessarily work
def get_character(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()

def get_all_moves(db: Session, character_id: int ,skip: int = 0, limit: int = 100):
    return db.query(Move).offset(skip).limit(limit).filter(Move.character_id == character_id)

#Picking the first from the list wont necessarily work
def get_move(db: Session, move_id: int):
    return db.query(Move).filter(Move.id == move_id).first()

def get_all_archetypes(db: Session ,skip: int = 0, limit: int = 100):
    return db.query(Archetype).offset(skip).limit(limit).all()

def get_move(db: Session, archetype_id: int):
    return db.query(Archetype).filter(Archetype.id == archetype_id).first()

