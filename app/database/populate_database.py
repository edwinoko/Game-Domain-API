from ..crawlers.smash_ultimate import populate_smash_database
from ..crawlers.guilty_gear_strive import populate_guilty_gear_database
from ..crawlers.street_fighter_6 import populate_street_fighter_6_database
from ..crawlers.tekken_8 import populate_tekken_8_database
import logging

# Get logger for logging database setup process
logger = logging.getLogger("uvicorn.info")


def populate_database():

    """
    Using the crawler to get information to populate the database with and
    sending the final state back to the main.
    """ 

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
