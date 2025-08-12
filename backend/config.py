import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'clave-secreta')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'tadeohuamanfernandoalex@gmail.com'
SMTP_PASS = 'fpqbkqeoazmurgsc'  # Tu App Password de Gmail
CONTACT_EMAIL = 'tadeohuamanfernandoalex@gmail.com'

DB_PATH = 'database.db'
