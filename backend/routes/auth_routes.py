from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)

# Simulamos un usuario con contraseña hasheada (cambia este hash por el de tu contraseña)
USUARIOS = {
    'usuario@ejemplo.com': {
        'password_hash': 'pbkdf2:sha256:150000$Ejemplo$hashed_password_aqui',
        'nombre': 'Juan Perez'
    }
}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"msg": "Email y contraseña son requeridos"}), 400

    usuario = USUARIOS.get(email)

    if not usuario or not check_password_hash(usuario['password_hash'], password):
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    access_token = create_access_token(identity=email)
    return jsonify({"access_token": access_token}), 200
