# ReviewService - Gestión de comentarios + validación ownership

from server.src.repositories.review_repository import ReviewRepository
from server.src.models.review import Review

class ReviewService:
    def __init__(self):
        self.repo = ReviewRepository()

    def get_reviews_for_content(self, content_id):
        return self.repo.find_by_content(content_id)

    def add_review(self, data):
        review = Review(
            id=None,
            user_id=data["user_id"],
            content_id=data["content_id"],
            rating=data["rating"],
            comment=data["comment"]
        )
        self.repo.create(review)

    def delete_review(self, review_id, user_id):
        # Validar que el usuario es el propietario del comentario antes de eliminar
        # This logic seems flawed (find_by_content(review_id)?). 
        # Should be find_by_id or similar.
        # But keeping original logic structure for now, just fixing imports.
        # Actually, find_by_content likely returns reviews for a content. 
        # If review_id is passed, it's wrong.
        # I'll assume repo has get_by_id or similar.
        # But I don't have ReviewRepository content.
        # I'll stick to fixing imports and syntax errors.
        reviews = self.repo.find_by_content(review_id) # This looks suspicious but I won't change logic too much.
        for rev in reviews:
            if rev[0] == review_id and rev[2] == user_id:  # rev[2] es user_id
                self.repo.delete(review_id)
                return True
        return False