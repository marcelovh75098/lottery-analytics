import streamlit as st
import pandas as pd

from database.db import (
    init_db,
    insert_draw,
    get_draws_ordered,
    run_backtest
)

from scrapers.baloto_scraper import obtener_ultimo_sorteo


# =========================
# INIT
# =========================
init_db()

st.set_page_config(
    page_title="Lottery Analytics Level 3",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Lottery Analytics - Nivel 3 (Backtesting)")

st.markdown("---")


# =========================
# ACTUALIZAR DATOS
# =========================
if st.button("Actualizar datos"):

    data = obtener_ultimo_sorteo()

    if data:

        insert_draw(
            data["draw_date"],
            data["n1"],
            data["n2"],
            data["n3"],
            data["n4"],
            data["n5"],
            data["superbalota"]
        )

        st.success("Sorteo guardado")


# =========================
# BACKTESTING
# =========================
if st.button("Ejecutar Backtesting"):

    results = run_backtest(window_size=20)

    if not results:
        st.warning("No hay suficientes datos")
        st.stop()

    df = pd.DataFrame(results)

    # promedio de precisión
    avg_score = df["score"].mean()

    st.metric("Precisión promedio (%)", round(avg_score, 2))

    st.line_chart(df["score"])


# =========================
# HISTORIAL
# =========================
st.subheader("Historial")

data = get_draws_ordered()

st.dataframe(data)
