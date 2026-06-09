import sqlite3
import os

DB_NAME = "data/lottery.db"


def create_database():

    os.makedirs("data", exist_ok=True)

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
        superbalota INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def get_total_draws():

    create_database()

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM baloto_draws"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def insert_test_draw():

    create_database()

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT OR IGNORE INTO baloto_draws
        (
            draw_date,
            n1,
            n2,
            n3,
            n4,
            n5,
            superbalota
        )
        VALUES
        (
            '2026-01-01',
            1,
            2,
            3,
            4,
            5,
            6
        )
        """)

        conn.commit()

        return True

    except Exception as e:

        print(f"Error insertando sorteo de prueba: {e}")

        return False

    finally:

        conn.close()


def insert_draw(
    fecha,
    n1,
    n2,
    n3,
    n4,
    n5,
    superbalota
):

    create_database()

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO baloto_draws
        (
            draw_date,
            n1,
            n2,
            n3,
            n4,
            n5,
            superbalota
        )
        VALUES
        (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            fecha,
            n1,
            n2,
            n3,
            n4,
            n5,
            superbalota
        ))

        conn.commit()

        return True

    except Exception as e:

        print(f"Error insertando sorteo: {e}")

        return False

    finally:

        conn.close()
