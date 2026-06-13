import pandas as pd

from database.db import (
    init_db,
    insert_draw,
    get_total_draws
)

CSV_FILE = "historico_baloto_revancha_2017_2026.csv"


def importar_historico():

    init_db()

    df = pd.read_csv(CSV_FILE)

    print(f"Sorteos encontrados: {len(df)}")

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

    print("================================")
    print("IMPORTACIÓN COMPLETADA")
    print("================================")
    print(f"Total en DB: {get_total_draws()}")


if __name__ == "__main__":
    importar_historico()
