from database.db import init_db, insert_draw
from scrapers.baloto_scraper import obtener_ultimo_sorteo


# =========================
# INICIALIZAR BASE DE DATOS
# =========================
init_db()
# Asegura que la tabla baloto_draws exista antes de todo


# =========================
# OBTENER DATOS DEL SCRAPER
# =========================
data = obtener_ultimo_sorteo()
# Trae el último sorteo desde la web


# =========================
# VALIDACIÓN DE DATOS
# =========================
if not data:
    print("❌ No se obtuvo información del scraper")

elif isinstance(data, dict) and "error" in data:
    print("❌ Error en scraper:", data["error"])

else:

    try:
        # =========================
        # INSERTAR EN BASE DE DATOS
        # =========================
        insert_draw(
            data["draw_date"],
            data["n1"],
            data["n2"],
            data["n3"],
            data["n4"],
            data["n5"],
            data["superbalota"]
        )

        print("✅ Sorteo insertado correctamente en la base de datos")

    except Exception as e:
        print("❌ Error insertando en DB:", str(e))
