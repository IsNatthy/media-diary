# Modelo Movie - Película, hereda de Content (campos: genre, duration)

from app.src.models.content import Content

class Movie(Content):
    def __init__(self, id, name, year, type, genre, state, duration):
        super().__init__(id, name, year, type="movies", genre, state)
        self.duration = duration