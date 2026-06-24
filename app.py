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
from strategies.meta_portfolio import MetaPortfolioStrategy

# ==================================================
# CONFIGURACIÓN GENERAL
# ==================================================
# Lottery Quant Engine
# Plataforma de análisis cuantitativo para Baloto.
# ==================================================

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Quant Engine")

# ==================================================
# INICIALIZACIÓN DE BASE DE DATOS
# ==================================================

init_db()

# ==================================================
# BOOTSTRAP DEL HISTÓRICO
# ==================================================
# Si la base está vacía:
# - Carga CSV histórico
# - Inserta sorteos
# - Devuelve estadísticas
# ==================================================

boot = bootstrap_if_empty()

st.write(boot)

# ==================================================
# CARGA DE DATOS
# ==================================================

draws = get_all_draws()

total_draws = get_total_draws()

st.metric(
    "Total Draws",
    total_draws
)

# ==================================================
# VALIDACIÓN
# ==================================================

if total_draws < 10:

    st.error(
        "Dataset insuficiente para ejecutar backtesting."
    )

    st.stop()

# ==================================================
# ESTADO DEL MOTOR
# ==================================================

st.subheader("Engine Status")

st.write({
    "draws_loaded": total_draws,
    "strategies": 5,
    "database": "ready"
})

# ==================================================
# EJECUCIÓN DEL MOTOR
# ==================================================

if st.button("Run Engine"):

    frequency = FrequencyStrategy()

    hot = HotNumbersStrategy()

    cold = ColdNumbersStrategy()

    momentum = MomentumStrategy()

    meta = MetaPortfolioStrategy(
        frequency,
        hot,
        cold,
        momentum
    )

    strategies = [

        frequency,

        hot,

        cold,

        momentum,

        meta

    ]

    results = backtest(
        strategies,
        draws
    )

    portfolio, metrics = build_portfolio(
        results
    )

    st.subheader("Portfolio Ranking")

    st.write(
        portfolio
    )

    st.subheader("Strategy Metrics")

    st.write(
        metrics
    )

    st.subheader("Detailed Metrics")

    for strategy_name, values in metrics.items():

        st.write(
            f"Strategy: {strategy_name}"
        )

        st.write({

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

        })

# ==================================================
# PREDICCIONES ACTUALES
# ==================================================
# Genera números usando TODO el histórico cargado.
# ==================================================

st.subheader("Today's Picks")

frequency = FrequencyStrategy()

hot = HotNumbersStrategy()

cold = ColdNumbersStrategy()

momentum = MomentumStrategy()

meta = MetaPortfolioStrategy(
    frequency,
    hot,
    cold,
    momentum
)

from engine.features import build_features

features = build_features(draws)

predictions = {

    "frequency":
        frequency.predict(features),

    "hot_numbers":
        hot.predict(features),

    "cold_numbers":
        cold.predict(features),

    "momentum":
        momentum.predict(features),

    "meta_portfolio":
        meta.predict(features)

}

st.write(
    predictions
)
