from flask import Blueprint, jsonify
from flask_mail import Mail, Message
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS

mail_bp = Blueprint('mail', __name__)

# Configuración de Flask-Mail
mail = Mail()

def init_mail(app):
    app.config['MAIL_SERVER'] = SMTP_SERVER
    app.config['MAIL_PORT'] = SMTP_PORT
    app.config['MAIL_USERNAME'] = SMTP_USER
    app.config['MAIL_PASSWORD'] = SMTP_PASS
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    mail.init_app(app)

@mail_bp.route('/send-test-email', methods=['GET'])
def send_test_email():
    try:
        msg = Message(
            subject="Prueba de correo Flask",
            sender=SMTP_USER,
            recipients=["tadeohuamanfernandoalex@gmail.com"],
            body="Hola, este es un correo de prueba desde Flask."
        )
        mail.send(msg)
        return jsonify({"message": "Correo enviado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
