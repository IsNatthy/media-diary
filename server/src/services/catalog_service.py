# CatalogService - Gestión de catálogo predefinido de películas/series

class CatalogService:
    def __init__(self):
        # Simulación de catálogo global
        self.catalog = [
            {
                "id": 1,
                "title": "Inception",
                "year": 2010,
                "type": "movie",
                "genre": "Sci-Fi",
                "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=300&h=450&fit=crop",
                "description": "Un ladrón que roba secretos corporativos a través del uso de tecnología de compartir sueños.",
                "duration": 148
            },
            {
                "id": 2,
                "title": "Breaking Bad",
                "year": 2008,
                "type": "series",
                "genre": "Crime",
                "poster": "https://i.pinimg.com/1200x/37/62/75/37627587496965efcc0ae42ac9dff525.jpg",
                "description": "Un profesor de química se convierte en fabricante de metanfetaminas.",
                "total_episodes": 62
            },
            {
                "id": 3,
                "title": "The Dark Knight",
                "year": 2008,
                "type": "movie",
                "genre": "Action",
                "poster": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?w=300&h=450&fit=crop",
                "description": "Batman debe aceptar una de las mayores pruebas para luchar contra la injusticia.",
                "duration": 152
            },
            {
                "id": 4,
                "title": "Stranger Things",
                "year": 2016,
                "type": "series",
                "genre": "Horror",
                "poster": "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?w=300&h=450&fit=crop",
                "description": "Cuando un niño desaparece, su madre, un jefe de policía y sus amigos deben enfrentarse a fuerzas terroríficas.",
                "total_episodes": 34
            },
            {
                "id": 5,
                "title": "Interstellar",
                "year": 2014,
                "type": "movie",
                "genre": "Sci-Fi",
                "poster": "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=300&h=450&fit=crop",
                "description": "Un equipo de exploradores viaja a través de un agujero de gusano en el espacio.",
                "duration": 169
            },
            {
                "id": 6,
                "title": "The Crown",
                "year": 2016,
                "type": "series",
                "genre": "Drama",
                "poster": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=300&h=450&fit=crop",
                "description": "Sigue la vida política de la Reina Isabel II y los eventos que definieron la segunda mitad del siglo XX.",
                "total_episodes": 60
            },
            {
                "id": 7,
                "title": "Parasite",
                "year": 2019,
                "type": "movie",
                "genre": "Thriller",
                "poster": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=300&h=450&fit=crop",
                "description": "Una familia pobre planea infiltrarse en una familia rica haciéndose pasar por trabajadores altamente calificados.",
                "duration": 132
            },
            {
                "id": 8,
                "title": "The Mandalorian",
                "year": 2019,
                "type": "series",
                "genre": "Sci-Fi",
                "poster": "https://images.unsplash.com/photo-1579566346927-c68383817a25?w=300&h=450&fit=crop",
                "description": "Las aventuras de un cazarrecompensas solitario en los confines de la galaxia.",
                "total_episodes": 24
            }
        ]

    def list_catalog(self):
        return self.catalog
    
    def get_item(self, item_id):
        for item in self.catalog:
            if item["id"] == item_id:
                return item
        return None