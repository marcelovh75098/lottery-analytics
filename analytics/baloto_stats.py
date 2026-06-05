import sqlite3

DB_NAME = "data/lottery.db"

def get_total_draws():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM baloto_draws"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total
