from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
 
from ..database import crud, models, schemas, setup

get_db = setup.get_db

router = APIRouter()

@router.get("/")
async def get_all_games(db: Session = Depends(get_db)):
    games = crud.get_games(db)
    #import pdb; pdb.set_trace()
    return games

@router.get("/{id}")
async def get_game(id: int, db: Session = Depends(get_db)):
    game = crud.get_game(db,id)
    #import pdb; pdb.set_trace()
    return game
