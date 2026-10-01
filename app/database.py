import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from collections.abc import Generator


# Load the environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create the engine
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass
