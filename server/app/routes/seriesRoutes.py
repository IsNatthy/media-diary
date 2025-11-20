from Flask import Blueprint, request, jsonify
from app.database.db import (
    get_series,
    add_series,
    update_serie_state,
    delete_series
)

series_bp = Blueprint('series', __name__)

#Obetener todas las series
@series_bp.get('/')
def get_series_route():
    series = get_series()
    return jsonify(series), 200

#Agregar nueva serie
@series_bp.post('/')
def add_series_route():
    data = request.json
    add_series(data['name'], data['year'], data['type'], data['genre'], data['state'], data['chapter'], data['total_chapters'], data['seasons'])
    return jsonify({"message": "Series added successfully"}), 201

#Actualizar estado de la serie
@series_bp.put('/<int:series_id>/state')
def update_series_state_route(series_id):
    data = request.json
    update_series_state(series_id, data['new_state'], data['chapter'], data['seasons'])
    return jsonify({"message": "Series state updated successfully"}), 200

#Eliminar serie
@series_bp.delete('/<int:series_id>')
def delete_series_route(series_id):
    delete_series(series_id)
    return jsonify({"message": "Series deleted successfully"}), 200
