import sqlite3

DB_path = 'database.db' #Cambiar luego

# Inicializar la conexion a la base de datos
def init_db():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        type TEXT NOT NULL,
        genre TEXT NOT NULL,
        state TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        type TEXT NOT NULL,
        genre TEXT NOT NULL,
        state TEXT NOT NULL,
        chapter INTEGER NOT NULL,
        total_chapters INTEGER NOT NULL,
        seasons INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Obtener peliculas de la base de datos
def get_movies():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    conn.close()
    return movies

#Obetener series de la base de datos
def get_series():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM series')
    series = cursor.fetchall()
    conn.close()
    return series

#Agregar pelicula a la base de datos
def add_movie(name, year, type, genre, state):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO movies (name, year, type, genre, state)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, year, type, genre, state))
    conn.commit()
    conn.close()

#Agregar serie a la base de datos
def add_series(name, year, type, genre, state, chapter, total_chapters, seasons):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO series (name, year, type, genre, state, chapter, total_chapters, seasons)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, year, type, genre, state, chapter, total_chapters, seasons))
    conn.commit()
    conn.close()

#Actualizar estado de la pelicula
def update_movie_state(movie_id, new_state):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE movies
        SET state = ?
        WHERE id = ?
    ''', (new_state, movie_id))
    conn.commit()
    conn.close()

#Actualizar estado de la serie
def update_series_state(series_id, new_state, chapter, seasons):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE series
        SET state = ?,
        SET chapter = ?,
        SET seasons = ?
        WHERE id = ?
    ''', (new_state, series_id))
    conn.commit()
    conn.close()

# Eliminar pelicula de la base de datos
def delete_movie(movie_id):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM movies
        WHERE id = ?
    ''', (movie_id,))
    conn.commit()
    conn.close()

# Eliminar serie de la base de datos
def delete_series(series_id):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM series
        WHERE id = ?
    ''', (series_id,))
    conn.commit()
    conn.close()