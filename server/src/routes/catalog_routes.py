# CatalogRoutes - Endpoints de catálogo público (GET /api/catalog)

from flask import Blueprint, jsonify
from src.services.catalog_service import CatalogService

catalog_bp = Blueprint('catalog', __name__)
service = CatalogService()

@catalog_bp.get('/')
def list_catalog():
    return jsonify(service.list_catalog()), 200

@catalog_bp.get('/<int:item_id>')
def get_catalog_item(item_id):
    item = service.get_item(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"message": "Item not found"}), 404