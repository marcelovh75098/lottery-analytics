from scrapers.baloto_scraper import obtener_ultimo_sorteo
from database.db import insert_draw, init_db


# =========================
# INICIALIZAR DB
# =========================
init_db()


# =========================
# OBTENER SORTEO
# =========================
data = obtener_ultimo_sorteo()


# =========================
# VALIDACIÓN
# =========================
if data and "error" not in data:

    insert_draw(
        data["draw_date"],
        data["n1"],
        data["n2"],
        data["n3"],
        data["n4"],
        data["n5"],
        data["superbalota"]
    )

    print("✅ Primer sorteo insertado correctamente")

else:
    print("❌ No se pudo obtener el sorteo:", data)
