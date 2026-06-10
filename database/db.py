import sqlite3

DB_NAME = "lottery.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    """
    Garantiza que la tabla exista siempre.
    Se ejecuta en cada arranque sin riesgo.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
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


def insert_draw(draw_date, n1, n2, n3, n4, n5, superbalota):
    """
    Inserción segura (evita duplicados).
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO baloto_draws (
            draw_date, n1, n2, n3, n4, n5, superbalota
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (draw_date, n1, n2, n3, n4, n5, superbalota))

    conn.commit()
    conn.close()


def get_all_draws():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT n1, n2, n3, n4, n5, superbalota
        FROM baloto_draws
        ORDER BY id ASC
    """)

    data = cur.fetchall()
    conn.close()
    return data


def get_total_draws():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM baloto_draws")
    total = cur.fetchone()[0]

    conn.close()
    return total
