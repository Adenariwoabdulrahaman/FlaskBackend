import sqlite3

def get_db_connection():
    try:
        conn = sqlite3.connect('yamdb.sqlite3')
        conn.row_factory = sqlite3.Row
        print("SQLite connected to yamdb.sqlite3.")
        return conn
    except Exception as e:
        print("Failed to connect to SQLite:", e)
        return None
