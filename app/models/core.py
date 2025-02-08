from database import engine
from models import metadata


def create_tables():
    metadata.drop_all(engine)
    metadata.create_all(engine)
