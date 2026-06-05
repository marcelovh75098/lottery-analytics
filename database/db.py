import sqlite3

def create_database():
    conn = sqlite3.connect("data/lottery.db")

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
        superbalota INTEGER
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Base de datos creada correctamente")
