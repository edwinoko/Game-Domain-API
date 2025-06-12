from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import setup
from ..database.models import Game


get_db = setup.get_db
router = APIRouter()

@router.get("/")
async def get_all_games(db: Session = Depends(get_db)):
    games = db.exec(select(Game)).all()
    return games

@router.get("/{id}")
async def get_game(id: int, db: Session = Depends(get_db)):
    game = db.get(Game, id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.post("/new")
async def create_game(game: Game, db: Session = Depends(get_db)):
    game.id = None  # Ensure id is not set, so DB will auto-increment
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

@router.delete("/delete/{id}")
async def delete_game(id: int, db: Session = Depends(get_db)):
    game = db.get(Game, id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(game)
    db.commit()
    return {"detail": "Game deleted"}

@router.put("/update/{id}")
async def update_game(id: int, updated_game: Game, db: Session = Depends(get_db)):
    game = db.get(Game, id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    game_data = updated_game.dict(exclude_unset=True)
    for key, value in game_data.items():
        setattr(game, key, value)
    db.add(game)
    db.commit()
    db.refresh(game)
    return game
