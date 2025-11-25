# Configuración de SQLAlchemy - engine, Base, SessionLocal, init_db()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Crear directorio de base de datos si no existe
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, 'media_diary.db')
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Importar todos los modelos aquí para que SQLAlchemy los reconozca
    from src.models.user import User
    from src.models.content import Content
    from src.models.movie import Movie
    from src.models.series import Series
    
    Base.metadata.create_all(bind=engine)