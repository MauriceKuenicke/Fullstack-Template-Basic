import os

from sqlalchemy import create_engine, NullPool, Engine

def get_backend_db_url():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    host = os.getenv("DB_HOST")
    return f"postgresql://{user}:{password}@{host}:5432/{db_name}"

def get_backend_db_engine() -> Engine:
    engine = create_engine(get_backend_db_url(),
                           echo=False,
                           pool_pre_ping=True,
                           poolclass=NullPool)
    return engine