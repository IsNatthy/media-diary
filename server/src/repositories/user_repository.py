# UserRepository - Queries de usuarios (find_by_username, create, etc.)

from app.src.repository.base_repository import BaseRepository

class UserRepository(BaseRepository):
    def find_by_username(self, username):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, password FROM user WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        return row
    
    def create(self, username, email, password):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO user (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, password))
        conn.commit()
        conn.close()