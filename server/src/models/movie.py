# Modelo Movie - Película, hereda de Content (campos: genre, duration)
from sqlalchemy import Column, Integer, ForeignKey
from src.models.content import Content

class Movie(Content):
    __tablename__ = "movies"

    id = Column(Integer, ForeignKey("contents.id"), primary_key=True)
    duration = Column(Integer) # in minutes

    __mapper_args__ = {
        "polymorphic_identity": "movie",
    }

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "duration": self.duration
        })
        return data