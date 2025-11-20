from app.database.db import get_series, add_series, update_series_state, delete_series

def get_all_series():
    return get_series()

def create_series(name, year, type, genre, state, chapter, total_chapters, seasons):
    if len(name) > 100 or len(name) < 1:
        raise ValueError("El nombre no es valido")
    if not name or not year or not type or not genre or not state or chapter is None or total_chapters is None or seasons is None:
        raise ValueError("Por favor llenar todos los campos")
    add_series(name, year, type, genre, state, chapter, total_chapters, seasons)

def change_series_state(series_id, new_state, chapter, seasons):
    if chapter is None or seasons is None:
        raise ValueError("Por favor llenar todos los campos")
    if new_state not in ['Visto', 'Por ver', 'Viendo']:
        raise ValueError("Estado invalido")
    update_series_state(series_id, new_state, chapter, seasons)

def remove_series(series_id):
    delete_series(series_id)