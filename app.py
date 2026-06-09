import streamlit as st

from database.db import get_total_draws, insert_draw
from scrapers.baloto_scraper import obtener_ultimo_sorteo

st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Analytics")

st.markdown("---")

# =========================
# BOTÓN ACTUALIZAR
# =========================
if st.button("Actualizar datos Baloto"):

    data = obtener_ultimo_sorteo()

    # 🔒 validación segura
    if data is None:
        st.error("El scraper no devolvió datos")
        st.stop()

    if isinstance(data, dict) and "error" in data:
        st.error(data["error"])
        st.stop()

    try:
        resultado = insert_draw(
            data["draw_date"],
            data["n1"],
            data["n2"],
            data["n3"],
            data["n4"],
            data["n5"],
            data["superbalota"]
        )

        st.success("Sorteo guardado correctamente")
        st.write(resultado)

    except Exception as e:
        st.error(f"Error insertando en DB: {str(e)}")

st.markdown("---")

# =========================
# TOTAL SORTEOS
# =========================
try:
    total = get_total_draws()

    if total is None:
        st.warning("No hay datos aún")
    else:
        st.metric("Total sorteos", total)

except Exception as e:
    st.error(f"Error: {str(e)}")
