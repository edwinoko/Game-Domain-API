from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import setup
from ..database.models import Move, Character

get_db = setup.get_db
router = APIRouter()

@router.get("/{id}")
async def get_move(id: int, db: Session = Depends(get_db)):
    move = db.get(Move, id)
    if not move:
        raise HTTPException(status_code=404, detail="Move not found")
    return move

@router.get("/character/{name}")
async def get_all_moves(name: str, db: Session = Depends(get_db)):
    character = db.exec(select(Character).where(Character.name == name)).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    moves = db.exec(select(Move).where(Move.character_id == character.id)).all()
    return moves

@router.post("/new")
async def create_move(move: Move, db: Session = Depends(get_db)):
    db.add(move)
    db.commit()
    db.refresh(move)
    return move

@router.delete("/delete/{id}")
async def delete_move(id: int, db: Session = Depends(get_db)):
    move = db.get(Move, id)
    if not move:
        raise HTTPException(status_code=404, detail="Move not found")
    db.delete(move)
    db.commit()
    return {"detail": "Move deleted"}

@router.put("/update/{id}")
async def update_move(id: int, updated_move: Move, db: Session = Depends(get_db)):
    move = db.get(Move, id)
    if not move:
        raise HTTPException(status_code=404, detail="Move not found")
    move_data = updated_move.dict(exclude_unset=True)
    for key, value in move_data.items():
        setattr(move, key, value)
    db.add(move)
    db.commit()
    db.refresh(move)
    return move