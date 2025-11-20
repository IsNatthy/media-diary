# AuthRoutes - Endpoints de autenticación (POST /auth/register, /auth/login, /auth/logout, GET /auth/me)

from flask import Blueprint, request, jsonify, session
from app.src.repositories.user_repository import UserRepository
from app.src.models.user import User

auth_bp = Blueprint('auth', __name__)
repo = UserRepository()

@auth_bp.post('/register')
def register():
    data = request.json
    username = data['username']
    email = data['email']
    password = data['password']
    
    existing_user = repo.find_by_username(username)
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400
    
    repo.create(username, email, password)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.post('/login')
def login():
    data = request.json
    username = data['username']
    password = data['password']
    
    user_row = repo.find_by_username(username)
    if not user_row or user_row[3] != password:
        return jsonify({"message": "Invalid credentials"}), 401
    
    session['user_id'] = user_row[0]
    return jsonify({"message": "Login successful"}), 200

@auth_bp.post('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200

@auth_bp.get('/me')
def me():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401
    
    user_row = repo.find_by_username(user_id)
    if not user_row:
        return jsonify({"message": "User not found"}), 404
    
    user = {
        "id": user_row[0],
        "username": user_row[1],
        "email": user_row[2]
    }
    return jsonify(user), 200