from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import setup
from ..crud_ops.archetype import get_all_archetypes, get_archetype_by_id, create_archetype, delete_archetype, update_archetype
from ..crud_ops.character import get_character_by_archetype
from ..database.schemas import Archetype

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

@router.post("/new")
async def create_archetypes(archetype: Archetype, db: Session = Depends(get_db)):
    archetype_state =  create_archetype(db, archetype)
    return archetype_state

@router.delete("/delete")
async def delete_archetypes(archetype: Archetype, db: Session = Depends(get_db)):
    archetype_state =  delete_archetype(db, archetype)
    return archetype_state

@router.put("/update")
async def update_archetypes(old_archetype: Archetype, new_archetype, db: Session = Depends(get_db)):
    archetype_state =  update_archetype(db, old_archetype, new_archetype)
    return archetype_state