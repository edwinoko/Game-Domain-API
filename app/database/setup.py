from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy_utils import database_exists, create_database
from ..crawlers.ssbu_crawler import get_data
import os


# Ensure that database folders are created
database_directory = "data/"
if not os.path.exists(database_directory):
    os.makedirs(database_directory)

# Database setup
DATABASE_URL = "sqlite:///data/sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# Dependency to get the database session
def get_db():
    x = database_exists(DATABASE_URL)
    if database_exists(DATABASE_URL):
        with Session(engine) as session:
            yield session
    else:
        # If the database does not exist, create it and initialize it
        create_database(DATABASE_URL)
        SQLModel.metadata.create_all(engine)

        # Add the character files to the environment
        get_data()
        with Session(engine) as session:
            yield session

