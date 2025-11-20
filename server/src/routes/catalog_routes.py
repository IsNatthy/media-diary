# CatalogRoutes - Endpoints de catálogo público (GET /api/catalog)

from flask import Blueprint, jsonify
from app.src.repositories.content_repository import ContentRepository

catalog_bp = Blueprint('catalog', __name__)
repo = ContentRepository()

@catalog_bp.get('/catalog')
def list_catalog():
    content_list = repo.get_all_content()
    return jsonify(content_list), 200

@catalog_bp.get('/catalog/<int:content_id>')
def get_catalog_item(content_id):
    content = repo.get_content_by_id(content_id)
    if content:
        return jsonify(content), 200
    else:
        return jsonify({"message": "Content not found"}), 404