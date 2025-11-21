# UserRepository - Queries de usuarios (find_by_username, create, etc.)

from server.src.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):
    def find_by_username(self, username):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        return row

    def find_by_id(self, user_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, password FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        return row
    
    def create(self, username, email, password):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, password))
        conn.commit()
        conn.close()