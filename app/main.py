from fastapi import FastAPI
from .routers import archetypes, games, moves, characters
from .database.populate_database  import populate_database
import logging

logger = logging.getLogger("uvicorn.info")

app = FastAPI()

logger.info("Populating the database....")
status = populate_database()
logger.info(status)

app.include_router(archetypes.router, prefix="/archetypes")
app.include_router(games.router, prefix="/games")
app.include_router(moves.router, prefix="/moves")
app.include_router(characters.router, prefix="/characters")
