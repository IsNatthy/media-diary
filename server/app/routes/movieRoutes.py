from flask import Blueprint, request, jsonify
from app.database.db import (
    get_movies,
    add_movie,
    update_movie_state,
    delete_movie
)

movie_bp = Blueprint('movies', __name__)

#Obtener todas las peliculas
@movie_bp.get('/')
def get_movies_route():
    movies = get_movies()
    return jsonify(movies), 200

#Agregar nueva pelicula
@movie_bp.post('/')
def add_movie_route():
    data = request.json
    add_movie(data['name'], data['year'], data['type'], data['genre'], data['state'])
    return jsonify({"message": "Movie added successfully"}), 201

#Actualizar estado de la pelicula
@movie_bp.put('/<int:movie_id>/state')
def update_movie_state_route(movie_id):
    data = request.json
    update_movie_state(movie_id, data['new_state'])
    return jsonify({"message": "Movie state updated successfully"}), 200

#Eliminar pelicula
@movie_bp.delete('/<int:movie_id>')
def delete_movie_route(movie_id):
    delete_movie(movie_id)
    return jsonify({"message": "Movie deleted successfully"}), 200
