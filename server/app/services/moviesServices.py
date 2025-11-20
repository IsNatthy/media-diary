from app.database.db import get_movies, add_movie, update_movie_state, delete_movie

def get_all_movies():
    return get_movies()

def create_movie(name, year, type, genre, state):
    if len(name) > 100 or len(name) < 1:
        raise ValueError("El nombre no es valido")
    if not name or not year or not type or not genre or not state:
        raise ValueError("Por favor llenar todos los campos")
    if state not in ['Visto', 'Por ver', 'Viendo']:
        raise ValueError("Estado invalido")
    add_movie(name, year, type, genre, state)

def change_movie_state(movie_id, new_state):
    if new_state not in ['Visto', 'Por ver', 'Viendo']:
        raise ValueError("Estado invalido")
    update_movie_state(movie_id, new_state)

def remove_movie(movie_id):
    delete_movie(movie_id)