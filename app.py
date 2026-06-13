import streamlit as st

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws
)

from engine.bootstrap import bootstrap_if_empty
from engine.backtester import backtest
from engine.portfolio import build_portfolio


# =====================================
# CONFIGURACIÓN
# =====================================

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Lottery Quant Engine")

# =====================================
# INIT
# =====================================

init_db()

boot = bootstrap_if_empty()

st.write(boot)

# =====================================
# DATA
# =====================================

draws = get_all_draws()

st.metric(
    "Total Draws",
    get_total_draws()
)

# =====================================
# VALIDACIÓN
# =====================================

if len(draws) < 3:
    st.error("Dataset insuficiente")
    st.stop()

# =====================================
# ESTRATEGIA SIMPLE
# =====================================

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

# =====================================
# EJECUCIÓN
# =====================================

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
