from models.db import get_db_connection
from utils.security import hash_password

def create_default_admin():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(20) DEFAULT 'admin',
            avatar VARCHAR(255),
            phone VARCHAR(20),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    admin_password = hash_password('admin123')
    cursor.execute('''
        INSERT OR IGNORE INTO admin_users (name, email, password, role)
        VALUES (?, ?, ?, ?)
    ''', ('Administrador', 'admin@cafeteria.com', admin_password, 'super_admin'))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM admin_users WHERE email = ? AND is_active = 1',
        (email,)
    ).fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute(
        'SELECT id, name, email, role, avatar FROM admin_users WHERE id = ? AND is_active = 1',
        (user_id,)
    ).fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_db_connection()
    users = conn.execute('''
        SELECT id, name, email, role, avatar, phone, created_at, is_active
        FROM admin_users
        ORDER BY created_at DESC
    ''').fetchall()
    conn.close()
    return users

def insert_user(name, email, password, role, phone):
    conn = get_db_connection()
    cursor = conn.execute('''
        INSERT INTO admin_users (name, email, password, role, phone)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, email, hash_password(password), role, phone))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

def update_user(user_id, updates):
    conn = get_db_connection()
    set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
    values = list(updates.values())
    values.append(user_id)
    conn.execute(f"UPDATE admin_users SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = ?", values)
    conn.commit()
    conn.close()

def soft_delete_user(user_id):
    conn = get_db_connection()
    conn.execute('UPDATE admin_users SET is_active = 0 WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
