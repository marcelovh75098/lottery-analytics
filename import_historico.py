import pandas as pd

from database.db import (
    init_db,
    insert_draw
)

CSV_FILE = "data/baloto_seed.csv"


def importar_historico():

    init_db()

    df = pd.read_csv(CSV_FILE)

    total = 0

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

        total += 1

    print(f"Histórico cargado: {total} sorteos")


if __name__ == "__main__":
    importar_historico()
