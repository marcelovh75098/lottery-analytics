import sqlite3

DB_NAME = "lottery.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    """
    Crea la tabla principal.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS baloto_draws (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            tipo_sorteo TEXT,

            sorteo_id INTEGER UNIQUE,

            draw_date TEXT,

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


def insert_draw(
    tipo_sorteo,
    sorteo_id,
    draw_date,
    n1,
    n2,
    n3,
    n4,
    n5,
    superbalota
):
    """
    Inserta únicamente sorteos nuevos.
    """

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        INSERT OR IGNORE INTO baloto_draws(

            tipo_sorteo,

            sorteo_id,

            draw_date,

            n1,
            n2,
            n3,
            n4,
            n5,

            superbalota

        )

        VALUES(

            ?,?,?,?,?,?,?,?,?

        )

    """,(

        tipo_sorteo,

        sorteo_id,

        draw_date,

        n1,
        n2,
        n3,
        n4,
        n5,

        superbalota

    ))

    conn.commit()

    inserted = cur.rowcount

    conn.close()

    return inserted > 0


def draw_exists(sorteo_id):
    """
    Verifica si el sorteo ya existe.
    """

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        SELECT 1

        FROM baloto_draws

        WHERE sorteo_id=?

    """,(sorteo_id,))

    existe = cur.fetchone() is not None

    conn.close()

    return existe


def get_last_draw():
    """
    Obtiene el último sorteo almacenado.
    """

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        SELECT

            tipo_sorteo,

            sorteo_id,

            draw_date,

            n1,
            n2,
            n3,
            n4,
            n5,

            superbalota

        FROM baloto_draws

        ORDER BY sorteo_id DESC

        LIMIT 1

    """)

    row = cur.fetchone()

    conn.close()

    return row


def get_total_draws():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        SELECT COUNT(*)

        FROM baloto_draws

    """)

    total = cur.fetchone()[0]

    conn.close()

    return total


def get_all_draws():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        SELECT

            n1,

            n2,

            n3,

            n4,

            n5,

            superbalota

        FROM baloto_draws

        ORDER BY sorteo_id

    """)

    rows = cur.fetchall()

    conn.close()

    return rows
