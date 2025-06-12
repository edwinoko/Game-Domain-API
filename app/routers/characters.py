from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import setup
from ..database.models import Character

get_db = setup.get_db
router = APIRouter()

@router.get("/")
async def get_all_characters(db: Session = Depends(get_db)):
    characters = db.exec(select(Character)).all()
    return characters

@router.get("/{id}")
async def get_character(id: int, db: Session = Depends(get_db)):
    character = db.get(Character, id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/new")
async def create_character(character: Character, db: Session = Depends(get_db)):
    db.add(character)
    db.commit()
    db.refresh(character)
    return character

@router.delete("/delete/{id}")
async def delete_character(id: int, db: Session = Depends(get_db)):
    character = db.get(Character, id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(character)
    db.commit()
    return {"detail": "Character deleted"}

@router.put("/update/{id}")
async def update_character(id: int, updated_character: Character, db: Session = Depends(get_db)):
    character = db.get(Character, id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    character_data = updated_character.dict(exclude_unset=True)
    for key, value in character_data.items():
        setattr(character, key, value)
    db.add(character)
    db.commit()
    db.refresh(character)
    return character