# LibraryService - CRUD de biblioteca personal del usuario + validación ownership
from sqlalchemy.orm import Session
from src.repositories.content_repository import ContentRepository
from src.models.movie import Movie
from src.models.series import Series

class LibraryService:
    def __init__(self, db: Session):
        self.content_repo = ContentRepository(db)

    def get_user_library(self, user_id):
        return self.content_repo.find_by_user(user_id)

    def add_content(self, user_id, data):
        # Validations
        if not data.get('title'):
            raise ValueError("El título es obligatorio")
            
        if not data.get('year') or not str(data.get('year')).isdigit():
            raise ValueError("El año debe ser un número válido")
            
        valid_statuses = ['pending', 'watching', 'completed', 'dropped']
        if data.get('status') and data.get('status') not in valid_statuses:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(valid_statuses)}")
            
        rating = data.get('rating', 0)
        if rating < 0 or rating > 5:
            raise ValueError("La calificación debe estar entre 0 y 5")

        content_type = data.get('type')
        
        # Map frontend fields to backend model fields
        common_data = {
            "title": data.get('title'),
            "year": data.get('year'),
            "status": data.get('status', 'pending'),
            "rating": data.get('rating', 0),
            "review": data.get('review'),
            "image_url": data.get('poster'), # Frontend sends 'poster'
            "description": data.get('description'),
            "user_id": user_id
        }

        if content_type == 'movie':
            content = Movie(
                **common_data,
                duration=data.get('duration')
            )
        elif content_type == 'series':
            content = Series(
                **common_data,
                current_season=data.get('currentSeason', 1), # Frontend sends camelCase
                current_episode=data.get('currentEpisode', 1),
                total_episodes=data.get('totalEpisodes')
            )
        else:
            raise ValueError("Tipo de contenido inválido")
            
        return self.content_repo.create(content)

    def update_content(self, user_id, content_id, data):
        content = self.content_repo.find_by_id(content_id)
        
        if not content:
            raise ValueError("Contenido no encontrado")
            
        if content.user_id != user_id:
            raise PermissionError("No tienes permiso para editar este contenido")
            
        # Validations for updates
        if 'status' in data:
            valid_statuses = ['pending', 'watching', 'completed', 'dropped']
            if data['status'] not in valid_statuses:
                raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(valid_statuses)}")
                
        if 'rating' in data:
            rating = data['rating']
            if rating < 0 or rating > 5:
                raise ValueError("La calificación debe estar entre 0 y 5")
            
        # Map frontend fields to backend model fields for update
        field_mapping = {
            'poster': 'image_url',
            'currentSeason': 'current_season',
            'currentEpisode': 'current_episode',
            'totalEpisodes': 'total_episodes'
        }

        # Update fields
        for key, value in data.items():
            # Use mapped key if exists, else use original key
            model_key = field_mapping.get(key, key)
            if hasattr(content, model_key):
                setattr(content, model_key, value)
                
        return self.content_repo.update(content)

    def delete_content(self, user_id, content_id):
        content = self.content_repo.find_by_id(content_id)
        
        if not content:
            raise ValueError("Contenido no encontrado")
            
        if content.user_id != user_id:
            raise PermissionError("No tienes permiso para eliminar este contenido")
            
        self.content_repo.delete(content)