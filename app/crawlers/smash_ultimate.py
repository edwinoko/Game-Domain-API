from ..database.models import Game, Character, Archetype, Move
from ..database.setup import get_db
from .ssbu_crawler import get_data
from sqlmodel import select

import logging
import os
import json
import random
from datetime import datetime, date


# Setting up the logger to show state in the terminal
logger = logging.getLogger("uvicorn.info")

# Preparing data file locations to be used to get the smash data
data_files = os.path.join(os.getcwd(),"data/smash_character_data")
archetype_file = os.path.join(os.getcwd(), "data/archetypes")
move_file = os.path.join(os.getcwd(),"data/moves")


# Ensuring that the database is available and can be written to
db_gen = get_db()
db = next(db_gen)


def populate_smash_database():
    
    """
    This is the starting point of retrieving the framedata by going through data folders.
    It logs every step to the terminal and finally returns a statement that everything has
    has been loaded properly.
    """

    # Setting up the basic information for the database
    title = "Super Smash Bros Ultimate"
    ssbu = {"title": title,
            "date": date(2018, 12, 7),
            "information": "Super Smash Bros. Ultimate is a fighting game, namely the fifth computer\
            game in the Super Smash Bros. game series. It was developed by Bandai Namco and Sora\
            Ltd. led by Masahiro Sakurai and published by Nintendo on December 7, 2018 for the Nintendo Switch."}

    # Inserting game title in to 
    logger.info("Inserting game titles...")
    logger.info(setup_titles(ssbu))
    logger.info(setup_titles(ssbu))

    logger.info("Inserting fighting game archetypes...")
    logger.info(setup_archetype())

    logger.info("Inserting characters and moves...")
    logger.info(setup_characters_and_moves(title))

    return "Database has been populated..."

def setup_titles(game_info):

    game_title = Game(
         title=game_info["title"],
         release_date=game_info["date"],
         information=game_info["information"]
    )

    db.add(game_title)
    db.commit()

    return game_info["title"] + " has been added to the database..."


def setup_archetype():
    archetypes = open(archetype_file)
    for archetype in archetypes.readlines():
        if len(str(archetype)) > 4:
            new_archetype = Archetype(
                name = archetype,
                description = "Still need to do this"
                )

            db.add(new_archetype)
            db.commit()

    archetypes.close()

    return "Added the standard archetypes to the database..."


def setup_characters_and_moves(title):

    for character in os.listdir(data_files):
        if not "Identifier" in character:
            updated_character_name = str(character).replace(".json", "").replace("_"," ")

            game_information  = db.exec(select(Game).where(Game.title == title)).first()
            archetypes = db.exec(select(Archetype)).all()

            new_character = Character(
                game_id = game_information.id,
                archetype_id = int(archetypes[random.randrange(0,len(archetypes)-1)].id),
                name = updated_character_name,
                release_date = datetime.now().date(),
                information = "Need to do this"
            )

            db.add(new_character)
            db.commit()

            move_status = setup_moves(character, updated_character_name)
            logger.info(move_status)

    return "Added characters and moves to the database..."


def setup_moves(file, character):
    character_move_file = open(os.path.join(data_files, file))
    character_moves = json.load(character_move_file)
    character_data= db.exec(select(Character).where(Character.name == character)).first()


    for move in character_moves["moves"]:
        move_data = character_moves["moves"][move]
        new_moves = Move(
            name = move_data.get("movename", ""),
            alias = move_data.get("movename", ""),
            startup_frames = move_data.get("startup", ""),
            landing_lag_frames = move_data.get("landinglag", ""),
            character_id = character_data.id,
            duration_frames = move_data.get("totalframes", ""),
            active_frame = move_data.get("activeframes", ""),
            end_active_frame = move_data.get("activeframes", ""), #fix that in data files
            recovery_frames = move_data.get("totalframes", ""), #needs  to be fixed
            start_invincibility_frame = move_data.get("totalframes", ""), #needs to be fixed
            end_invincibility_frame = move_data.get("totalframes", ""), #needs to be fixed
            gif_link = move_data.get("hitbox", ""),
            command_input = move_data.get("totalframes", ""), #needs to be fixed
            damage = move_data.get("basedamage", ""),
            notes = move_data.get("notes", ""),
            shield_lag = move_data.get("shieldlag", ""),
            shield_stun = move_data.get("shieldstun", ""),
            extra_information = move_data.get("notes", ""),
        )
        db.add(new_moves)
        db.commit()
    

    return "Added moves of "+character+ " to the database..."
