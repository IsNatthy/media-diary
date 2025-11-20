# ContentRepository - Queries de contenido (find_by_user, create, update, delete)

from app.src.repository.base_repository import BaseRepository
from app.src.models.content import Content

class ContentRepository(BaseRepository):

    def get_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, genre, year, type, state  * FROM content")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_by_id(self, content_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, genre, year, type, state * FROM content WHERE id = ?", (content_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def find_by_user(self, user_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, genre, year, type, state * FROM content WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def create(self, content: Content, user_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO content (title, year, type, genre, state, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (content.title, content.year, content.type, content.genre, content.state, user_id))
        conn.commit()
        conn.close()
    
    def update(self, content_id, data):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE content
            SET state = ?
            WHERE id = ?
        ''', (data['state'], content_id))
        conn.commit()
        conn.close()

    def delete(self, content_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM content WHERE id = ?', (content_id,))
        conn.commit()
        conn.close()