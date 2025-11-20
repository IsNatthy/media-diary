# LibraryRoutes - Endpoints de biblioteca personal (GET/POST/PUT/DELETE /api/library)

from flask import Blueprint, jsonify, request, session
from app.src.services.library_service import LibraryService
from app.src.repositories.catalog_service import CatalogService

library_bp = Blueprint('library', __name__)

catalog_service = CatalogService()
library_service = LibraryService(catalog_service, user_id=None)  # user_id se establecerá desde la sesión

@library_bp.get('/library')
def list_library():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    library_service.user_id = user_id
    library_content = library_service.list_library()
    return jsonify(library_content), 200

@library_bp.post('/library/<int:content_id>')
def add_to_library(content_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    library_service.user_id = user_id
    content = library_service.add_to_library(content_id)
    return jsonify(content), 201

@library_bp.delete('/library/<int:content_id>')
def remove_from_library(content_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    library_service.user_id = user_id
    library_service.remove_from_library(content_id)
    return jsonify({"message": "Content removed from library"}), 200

@library_bp.get('/library/<int:content_id>')
def get_library_item(content_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    library_service.user_id = user_id
    try:
        content = library_service.get_full_info(content_id)
        return jsonify(content), 200
    except ValueError:
        return jsonify({"message": "Content not found"}), 404