# Factory de la app Flask - create_app() con configuración de sesiones, CORS y blueprints

from flask import Flask
from flask_cors import CORS
from server.src.routes import auth_bp, catalog_bp, library_bp, review_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey' # In production this should be an env var
    
    # CORS configuration
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    
    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(library_bp, url_prefix='/library')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    
    return app