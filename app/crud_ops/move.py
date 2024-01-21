from sqlalchemy.orm import Session
from ..database.models import Move

def get_all_moves(db: Session, character_id: int ,skip: int = 0, limit: int = 100):
    return db.query(Move).filter(Move.character_id == character_id).offset(skip).limit(limit)

def get_move(db: Session, move_id: int): 
    return db.query(Move).filter(Move.id == move_id).first()

def create_move(db: Session, move: Move):
    return f'Move {move.name} has been created'

def delete_move(db: Session, move: Move):
    return f'Move {move.name} has been deleted'

def update_move(db: Session, old_move, new_move):
    return f'{old_move.name} has been updated to {new_move.name}'