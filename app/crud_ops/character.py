from sqlalchemy.orm import Session
from ..database.models import Character

def get_all_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Character).offset(skip).limit(limit).all()

def get_character_by_id(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()

def get_character_by_name(db: Session, character_name: int):
    return db.query(Character).filter(Character.name == character_name).first()

def get_character_by_archetype(db: Session, archetype_id: int):
    return db.query(Character).filter(Character.archetype_id == archetype_id).all()

def create_character(db: Session, character):
    return f'character {character.title} has been created'

def delete_character(db: Session, character):
    return f'character {character.title} has been deleted'

def update_character(db: Session, old_character, new_character):
    return f'character {old_character.title} has been updated to {new_character.title}'
