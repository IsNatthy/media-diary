# LibraryService - CRUD de biblioteca personal del usuario + validación ownership

from server.src.repositories.content_repository import ContentRepository
from server.src.models.content import Content

class LibraryService:
    def __init__(self, catalog_service, user_id):
        self.catalog_service = catalog_service
        self.user_id = user_id
        self.content_repo = ContentRepository()

    def get_full_info(self, content_id):
        content = self.catalog_service.get_content(content_id)

        if not content:
            raise ValueError("Content not found")

        return content

    def add_to_library(self, content_id):
        content_data = self.catalog_service.get_content(content_id)
        if not content_data:
             raise ValueError("Content not found")
        
        # Create new content for user based on catalog item
        # Assuming tuple index: 1=title, 2=year, 3=type, 4=genre
        new_content = Content(None, content_data[1], content_data[2], content_data[3], content_data[4], "planned")
        self.content_repo.create(new_content, self.user_id)
        return new_content
        
    def remove_from_library(self, content_id):
        self.content_repo.delete(content_id)

    def list_library(self):
        return self.content_repo.find_by_user(self.user_id)