from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from loguru import logger

from backend.settings import postgres_db_url

engine = None
SessionLocal: sessionmaker | None = None


def init_postgres():
    logger.debug(f"Initializing Postgres database with URL: {postgres_db_url}")
    global engine, SessionLocal
    engine = create_engine(postgres_db_url)
    SessionLocal = sessionmaker(bind=engine)
    if SessionLocal is None:
        logger.error("Postgres database initialization failed")


def get_db_session():
    if SessionLocal is None:
        logger.error("Postgres database session not initialized")
        return None
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
