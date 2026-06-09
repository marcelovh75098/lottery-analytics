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
# BOTÓN PRINCIPAL
# =========================
if st.button("Actualizar datos Baloto"):

    resultado = insert_draw()

    # 🔒 PROTECCIÓN CONTRA NoneType
    if resultado is None:
        st.error("Error: la función no devolvió ninguna respuesta (None)")
    
    elif isinstance(resultado, dict) and "error" in resultado:
        st.error(resultado["error"])

    else:
        st.success("Datos actualizados correctamente")
        st.write(resultado)

st.markdown("---")

# =========================
# TOTAL DE SORTEOS
# =========================
try:
    total = get_total_draws()

    if total is None:
        st.warning("No se pudo obtener el total de sorteos")
    else:
        st.metric("Total sorteos guardados", total)

except Exception as e:
    st.error(f"Error cargando datos: {str(e)}")
