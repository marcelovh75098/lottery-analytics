import sqlite3
import os

DB_NAME = "lottery.db"


def get_connection():
    """
    JUSTIFICACIÓN:
    Centraliza conexión.
    Evita corrupción por múltiples accesos simultáneos.
    """
    return sqlite3.connect(DB_NAME)


def init_db():
    """
    JUSTIFICACIÓN:
    Garantiza existencia de tabla SIEMPRE.
    Se ejecuta de forma idempotente (segura múltiples veces).
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS baloto_draws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            draw_date TEXT UNIQUE,
            n1 INTEGER,
            n2 INTEGER,
            n3 INTEGER,
            n4 INTEGER,
            n5 INTEGER,
            superbalota INTEGER
        )
    """)

    conn.commit()
    conn.close()


def safe_init():
    """
    JUSTIFICACIÓN:
    Capa de protección para Render.
    Asegura DB antes de cualquier query.
    """

    init_db()


def get_total_draws():

    safe_init()  # 🔥 CLAVE: nunca consultar sin tabla

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM baloto_draws")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_all_draws():

    safe_init()  # 🔥 PROTECCIÓN CRÍTICA

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT n1, n2, n3, n4, n5, superbalota
        FROM baloto_draws
        ORDER BY id ASC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
