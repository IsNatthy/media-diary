# AuthService - Lógica de negocio para autenticación
from sqlalchemy.orm import Session
from src.repositories.user_repository import UserRepository
from src.models.user import User

import re

class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, username, email, password):
        # Validations
        if not username or len(username) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
            
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Formato de email inválido")
            
        if not password or len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")

        # Normalize email
        email = email.lower()

        # Check if user exists
        if self.user_repository.find_by_username(username):
            raise ValueError("El nombre de usuario ya existe")
        
        if self.user_repository.find_by_email(email):
            raise ValueError("El email ya está registrado")
            
        # Create user (password in plain text as requested)
        new_user = User(username=username, email=email, password=password)
        return self.user_repository.create(new_user)

    def login(self, email, password):
        if not email or not password:
            return None
            
        email = email.lower()
        user = self.user_repository.find_by_email(email)
        if not user:
            return None
            
        # Simple password check (plain text)
        if user.password == password:
            return user
            
        return None
