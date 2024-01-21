from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import setup
from ..crud_ops.character import get_all_characters, get_character_by_id, create_character, update_character, delete_character
from ..database.schemas import Character


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

@router.post("/new")
async def create_characters(db: Session, character: Character):
    character_state =  create_character(db, character)
    return character_state

@router.delete("/delete")
async def delete_characters(db: Session, character: Character):
    character_state =  delete_character(db, character)
    return character_state

@router.put("/update")
async def update_characters(db: Session, old_character: Character, new_character: Character):
    character_state =  update_character(db, old_character, new_character)
    return character_state