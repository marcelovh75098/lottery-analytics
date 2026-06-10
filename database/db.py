import sqlite3
from collections import Counter

DB_NAME = "lottery.db"


# =========================
# OBTENER HISTORIAL
# =========================
def get_draws():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT n1,n2,n3,n4,n5,superbalota
        FROM baloto_draws
        ORDER BY id ASC
    """)

    data = cursor.fetchall()
    conn.close()

    return data


# =========================
# CREAR FEATURES
# =========================
def create_features(window):

    numbers = []
    for row in window:
        numbers.extend(row)

    counter = Counter(numbers)

    # vector de features (simplificado pero potente)
    features = [
        counter.get(i, 0) for i in range(1, 51)  # números 1–50
    ]

    return features


# =========================
# DATASET ML
# =========================
def build_dataset(window_size=20):

    data = get_draws()

    X = []
    y = []

    for i in range(window_size, len(data)):

        window = data[i-window_size:i]

        X.append(create_features(window))

        # target: sorteo actual
        y.append(data[i])

    return X, y
def init_db():
    # Alias de compatibilidad para el sistema institucional
    create_database()
