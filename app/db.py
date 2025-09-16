import psycopg
from psycopg.rows import dict_row
from .config import DATABASE_URL

 # opens a new connection
def get_connection():
    conn = psycopg.connect(DATABASE_URL)
    conn.row_factory = dict_row
    return conn

'''
Design Decision 1: Since the task requires small services and straightforward CRUD, I chose to use a Sync driver psycopg3 (sync) + raw SQL with parameterized queries.

Design Optimization: If the task was to develop endpoints for High-throughput APIs, then an async driver would fit the task (eg: asyncpg)

'''
def get_db_conn():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()