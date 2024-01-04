from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import crud, setup

get_db = setup.get_db
router = APIRouter()

@router.get("/")
async def get_all_characters(db: Session = Depends(get_db)):
    characters = crud.get_all_characters(db)
    return characters

@router.get("/{id}")
async def get_character(id: int, db: Session = Depends(get_db)):
    character = crud.get_character_by_id(db,id)
    return character
