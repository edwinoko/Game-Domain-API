from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import setup
from ..crud_ops.archetype import get_all_archetypes, get_archetype_by_id
from ..crud_ops.character import get_character_by_archetype

get_db = setup.get_db
router = APIRouter()

@router.get("/")
async def get_all_archetypes(db: Session = Depends(get_db)):
    archetypes = get_all_archetypes(db)
    return archetypes

@router.get("/{id}")
async def get_archetype(id: int, db: Session = Depends(get_db)):
    archetype = get_archetype_by_id(db,id)
    characters_based_on_archetype = get_character_by_archetype(db, archetype.id)
    return characters_based_on_archetype
