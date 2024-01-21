from sqlalchemy.orm import Session
from ..database.models import Character

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
