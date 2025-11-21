# CatalogService - Gestión de catálogo predefinido de películas/series

from server.src.repositories.content_repository import ContentRepository

class CatalogService:
    def __init__(self):
        self.repo = ContentRepository()

    def list_content(self):
        return self.repo.get_all()
    
    def get_content(self, content_id):
        return self.repo.get_by_id(content_id)