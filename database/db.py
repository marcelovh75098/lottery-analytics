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
        draw_date TEXT,
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

    print("Base de datos creada correctamente")

if __name__ == "__main__":
    create_database()
