import sqlite3

DB_NAME = "lottery.db"


def init_db():
    """
    JUSTIFICACIÓN:
    Inicializa la base de datos SQLite.
    - Se ejecuta al inicio del sistema.
    - Evita error de tabla inexistente en Render o local.
    """
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


def insert_draw(draw_date, n1, n2, n3, n4, n5, superbalota):
    """
    JUSTIFICACIÓN:
    Inserta un sorteo en la base de datos.
    - INSERT OR IGNORE evita duplicados por draw_date.
    - Previene corrupción del dataset en re-ejecuciones.
    """
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


def get_all_draws():
    """
    JUSTIFICACIÓN:
    Extrae todo el historial de sorteos.
    - Base del backtesting cuantitativo.
    - Orden ascendente para simulación temporal.
    """
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


def get_total_draws():
    """
    JUSTIFICACIÓN:
    Retorna el tamaño del dataset.
    - Usado para validar si el sistema puede ejecutar backtesting.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM baloto_draws")
    total = cursor.fetchone()[0]

    conn.close()
    return total
