import csv
import os

from database.db import (
    get_total_draws,
    insert_draw,
    init_db
)

# ==================================================
# UBICACIÓN DEL PROYECTO
# ==================================================
# JUSTIFICACIÓN:
# Render ejecuta el proyecto desde:
#
# /opt/render/project/src
#
# No podemos depender de rutas relativas ambiguas.
# Obtenemos la carpeta actual donde vive bootstrap.py
# y construimos una ruta absoluta al CSV.
# ==================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "data",
        "historico_baloto_revancha_2017_2026.csv"
    )
)

# ==================================================
# BOOTSTRAP DE DATOS
# ==================================================
# JUSTIFICACIÓN:
# Si la base está vacía:
# 1. Crear tablas
# 2. Buscar CSV histórico
# 3. Importar sorteos
# 4. Devolver estadísticas
#
# Si la base ya tiene registros:
# No vuelve a importar.
# ==================================================

def bootstrap_if_empty():

    init_db()

    total = get_total_draws()

    if total > 0:
        return {
            "status": "already_loaded",
            "total_draws": total,
            "csv_path": CSV_PATH
        }

    if not os.path.exists(CSV_PATH):
        return {
            "status": "error",
            "message": "CSV no encontrado",
            "csv_path": CSV_PATH,
            "total_draws": 0
        }

    inserted = 0

    try:

        with open(
            CSV_PATH,
            newline="",
            encoding="utf-8"
        ) as f:

            reader = csv.DictReader(f)

            for row in reader:

                insert_draw(
                    tipo_sorteo=row["tipo_sorteo"],
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
            "total_draws": get_total_draws(),
            "csv_path": CSV_PATH
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e),
            "csv_path": CSV_PATH,
            "total_draws": get_total_draws()
        }
