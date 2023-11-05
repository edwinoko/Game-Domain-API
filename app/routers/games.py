from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
 
from ..database import crud, models, schemas, setup

get_db = setup.get_db

router = APIRouter()


@router.get("/", response_model=schemas.Game)
async def get_all_games(db: Session = Depends(get_db)):
    games = crud.get_games(db)
        
    return games

@router.get("/{id}", response_model=schemas.Game)
async def get_game(id: int, db: Session = Depends(get_db)):
    
    pass