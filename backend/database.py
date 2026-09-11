from fastapi import HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from backend.config import get_database_url

engine = None
SessionLocal = None


class Base(DeclarativeBase):
    pass


def init_engine():
    global engine, SessionLocal
    if SessionLocal is not None:
        return engine

    url = get_database_url()
    if not url:
        return None

    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    engine = create_engine(url, connect_args=connect_args)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine


def get_db():
    init_engine()
    if SessionLocal is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="SQLALCHEMY_DATABASE_URL is not set",
        )
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
