from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import Settings

Base = declarative_base()

engine = create_engine(Settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()