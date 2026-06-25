import sqlite3

DB_NAME = "lottery.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS baloto_draws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_sorteo TEXT,
            sorteo_id INTEGER,
            draw_date TEXT,
            n1 INTEGER,
            n2 INTEGER,
            n3 INTEGER,
            n4 INTEGER,
            n5 INTEGER,
            superbalota INTEGER,
            UNIQUE(tipo_sorteo, sorteo_id)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS predictions_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prediction_date TEXT,
            strategy TEXT,
            n1 INTEGER,
            n2 INTEGER,
            n3 INTEGER,
            n4 INTEGER,
            n5 INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO baloto_draws (
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
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
    conn.close()


def save_prediction(
    prediction_date,
    strategy,
    numbers
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO predictions_history (
            prediction_date,
            strategy,
            n1,
            n2,
            n3,
            n4,
            n5
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        prediction_date,
        strategy,
        numbers[0],
        numbers[1],
        numbers[2],
        numbers[3],
        numbers[4]
    ))

    conn.commit()
    conn.close()


def get_predictions_history(limit=100):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            prediction_date,
            strategy,
            n1,
            n2,
            n3,
            n4,
            n5,
            created_at
        FROM predictions_history
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cur.fetchall()

    conn.close()

    return rows


def get_total_draws():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM baloto_draws"
    )

    total = cur.fetchone()[0]

    conn.close()

    return total


def get_all_draws():

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
        ORDER BY draw_date
    """)

    rows = cur.fetchall()

    conn.close()

    return rows
