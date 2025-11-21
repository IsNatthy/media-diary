# Configuración de SQLAlchemy - engine, Base, SessionLocal, init_db()
# Configuración de SQLAlchemy - engine, Base, SessionLocal, init_db()

import sqlite3

BD_PATH = 'app/src/config/database.db'

class DatabaseConnection:
    @staticmethod
    def connect():
        return sqlite3.connect(BD_PATH)