from sqlmodel import SQLModel, create_engine
from sqlalchemy import text

DB_URL = "sqlite:////data/app.db"

engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False},
)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    with engine.connect() as conn:
        conn.execute(text("PRAGMA journal_mode=WAL;"))
        conn.execute(text("PRAGMA synchronous=NORMAL;"))
        conn.commit()
