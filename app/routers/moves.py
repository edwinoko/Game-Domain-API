from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
 
from ..database import crud, setup

get_db = setup.get_db

router = APIRouter()

@router.get("/{id}")
async def get_move(id: int, db: Session = Depends(get_db)):
    character = crud.get_character_by_id(db,id)
    return character

@router.get("/character/{name}")
async def get_all_moves(name: str, db: Session = Depends(get_db)):
    character = crud.get_character_by_name(db, name)
    moves = crud.get_all_moves(db, character.id)
    return moves
