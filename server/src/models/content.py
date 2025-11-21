# Modelo Content - Clase base abstracta para Movie y Series (herencia polimórfica)

class Content:
    def __init__(self, id, title, year, type, genre, state):
        self.id = id
        self.title = title
        self.year = year
        self.type = type
        self.genre = genre
        self.state = state