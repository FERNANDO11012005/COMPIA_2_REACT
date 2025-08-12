from models.db import get_db_connection

def create_contact_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            message TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            status VARCHAR(20) DEFAULT 'new'
        )
    ''')
    conn.commit()
    conn.close()

def insert_contact(name, email, message):
    conn = get_db_connection()
    cursor = conn.execute(
        'INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
        (name, email, message)
    )
    contact_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return contact_id

def get_contacts_paginated(page, per_page, status):
    offset = (page - 1) * per_page
    conn = get_db_connection()

    where_clause = ""
    params = []
    if status != 'all':
        where_clause = "WHERE status = ?"
        params.append(status)

    total_query = f"SELECT COUNT(*) FROM contacts {where_clause}"
    total = conn.execute(total_query, params).fetchone()[0]

    query = f"""
        SELECT * FROM contacts {where_clause}
        ORDER BY created_at DESC
        LIMIT ? OFFSET ?
    """
    params.extend([per_page, offset])
    contacts = conn.execute(query, params).fetchall()
    conn.close()

    return total, contacts
