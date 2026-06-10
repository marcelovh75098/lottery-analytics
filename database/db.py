import sqlite3

# =========================
# BASE DE DATOS
# =========================
DB_NAME = "lottery.db"
# Nombre del archivo de base de datos SQLite


# =========================
# CREAR BASE DE DATOS Y TABLA
# =========================
def create_database():
    # Crea la tabla principal si no existe

    conn = sqlite3.connect(DB_NAME)
    # Conexión a SQLite local (archivo .db)

    cursor = conn.cursor()
    # Cursor para ejecutar SQL

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
    # Tabla de sorteos:
    # - id: identificador único
    # - draw_date: fecha del sorteo (única)
    # - n1-n5: números principales
    # - superbalota: número extra

    conn.commit()
    # Guarda cambios en la base de datos

    conn.close()
    # Cierra conexión


# =========================
# ALIAS INSTITUCIONAL (COMPATIBILIDAD)
# =========================
def init_db():
    # Alias para compatibilidad con app institucional

    create_database()
    # Llama a la función real de creación


# =========================
# INSERTAR SORTEO
# =========================
def insert_draw(draw_date, n1, n2, n3, n4, n5, superbalota):
    # Inserta un nuevo sorteo en la base de datos

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO baloto_draws (
                draw_date, n1, n2, n3, n4, n5, superbalota
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (draw_date, n1, n2, n3, n4, n5, superbalota))
        # INSERT OR IGNORE evita duplicados por fecha

        conn.commit()
        conn.close()

        return {"status": "ok"}
        # Respuesta estándar para Streamlit

    except Exception as e:
        return {"status": "error", "message": str(e)}
        # Manejo de errores controlado


# =========================
# OBTENER TODOS LOS SORTEOS
# =========================
def get_all_draws():
    # Función principal usada por el motor institucional

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT n1, n2, n3, n4, n5, superbalota
        FROM baloto_draws
        ORDER BY id ASC
    """)
    # Devuelve todos los sorteos ordenados cronológicamente

    data = cursor.fetchall()
    # Lista de tuplas con los sorteos

    conn.close()

    return data
    # Formato: [(n1,n2,n3,n4,n5,super), ...]


# =========================
# TOTAL DE SORTEOS
# =========================
def get_total_draws():
    # Retorna cuántos sorteos hay en la base

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM baloto_draws
    """)

    total = cursor.fetchone()[0]
    # Extrae el número total

    conn.close()

    return total
