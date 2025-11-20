# ReviewRepository - Queries de comentarios (find_by_content, create, delete)

from app.src.repository.base_repository import BaseRepository
from app.src.models.review import Review

class ReviewRepository(BaseRepository):
    def find_by_content(self, content_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, content_id, user_id, rating, comment FROM review WHERE content_id = ?", (content_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def create(self, review: Review):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO review (content_id, user_id, rating, comment)
            VALUES (?, ?, ?, ?)
        ''', (review.content_id, review.user_id, review.rating, review.comment))
        conn.commit()
        conn.close()
    
    def delete(self, review_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM review WHERE id = ?', (review_id,))
        conn.commit()
        conn.close()