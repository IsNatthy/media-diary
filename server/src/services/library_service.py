# LibraryService - CRUD de biblioteca personal del usuario + validación ownership

class LibraryService:
    def __init__(self, catalog_service, user_id):
        self.catalog_service = catalog_service
        self.user_id = user_id

    def get_full_info(self, content_id):
        content = self.catalog_service.get_content(content_id)

        if not content:
            raise ValueError("Content not found")

        return content

    def add_to_library(self, content_id):
        content = self.catalog_service.add_to_library(content_id)
        return content
        
    def remove_from_library(self, content_id):
        # Lógica para eliminar contenido de la biblioteca del usuario
        pass

    def list_library(self):
        # Lógica para listar todo el contenido en la biblioteca del usuario
        pass