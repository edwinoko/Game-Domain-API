from sqlalchemy.orm import Session
from .models import Game, Archetype, Move, Character

# GAMES
def get_games(db: Session, skip: int = 0, limit: int = 100):

    """
    Get a list of all the game franchises loaded into the database and
    returns them as a list of games.
    """

    return db.query(Game).offset(skip).limit(limit).all()


def get_game_by_id(db: Session, game_id: int):
    
    """
    Takes a game id and looks up what game is linked to that id in the
    database. It then returns that game object.
    """
    
    return db.query(Game).filter(Game.id == game_id).first()

def get_game_by_name(db: Session, title: str):

    """
    Takes the name of the game and returns the game information related to
    that game.
    """

    return db.query(Game).filter(Game.title == title).first()


# CHARACTERS
def get_all_characters(db: Session, skip: int = 0, limit: int = 100):

    """
    Gets a list of all the characters in the database and returns them as
    a list.
    """

    return db.query(Character).offset(skip).limit(limit).all()

def get_character_by_id(db: Session, character_id: int):

    """
    Searches for a character based on id and returns that character object.
    """

    return db.query(Character).filter(Character.id == character_id).first()

def get_character_by_name(db: Session, character_name: int):

    """
    Allows for character details to be looked up based on the name of the character. 
    It will always return one character. (regardles of game franchise)
    """

    return db.query(Character).filter(Character.name == character_name).first()

def get_character_by_archetype(db: Session, archetype_id: int):

    """
    Searches for all characters related to a specific archetype. It returns a list
    of characters that are related to that archetype.
    """

    return db.query(Character).filter(Character.archetype_id == archetype_id).all()


# MOVES
def get_all_moves(db: Session, character_id: int ,skip: int = 0, limit: int = 100):

    """
    Returns all the moves defined in the database. Dont know how useful this is at the time
    of writing so might remove this.
    """

    return db.query(Move).filter(Move.character_id == character_id).offset(skip).limit(limit)

def get_move(db: Session, move_id: int):

    """
    Takes a move id and returns the object related to that move id. 
    """

    return db.query(Move).filter(Move.id == move_id).first()


# ARCHETYPES
def get_all_archetypes(db: Session ,skip: int = 0, limit: int = 100):

    """
    Give back a list of all archetypes found in the database.
    """

    return db.query(Archetype).offset(skip).limit(limit).all()

def get_archetype_by_id(db: Session, archetype_id: int):

    """
    Takes a archetype id and returns the object related to that ID.
    """

    return db.query(Archetype).filter(Archetype.id == archetype_id).first()

def get_archetype_by_name(db: Session, name: int):

    """
    Takes a name and returns all archetype information related to that name.
    """

    return db.query(Archetype).filter(Archetype.name == name).first()
