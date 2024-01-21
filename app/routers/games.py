from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import setup
from ..crud_ops.game import get_games, get_game_by_id

get_db = setup.get_db
router = APIRouter()

@router.get("/")
async def get_all_games(db: Session = Depends(get_db)):
    games = get_games(db)
    return games

@router.get("/{id}")
async def get_game(id: int, db: Session = Depends(get_db)):
    game = get_game_by_id(db,id)
    return game
