import pandas as pd

from database.db import (
    init_db,
    insert_draw,
    get_total_draws
)

# ==================================================
# IMPORTADOR DEL HISTÓRICO REAL BALOTO / REVANCHA
# ==================================================
# Este script se ejecuta UNA SOLA VEZ para cargar
# todos los sorteos históricos dentro de SQLite.
#
# El CSV debe contener:
#
# Tipo_Sorteo
# Sorteo_Id
# Fecha
# B1
# B2
# B3
# B4
# B5
# Super_Balota
#
# INSERT OR IGNORE evita duplicados.
# ==================================================

CSV_FILE = "data/baloto_seed.csv"


def importar_historico():

    init_db()

    df = pd.read_csv(CSV_FILE)

    print(f"Sorteos encontrados en CSV: {len(df)}")

    for _, row in df.iterrows():

        insert_draw(
            str(row["Tipo_Sorteo"]),
            int(row["Sorteo_Id"]),
            str(row["Fecha"]),
            int(row["B1"]),
            int(row["B2"]),
            int(row["B3"]),
            int(row["B4"]),
            int(row["B5"]),
            int(row["Super_Balota"])
        )

    print("===================================")
    print("Carga completada")
    print("===================================")
    print(f"Total en base de datos: {get_total_draws()}")


if __name__ == "__main__":
    importar_historico()
