from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)
connection = engine.connect()

SessionLocal = sessionmaker(engine, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
