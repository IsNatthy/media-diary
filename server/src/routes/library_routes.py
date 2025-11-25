# LibraryRoutes - Endpoints de biblioteca personal (GET/POST/PUT/DELETE /api/library)

from flask import Blueprint, jsonify, request, session
from src.config.database import get_db
from src.services.library_service import LibraryService

library_bp = Blueprint('library', __name__)

@library_bp.get('/')
def list_library():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "No autenticado"}), 401

    db = next(get_db())
    service = LibraryService(db)
    
    try:
        contents = service.get_user_library(user_id)
        return jsonify([c.to_dict() for c in contents]), 200
    finally:
        db.close()

@library_bp.post('/')
def add_content():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "No autenticado"}), 401

    data = request.json
    db = next(get_db())
    service = LibraryService(db)
    
    try:
        content = service.add_content(user_id, data)
        return jsonify(content.to_dict()), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    finally:
        db.close()

@library_bp.put('/<int:content_id>')
def update_content(content_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "No autenticado"}), 401

    data = request.json
    db = next(get_db())
    service = LibraryService(db)
    
    try:
        content = service.update_content(user_id, content_id, data)
        return jsonify(content.to_dict()), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except PermissionError as e:
        return jsonify({"message": str(e)}), 403
    finally:
        db.close()

@library_bp.delete('/<int:content_id>')
def delete_content(content_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "No autenticado"}), 401

    db = next(get_db())
    service = LibraryService(db)
    
    try:
        service.delete_content(user_id, content_id)
        return jsonify({"message": "Contenido eliminado"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except PermissionError as e:
        return jsonify({"message": str(e)}), 403
    finally:
        db.close()