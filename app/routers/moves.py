from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
 
from ..database import setup
from ..crud_ops.move import get_move, get_all_moves, create_move, update_move, delete_move
from ..crud_ops.character import get_character_by_name
from ..database.schemas import Move

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

@router.post("/new")
async def create_moves(move: Move, db: Session = Depends(get_db)):
    move_state =  create_move(db, move)
    return move_state

@router.delete("/delete")
async def delete_moves(move: Move, db: Session = Depends(get_db)):
    move_state =  delete_move(db, move)
    return move_state

@router.put("/update")
async def update_moves(old_move: Move, new_move: Move, db: Session = Depends(get_db)):
    move_state =  update_move(db, old_move, new_move)
    return move_state