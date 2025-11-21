# Script para arrancar el servidor Flask en modo desarrollo

from server.src.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)