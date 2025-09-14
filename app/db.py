import psycopg
from psycopg.rows import dict_row
from .config import DATABASE_URL

 # opens a new connection
def get_connection():
    conn = psycopg.connect(DATABASE_URL)
    conn.row_factory = dict_row
    return conn


def get_db_conn():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()