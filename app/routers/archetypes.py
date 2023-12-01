from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.models import Game, Archetype, Move, Character
 
from ..database import crud, setup

get_db = setup.get_db

router = APIRouter()

@router.get("/")
async def get_all_archetypes(db: Session = Depends(get_db)):
    archetypes = crud.get_all_archetypes(db)
    return archetypes

@router.get("/{id}")
async def get_archetype(id: int, db: Session = Depends(get_db)):
    archetype = crud.get_archetype_by_id(db,id)
    characters_based_on_archetype = crud.get_character_by_archetype(db, archetype.id)
    return characters_based_on_archetype
