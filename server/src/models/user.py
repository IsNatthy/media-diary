# Modelo User - Usuario del sistema (id, username, password)

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.email = email
        self.password = password