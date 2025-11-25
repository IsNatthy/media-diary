# Modelo User - Usuario del sistema (id, username, password)
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)  # En texto plano como solicitado (no recomendado para prod)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }