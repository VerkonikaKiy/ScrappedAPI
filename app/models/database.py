from sqlalchemy import create_engine

from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)
connection = engine.connect()
