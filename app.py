import streamlit as st

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws
)

from engine.bootstrap import bootstrap_if_empty
from engine.update_database import actualizar_base_datos
from engine.backtester import backtest
from engine.portfolio import build_portfolio


# ==================================================
# CONFIGURACIÓN
# ==================================================

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Quant Engine")


# ==================================================
# BASE DE DATOS
# ==================================================

init_db()

boot = bootstrap_if_empty()

update = actualizar_base_datos()

draws = get_all_draws()

total_draws = get_total_draws()


# ==================================================
# PANEL DE ESTADO
# ==================================================

st.subheader("Engine Status")

st.json({
    "bootstrap": boot,
    "database_update": update,
    "draws_loaded": total_draws
})


# ==================================================
# VALIDACIÓN
# ==================================================

if total_draws < 3:
    st.error("Dataset insuficiente.")
    st.stop()


# ==================================================
# ESTRATEGIA FRECUENCIA
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

    st.subheader("Ranking")

    st.write(portfolio)

    st.subheader("Métricas")

    st.write(metrics)
