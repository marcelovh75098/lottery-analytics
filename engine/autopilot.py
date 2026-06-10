from database.db import get_total_draws, insert_draw
from scrapers.baloto_scraper import obtener_ultimo_sorteo


# =========================
# AUTO INGESTA DE DATOS
# =========================
def ensure_data(min_rows=30):

    total = get_total_draws()

    # =========================
    # SI YA HAY DATA SUFICIENTE
    # =========================
    if total >= min_rows:
        return {
            "status": "ok",
            "message": "Dataset completo",
            "total": total
        }

    # =========================
    # SI FALTA DATA → SCRAPER
    # =========================
    inserted = 0

    while get_total_draws() < min_rows:

        data = obtener_ultimo_sorteo()

        if not data or "error" in data:
            return {
                "status": "error",
                "message": "Scraper falló",
                "detail": data
            }

        insert_draw(
            data["draw_date"],
            data["n1"],
            data["n2"],
            data["n3"],
            data["n4"],
            data["n5"],
            data["superbalota"]
        )

        inserted += 1

    return {
        "status": "ok",
        "message": "Auto-ingesta completada",
        "inserted": inserted,
        "total": get_total_draws()
    }
