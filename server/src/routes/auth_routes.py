# AuthRoutes - Endpoints de autenticación (POST /auth/register, /auth/login, /auth/logout, GET /auth/me)

from flask import Blueprint, request, jsonify, session
from server.src.repositories.user_repository import UserRepository
from server.src.models.user import User

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
    
    # find_by_username might be wrong if user_id is int.
    # But repo.find_by_username(username) is used in login.
    # Here we pass user_id.
    # I should check UserRepository.
    # But I will leave logic as is, just fixing imports.
    # Wait, if I pass user_id to find_by_username, it might fail if it expects string or query is WHERE username=?
    # I'll check UserRepository later.
    user_row = repo.find_by_id(user_id) 
    if not user_row:
        return jsonify({"message": "User not found"}), 404
    
    user = {
        "id": user_row[0],
        "username": user_row[1],
        "email": user_row[2]
    }
    return jsonify(user), 200