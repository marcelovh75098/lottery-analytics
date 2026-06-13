import streamlit as st

from database.db import init_db, get_all_draws, get_total_draws
from engine.backtester import backtest
from engine.portfolio import build_portfolio


# =========================
# INIT SEGURO
# =========================
st.title("🏛️ Lottery Quant Engine")

init_db()
boot = bootstrap_if_empty()


st.write(boot)


# =========================
# DATA
# =========================
draws = get_all_draws()

st.metric("Total draws", get_total_draws())


# =========================
# SAFE CHECK
# =========================
if len(draws) < 3:
    st.error("Dataset insuficiente")
    st.stop()


# =========================
# STRATEGY SIMPLE (inline para evitar imports rotos)
# =========================
class FrequencyStrategy:

    def name(self):
        return "frequency"

    def predict(self, features):
        freq = features["frequency"]
        return sorted(freq, key=freq.get, reverse=True)[:5]


# =========================
# RUN
# =========================
if st.button("Run Engine"):

    strategies = [FrequencyStrategy()]

    results = backtest(strategies, draws)

    portfolio, metrics = build_portfolio(results)

    st.write(portfolio)
    st.write(metrics)
