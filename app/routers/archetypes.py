from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import setup
from ..database.models import Archetype, Character

get_db = setup.get_db
router = APIRouter()

@router.get("/")
async def get_all_archetypes(db: Session = Depends(get_db)):
    archetypes = db.exec(select(Archetype)).all()
    return archetypes

@router.get("/{id}")
async def get_archetype(id: int, db: Session = Depends(get_db)):
    archetype = db.get(Archetype, id)
    if not archetype:
        raise HTTPException(status_code=404, detail="Archetype not found")
    characters = db.exec(select(Character).where(Character.archetype_id == archetype.id)).all()
    return {"archetype": archetype, "characters": characters}

@router.post("/new")
async def create_archetype(archetype: Archetype, db: Session = Depends(get_db)):
    db.add(archetype)
    db.commit()
    db.refresh(archetype)
    return archetype

@router.delete("/delete/{id}")
async def delete_archetype(id: int, db: Session = Depends(get_db)):
    archetype = db.get(Archetype, id)
    if not archetype:
        raise HTTPException(status_code=404, detail="Archetype not found")
    db.delete(archetype)
    db.commit()
    return {"detail": "Archetype deleted"}

@router.put("/update/{id}")
async def update_archetype(id: int, updated_archetype: Archetype, db: Session = Depends(get_db)):
    archetype = db.get(Archetype, id)
    if not archetype:
        raise HTTPException(status_code=404, detail="Archetype not found")
    archetype_data = updated_archetype.dict(exclude_unset=True)
    for key, value in archetype_data.items():
        setattr(archetype, key, value)
    db.add(archetype)
    db.commit()
    db.refresh(archetype)
    return archetype