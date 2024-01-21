from sqlalchemy.orm import Session
from ..database.models import Archetype

def get_all_archetypes(db: Session ,skip: int = 0, limit: int = 100):
    return db.query(Archetype).offset(skip).limit(limit).all()

def get_archetype_by_id(db: Session, archetype_id: int):
    return db.query(Archetype).filter(Archetype.id == archetype_id).first()

def get_archetype_by_name(db: Session, name: int):
    return db.query(Archetype).filter(Archetype.name == name).first()

def create_archetype(db: Session, archetype):
    return f'Archetype {archetype.title} has been created'

def delete_archetype(db: Session, archetype):
    return f'Archetype {archetype.title} has been deleted'

def update_archetype(db: Session, old_archetype, new_archetype):
    return f'Archetype {old_archetype.title} has been updated to {new_archetype.title}'
