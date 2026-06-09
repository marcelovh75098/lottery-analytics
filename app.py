import streamlit as st

from database.db import (
    init_db,
    insert_draw,
    get_total_draws,
    get_all_draws
)

from scrapers.baloto_scraper import obtener_ultimo_sorteo


# =========================
# INIT DB
# =========================
init_db()


# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Analytics")

st.markdown("---")


# =========================
# ACTUALIZAR DATOS
# =========================
if st.button("Actualizar datos Baloto"):

    data = obtener_ultimo_sorteo()

    if data is None:
        st.error("El scraper no devolvió datos")
        st.stop()

    if isinstance(data, dict) and "error" in data:
        st.error(data["error"])
        st.stop()

    resultado = insert_draw(
        data["draw_date"],
        data["n1"],
        data["n2"],
        data["n3"],
        data["n4"],
        data["n5"],
        data["superbalota"]
    )

    if isinstance(resultado, dict) and "error" in resultado:
        st.error(resultado["error"])
    else:
        st.success("Sorteo guardado correctamente")


st.markdown("---")


# =========================
# MÉTRICAS
# =========================
total = get_total_draws()
st.metric("Total sorteos", total)


# =========================
# TABLA DE SORTEOS
# =========================
st.subheader("Últimos sorteos")

data = get_all_draws()

if data:
    st.dataframe(data)
else:
    st.warning("No hay sorteos aún")
