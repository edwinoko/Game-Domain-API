from sqlalchemy.orm import Session
from ..database.models import Game

def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Game).offset(skip).limit(limit).all()

def get_game_by_id(db: Session, game_id: int):
    return db.query(Game).filter(Game.id == game_id).first()

def get_game_by_name(db: Session, title: str):
    return db.query(Game).filter(Game.title == title).first()

def create_game(db: Session, game):
    return f'Game {game.title} has been created'

def delete_game(db: Session, game):
    return f'Game {game.title} has been deleted'

def update_game(db: Session, old_game, new_game):
    return f'Game {old_game.title} has been updated to {new_game.title}'