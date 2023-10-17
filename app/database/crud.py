from sqlalchemy.orm import Session

from . import models, schemas

def get_games(db: Session, game_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.game).offset(skip).limit(limit).all()

def get_game(db: Session, game_id: int):
    return db.query(models.game).filter(models.game.id == game_id).first()

def get_all_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.character).offset(skip).limit(limit).all()

def get_character(db: Session, character_id: int):
    return db.query(models.character).filter(models.character.id == character_id).first()

def get_all_moves(db: Session, character_id: int ,skip: int = 0, limit: int = 100):
    return db.query(models.move).offset(skip).limit(limit).all().filter(models.move.character_id == character_id)

def get_move(db: Session, move_id: int):
    return db.query(models.move).filter(models.move.id == move_id).first()

