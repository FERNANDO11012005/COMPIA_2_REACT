from flask import Blueprint, request, jsonify
import sqlite3
from utils.email_utils import send_email

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["POST"])
def send_contact():
    data = request.get_json()
    name = data.get("name")       # ojo que aquí usas "name"
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"success": False, "error": "Todos los campos son obligatorios"}), 400

    # Guardar en SQLite
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    # Enviar correo, aquí los parámetros con nombre y orden correcto
    success = send_email(
        to_email="tadeohuamanfernandoalex@gmail.com",
        subject=f"Nuevo mensaje de {name}",
        body=f"Email: {email}\n\nMensaje:\n{message}"
    )

    if not success:
        return jsonify({"success": False, "error": "Error enviando el correo"}), 500

    return jsonify({"success": True, "message": "Mensaje enviado con éxito"})
