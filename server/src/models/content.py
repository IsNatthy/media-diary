# Modelo Content - Clase base abstracta para Movie y Series (herencia polimórfica)
from sqlalchemy import Column, Integer, String, ForeignKey
from src.config.database import Base

class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    type = Column(String) # 'movie' or 'series'
    status = Column(String) # 'pending', 'watching', 'completed', 'dropped'
    rating = Column(Integer, default=0)
    review = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    description = Column(String, nullable=True)
    
    # Foreign key to user (Library ownership)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Polymorphic configuration
    __mapper_args__ = {
        "polymorphic_identity": "content",
        "polymorphic_on": type
    }

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "type": self.type,
            "status": self.status,
            "rating": self.rating,
            "review": self.review,
            "poster": self.image_url, # Frontend expects 'poster'
            "description": self.description,
            "user_id": self.user_id
        }