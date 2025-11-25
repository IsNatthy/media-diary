# ContentRepository - Queries de contenido (find_by_user, create, update, delete)
from sqlalchemy.orm import Session
from src.models.content import Content
from src.models.movie import Movie
from src.models.series import Series

class ContentRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_user(self, user_id: int):
        return self.db.query(Content).filter(Content.user_id == user_id).all()

    def find_by_id(self, content_id: int):
        return self.db.query(Content).filter(Content.id == content_id).first()
    
    def create(self, content: Content):
        self.db.add(content)
        self.db.commit()
        self.db.refresh(content)
        return content
    
    def update(self, content: Content):
        self.db.commit()
        self.db.refresh(content)
        return content

    def delete(self, content: Content):
        self.db.delete(content)
        self.db.commit()