# Script para crear/resetear la base de datos y todas las tablas

import sqlite3
import os

DB_PATH = 'app/src/config/database.db'

def init_db():
    # Ensure directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Content table
    # Merging Movie and Series fields into one table for simplicity as per repository usage
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            type TEXT,
            genre TEXT,
            state TEXT,
            user_id INTEGER,
            duration INTEGER,
            current_season INTEGER,
            current_episode INTEGER,
            total_episodes INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Reviews table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id INTEGER,
            user_id INTEGER,
            rating INTEGER,
            comment TEXT,
            FOREIGN KEY (content_id) REFERENCES content (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()