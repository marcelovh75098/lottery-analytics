import csv
import os

from database.db import get_total_draws, insert_draw, init_db


CSV_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "historico_baloto_revancha_2017_2026.csv"
)


def bootstrap_if_empty():
    """
    Si la base está vacía:
    -> carga histórico real desde CSV
    """

    init_db()

    total = get_total_draws()

    if total > 0:
        return {
            "status": "already_loaded",
            "total_draws": total
        }

    if not os.path.exists(CSV_PATH):
        return {
            "status": "error",
            "message": "CSV no encontrado",
            "total_draws": 0
        }

    inserted = 0

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            insert_draw(
                tipo_sorteo=row.get("tipo_sorteo", "baloto"),
                sorteo_id=int(row["sorteo_id"]),
                draw_date=row["fecha"],
                n1=int(row["n1"]),
                n2=int(row["n2"]),
                n3=int(row["n3"]),
                n4=int(row["n4"]),
                n5=int(row["n5"]),
                superbalota=int(row["superbalota"])
            )
            inserted += 1

    return {
        "status": "loaded",
        "inserted": inserted,
        "total_draws": get_total_draws()
    }
