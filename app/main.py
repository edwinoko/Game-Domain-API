from fastapi import FastAPI
from .routers import archetypes, games, moves, characters
from .database.populate_database import populate_database
from fastapi.middleware.cors import CORSMiddleware
import logging

# Setting up a logger to show database processes in the terminal.
logger = logging.getLogger("uvicorn.info")

# Starting up FastApi.
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Populating the database with games loaded in populate_database.
# If the database is already loaded this step is skipped.
logger.info("Populating the database....")
status = populate_database()
logger.info(status)

# Setting up the routers based on fighting game categories.
app.include_router(archetypes.router, prefix="/archetypes")
app.include_router(games.router, prefix="/games")
app.include_router(moves.router, prefix="/moves")
app.include_router(characters.router, prefix="/characters")
