from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
 
from ..database import setup
from ..crud_ops.move import get_move, get_all_moves
from ..crud_ops.character import get_move, get_character_by_name

get_db = setup.get_db
router = APIRouter()

@router.get("/{id}")
async def get_move(id: int, db: Session = Depends(get_db)):
    move = get_move(db,id)
    return move

@router.get("/character/{name}")
async def get_all_moves(name: str, db: Session = Depends(get_db)):
    character = get_character_by_name(db, name)
    moves = get_all_moves(db, character.id)
    return moves
