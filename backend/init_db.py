from models.user_model import create_default_admin
from models.contact_model import create_contact_table

def init_db():
    create_contact_table()
    create_default_admin()
