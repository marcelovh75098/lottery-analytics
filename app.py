import streamlit as st

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws
)

from engine.bootstrap import bootstrap_if_empty
from engine.backtester import backtest
from engine.portfolio import build_portfolio

# ==================================================
# CONFIGURACIÓN GENERAL DE STREAMLIT
# ==================================================

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Quant Engine")

# ==================================================
# INICIALIZAR BASE DE DATOS
# ==================================================
# Crea la base de datos y las tablas si no existen
# ==================================================

init_db()

# ==================================================
# CARGAR DATOS INICIALES SI LA BASE ESTÁ VACÍA
# ==================================================
# bootstrap_if_empty() intenta cargar el histórico
# desde el CSV cuando la tabla está vacía.
# ==================================================

boot = bootstrap_if_empty()

st.write(boot)

# ==================================================
# CARGAR HISTÓRICO DESDE SQLITE
# ==================================================

draws = get_all_draws()

total_draws = get_total_draws()

st.metric(
    "Total Draws",
    total_draws
)

# ==================================================
# VALIDACIÓN DE DATOS
# ==================================================
# El motor necesita al menos algunos sorteos para
# poder ejecutar métricas y backtesting.
# ==================================================

if total_draws < 3:
    st.error(
        "Dataset insuficiente. Debe cargar el histórico primero."
    )
    st.stop()

# ==================================================
# ESTRATEGIA DE FRECUENCIA
# ==================================================
# Estrategia simple:
# selecciona los 5 números más frecuentes.
# ==================================================

class FrequencyStrategy:

    def name(self):
        return "frequency"

    def predict(self, features):

        freq = features["frequency"]

        return sorted(
            freq,
            key=freq.get,
            reverse=True
        )[:5]

# ==================================================
# EJECUCIÓN DEL MOTOR
# ==================================================

if st.button("Run Engine"):

    strategies = [
        FrequencyStrategy()
    ]

    results = backtest(
        strategies,
        draws
    )

    portfolio, metrics = build_portfolio(
        results
    )

    st.subheader("Portfolio")
    st.write(portfolio)

    st.subheader("Metrics")
    st.write(metrics)
