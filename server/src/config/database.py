# Configuración de SQLAlchemy - engine, Base, SessionLocal, init_db()
# Configuración de SQLAlchemy - engine, Base, SessionLocal, init_db()

import sqlite3

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BD_PATH = os.path.join(BASE_DIR, 'database.db')

class DatabaseConnection:
    @staticmethod
    def connect():
        return sqlite3.connect(BD_PATH)