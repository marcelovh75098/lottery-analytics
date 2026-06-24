import streamlit as st

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws
)

from engine.bootstrap import bootstrap_if_empty
from engine.backtester import backtest
from engine.portfolio import build_portfolio

from strategies.frequency import FrequencyStrategy
from strategies.hot_numbers import HotNumbersStrategy
from strategies.cold_numbers import ColdNumbersStrategy
from strategies.momentum import MomentumStrategy

# ==================================================
# CONFIGURACIÓN GENERAL
# ==================================================
# JUSTIFICACIÓN:
# Punto de entrada principal de Lottery Analytics.
# Carga base de datos, histórico, ejecuta estrategias
# y presenta ranking cuantitativo.
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

init_db()

# ==================================================
# BOOTSTRAP DE DATOS
# ==================================================
# Si la base está vacía:
# - carga CSV histórico
# - inserta sorteos
# - devuelve estado
# ==================================================

boot = bootstrap_if_empty()

st.write(boot)

# ==================================================
# CARGAR HISTÓRICO
# ==================================================

draws = get_all_draws()

total_draws = get_total_draws()

st.metric(
    "Total Draws",
    total_draws
)

# ==================================================
# VALIDACIÓN MÍNIMA
# ==================================================

if total_draws < 10:

    st.error(
        "Dataset insuficiente para ejecutar backtesting."
    )

    st.stop()

# ==================================================
# PANEL INFORMATIVO
# ==================================================

st.subheader("Engine Status")

st.write({
    "draws_loaded": total_draws,
    "strategies": 4,
    "database": "ready"
})

# ==================================================
# EJECUCIÓN DEL MOTOR
# ==================================================

if st.button("Run Engine"):

    strategies = [

        FrequencyStrategy(),

        HotNumbersStrategy(),

        ColdNumbersStrategy(),

        MomentumStrategy()

    ]

    results = backtest(
        strategies,
        draws
    )

    portfolio, metrics = build_portfolio(
        results
    )

    st.subheader("Portfolio Ranking")

    st.write(portfolio)

    st.subheader("Strategy Metrics")

    st.write(metrics)

    st.subheader("Detailed Metrics")

    for strategy_name, values in metrics.items():

        st.write(
            f"Strategy: {strategy_name}"
        )

        st.write(
            {
                "mean_hits": round(
                    values["mean_hits"],
                    4
                ),
                "volatility": round(
                    values["volatility"],
                    4
                ),
                "score_ratio": round(
                    values["score_ratio"],
                    4
                )
            }
        )
