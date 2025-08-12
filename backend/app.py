from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import config
from routes.auth_routes import auth_bp
from routes.contact_routes import contact_bp
from routes.user_routes import user_bp
from routes.email_routes import mail_bp, init_mail  # 👈 nuevo
from init_db import init_db

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = config.JWT_ACCESS_TOKEN_EXPIRES

# Inicializar correo
init_mail(app)  # 👈 nuevo

CORS(app, origins=['http://localhost:5173', 'https://tu-frontend.vercel.app'])
jwt = JWTManager(app)

# Registrar Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(contact_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")
app.register_blueprint(mail_bp, url_prefix="/api")  # 👈 nuevo

# Mostrar todas las rutas registradas
with app.app_context():
    print("\n📌 Rutas registradas en el backend:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint:30s} -> {rule}")
    print("")

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
