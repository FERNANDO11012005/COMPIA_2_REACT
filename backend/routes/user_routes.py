# backend/routes/user_routes.py
from flask import Blueprint, jsonify
import requests

# Definir el Blueprint
user_bp = Blueprint("users", __name__)

# Ruta para listar usuarios desde DummyJSON
@user_bp.route("/users", methods=["GET"])
def get_users():
    res = requests.get("https://dummyjson.com/users")
    return jsonify(res.json())

# Ruta para obtener un usuario por ID
@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    res = requests.get(f"https://dummyjson.com/users/{user_id}")
    return jsonify(res.json())
