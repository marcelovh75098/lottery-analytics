import sqlite3

DB_NAME = "lottery.db"


# =========================
# CREAR BASE DE DATOS
# =========================
def create_database():

    conn = sqlite3.connect(DB_NAME)
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


# =========================
# COMPATIBILIDAD APP (CRÍTICO)
# =========================
def init_db():
    create_database()


# =========================
# INSERTAR SORTEO
# =========================
def insert_draw(draw_date, n1, n2, n3, n4, n5, superbalota):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO baloto_draws (
            draw_date, n1, n2, n3, n4, n5, superbalota
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (draw_date, n1, n2, n3, n4, n5, superbalota))

    conn.commit()
    conn.close()


# =========================
# OBTENER SORTEOS (OBLIGATORIO PARA APP)
# =========================
def get_all_draws():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT n1, n2, n3, n4, n5, superbalota
        FROM baloto_draws
        ORDER BY id ASC
    """)

    data = cursor.fetchall()
    conn.close()

    return data


# =========================
# TOTAL SORTEOS
# =========================
def get_total_draws():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM baloto_draws")

    total = cursor.fetchone()[0]

    conn.close()

    return total
