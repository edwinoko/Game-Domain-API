from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import setup
from ..crud_ops.game import get_games, get_game_by_id, update_game, delete_game, create_game
from ..database.schemas import Game


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

@router.post("/new")
async def create_games(game: Game, db: Session = Depends(get_db)):
    game_state =  create_game(db, game)
    return game_state

@router.delete("/delete")
async def delete_games(game: Game, db: Session = Depends(get_db)):
    game_state =  delete_game(db, game)
    return game_state

@router.put("/update")
async def update_games(old_game: Game, new_game: Game, db: Session = Depends(get_db)):
    game_state =  update_game(db, old_game, new_game)
    return game_state
