# Modelo Movie - Película, hereda de Content (campos: genre, duration)

from server.src.models.content import Content

class Movie(Content):
    def __init__(self, id, title, year, type, genre, state, duration):
        super().__init__(id, title, year, "movies", genre, state)
        self.duration = duration