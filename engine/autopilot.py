from database.db import get_total_draws, insert_draw
from scrapers.baloto_scraper import obtener_ultimo_sorteo


# =========================================================
# AUTOPILOT - GARANTIZA DATOS MÍNIMOS
# =========================================================
def ensure_data(min_rows=30):

    total = get_total_draws()

    # =========================
    # CASO 1: YA HAY DATA
    # =========================
    if total >= min_rows:
        return {
            "status": "ok",
            "message": "Dataset listo",
            "total": total
        }

    # =========================
    # CASO 2: FALTA DATA → AUTO-INGESTA
    # =========================
    inserted = 0
    attempts = 0

    while get_total_draws() < min_rows and attempts < 10:

        data = obtener_ultimo_sorteo()
        attempts += 1

        # si falla scraper
        if not data or "error" in data:
            continue

        try:
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

        except Exception:
            continue

    return {
        "status": "ok",
        "inserted": inserted,
        "total": get_total_draws()
    }
