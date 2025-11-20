# Modelo Review - Comentarios de usuarios sobre contenido (content_id FK, user_id FK, text)

class Review:
    def __init__(self, id, content_id, user_id, rating, comment):
        self.id = id
        self.content_id = content_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment