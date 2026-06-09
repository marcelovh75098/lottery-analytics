import sqlite3

DB_NAME = "lottery.db"


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


def insert_draw(
    draw_date,
    n1,
    n2,
    n3,
    n4,
    n5,
    superbalota
):

    try:

        conn = sqlite3.connect(DB_NAME)

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO baloto_draws (
                draw_date,
                n1,
                n2,
                n3,
                n4,
                n5,
                superbalota
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
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

        return True

    except Exception:

        return False


def get_total_draws():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM baloto_draws
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_all_draws():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            draw_date,
            n1,
            n2,
            n3,
            n4,
            n5,
            superbalota
        FROM baloto_draws
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
