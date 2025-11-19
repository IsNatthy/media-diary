from flask import Flask
from .database.db import init_db
from .routes.movie_routes import movie_bp
from .routes.series_routes import series_bp

def create_app():
    app = Flask(__name__)

    # Inicializar base de datos
    init_db()

    # Registrar rutas
    app.register_blueprint(movie_bp, url_prefix="/movies")
    app.register_blueprint(series_bp, url_prefix="/series")

    return app
