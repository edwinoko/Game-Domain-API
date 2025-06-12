from ..crawlers.smash_ultimate import populate_smash_database
from ..crawlers.guilty_gear_strive import populate_guilty_gear_database
from ..crawlers.street_fighter_6 import populate_street_fighter_6_database
from ..crawlers.tekken_8 import populate_tekken_8_database
from .models import Game, Character, Archetype, Move
from .setup import get_db
import logging
import os

# Get logger for logging database setup process
logger = logging.getLogger("uvicorn.info")


def is_database_empty():
    """
    Check if any of the main tables are empty.
    """
    # get_db is a generator, so we need to get the session from it
    db_gen = get_db()
    session = next(db_gen)
    try:
        if (
            session.query(Game).first() is None or
            session.query(Character).first() is None or
            session.query(Archetype).first() is None or
            session.query(Move).first() is None
        ):
            return True
        return False
    finally:
        session.close()

def populate_database():

    """
    Using the crawler to get information to populate the database with and
    sending the final state back to the main.
    """ 
    if is_database_empty():
        # Loading in the smash bros ultimate framedata.
        smash_database_state = populate_smash_database()
        logger.info(smash_database_state)

        # Loading in the Guilty gear framedata
        guilty_gear_strive_state = populate_guilty_gear_database()
        logger.info(guilty_gear_strive_state)
        
        # Loading in the street fighter 6 framedata
        street_fighter_6_state = populate_street_fighter_6_database()
        logger.info(street_fighter_6_state)

        # Loading in the tekken 8 framedata
        tekken_8_state = populate_tekken_8_database()
        logger.info(tekken_8_state)

        return "All databases have been loaded"
    else:
        return "Database already populated, skipping population step"
