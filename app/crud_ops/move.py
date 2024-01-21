from sqlalchemy.orm import Session
from ..database.models import Move

def get_all_moves(db: Session, character_id: int ,skip: int = 0, limit: int = 100):

    """
    Returns all the moves defined in the database. Dont know how useful this is at the time
    of writing so might remove this.
    """

    return db.query(Move).filter(Move.character_id == character_id).offset(skip).limit(limit)


def get_move(db: Session, move_id: int):

    """
    Takes a move id and returns the object related to that move id. 
    """
    
    return db.query(Move).filter(Move.id == move_id).first()