import sqlite3
from collections import Counter

DB_NAME = "lottery.db"


# =========================
# INIT DB
# =========================
def init_db():
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
# INSERT
# =========================
def insert_draw(draw_date, n1, n2, n3, n4, n5, superbalota):
    try:
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

        return {"ok": True}

    except Exception as e:
        return {"error": str(e)}


# =========================
# TRAER SORTEOS ORDENADOS
# =========================
def get_draws_ordered():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT draw_date, n1, n2, n3, n4, n5, superbalota
        FROM baloto_draws
        ORDER BY id ASC
    """)

    data = cursor.fetchall()
    conn.close()

    return data


# =========================
# PREDICCIÓN (VENTANA MÓVIL)
# =========================
def predict_from_history(history_window):

    numbers = []
    for row in history_window:
        numbers.extend(row[1:])  # ignoramos fecha

    counter = Counter(numbers)

    return [num for num, _ in counter.most_common(6)]


# =========================
# EVALUAR
# =========================
def evaluate(prediction, real):

    hits = len(set(prediction) & set(real))
    score = (hits / 6) * 100

    return hits, round(score, 2)


# =========================
# BACKTESTING COMPLETO
# =========================
def run_backtest(window_size=20):

    data = get_draws_ordered()

    results = []

    for i in range(window_size, len(data)):

        # ventana histórica
        window = data[i-window_size:i]

        # predicción
        pred = predict_from_history(window)

        # resultado real
        real = data[i][1:]

        hits, score = evaluate(pred, real)

        results.append({
            "index": i,
            "prediction": pred,
            "real": real,
            "hits": hits,
            "score": score
        })

    return results
