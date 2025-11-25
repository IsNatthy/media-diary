# Script para arrancar el servidor Flask en modo desarrollo
import sys
import os

# Add the server directory to the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)