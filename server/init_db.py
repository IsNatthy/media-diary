# Script para crear/resetear la base de datos y todas las tablas
from src.config.database import init_db

if __name__ == '__main__':
    print("Initializing database...")
    init_db()
    print("Database initialized successfully.")