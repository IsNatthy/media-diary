# AuthRoutes - Endpoints de autenticación (POST /auth/register, /auth/login, /auth/logout, GET /auth/me)

from flask import Blueprint, request, jsonify, session
from src.config.database import get_db
from src.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/register')
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({"message": "Faltan datos requeridos"}), 400
    
    db = next(get_db())
    service = AuthService(db)
    
    try:
        user = service.register(username, email, password)
        return jsonify({"message": "Usuario registrado exitosamente", "user": user.to_dict()}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    finally:
        db.close()

@auth_bp.post('/login')
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"message": "Email y contraseña son requeridos"}), 400
    
    db = next(get_db())
    service = AuthService(db)
    
    try:
        user = service.login(email, password)
        if not user:
            return jsonify({"message": "Credenciales inválidas"}), 401
        
        session['user_id'] = user.id
        return jsonify({"message": "Login exitoso", "user": user.to_dict()}), 200
    finally:
        db.close()

@auth_bp.post('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout exitoso"}), 200

@auth_bp.get('/me')
def me():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "No autenticado"}), 401
    
    db = next(get_db())
    from src.repositories.user_repository import UserRepository
    repo = UserRepository(db)
    
    try:
        user = repo.find_by_id(user_id)
        if not user:
            session.pop('user_id', None)
            return jsonify({"message": "Usuario no encontrado"}), 404
        
        return jsonify(user.to_dict()), 200
    finally:
        db.close()