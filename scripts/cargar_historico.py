import pandas as pd
from database.db import insert_draw, existe_sorteo

# ruta del archivo CSV
FILE_PATH = "data/historico_baloto_revancha_2017_2026.csv"

def cargar_historico():
    df = pd.read_csv(FILE_PATH)

    print(f"📊 Total registros en CSV: {len(df)}")

    insertados = 0
    duplicados = 0

    for _, row in df.iterrows():

        data = {
            "fecha": row["fecha"],
            "n1": int(row["n1"]),
            "n2": int(row["n2"]),
            "n3": int(row["n3"]),
            "n4": int(row["n4"]),
            "n5": int(row["n5"]),
            "superbalota": int(row["superbalota"])
        }

        if existe_sorteo(data["fecha"], data["superbalota"]):
            duplicados += 1
            continue

        insert_draw(data)
        insertados += 1

    print("✅ Carga completada")
    print(f"✔ Insertados: {insertados}")
    print(f"⚠ Duplicados: {duplicados}")


if __name__ == "__main__":
    cargar_historico()
