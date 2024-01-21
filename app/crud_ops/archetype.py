from sqlalchemy.orm import Session
from ..database.models import Archetype

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
