from sqlalchemy.orm import Session
from ..database.models import Game

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
