# Factory de la app Flask - create_app() con configuración de sesiones, CORS y blueprints

from flask import Flask
from flask_cors import CORS
from flask_session import Session
from src.config.database import init_db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey' # In production this should be an env var
    
    # Session configuration
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    
    # CORS configuration
    # Allow requests from the frontend
    CORS(app, supports_credentials=True, resources={
        r"/*": {
            "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Register Blueprints
    # Import inside function to avoid circular imports if any
    from src.routes.auth_routes import auth_bp
    from src.routes.catalog_routes import catalog_bp
    from src.routes.library_routes import library_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(catalog_bp, url_prefix='/api/catalog')
    app.register_blueprint(library_bp, url_prefix='/api/library')
    
    return app