from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import setup
from ..crud_ops.character import get_all_characters, get_character_by_id

get_db = setup.get_db
router = APIRouter()

@router.get("/")
async def get_all_characters(db: Session = Depends(get_db)):
    characters = get_all_characters(db)
    return characters

@router.get("/{id}")
async def get_character(id: int, db: Session = Depends(get_db)):
    character = get_character_by_id(db,id)
    return character
