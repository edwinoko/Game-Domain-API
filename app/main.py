from fastapi import Depends, FastAPI

from .database.setup import engine, Base
from .routers import archetypes, games, moves, characters

Base.metadata.create_all(bind=engine)

app = FastAPI()


#app.include_router(archetypes.router, prefix="/archetypes")
app.include_router(games.router, prefix="/games")
#app.include_router(moves.router, prefix="/admin")
#app.include_router(characters.router, prefix="/admin")