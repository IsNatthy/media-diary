from app.src.config.database import DatabaseConnection

class BaseRepository:
    def connect(self):
        return DatabaseConnection.connect()