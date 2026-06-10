import streamlit as st

from database.db import init_db, get_all_draws, get_total_draws
from engine.autopilot import ensure_data

from strategies.frequency import FrequencyStrategy
from strategies.hot import HotStrategy

from engine.backtester import backtest
from engine.portfolio import build_portfolio
from engine.ensemble import ensemble_predict


# =========================
# INIT SISTEMA
# =========================
init_db()


st.set_page_config(page_title="Lottery AI", layout="wide")
st.title("🏛️ Lottery Analytics - Autonomous Engine")


# =========================
# AUTOPILOTO (CLAVE)
# =========================
status = ensure_data(min_rows=30)

if status["status"] == "error":
    st.error("No se pudo inicializar el dataset")
    st.write(status)
    st.stop()


# =========================
# MOTOR INSTITUCIONAL
# =========================
if st.button("🚀 Ejecutar Motor Institucional"):

    draws = get_all_draws()

    strategies = [
        FrequencyStrategy(),
        HotStrategy()
    ]

    results = backtest(strategies, draws)

    portfolio, scores = build_portfolio(results)

    selected = [s for s in strategies if s.name() in portfolio]

    prediction = ensemble_predict(selected, draws, scores)

    st.subheader("🏆 Portfolio")
    st.write(portfolio)

    st.subheader("📊 Scores")
    st.write(scores)

    st.subheader("🎯 Predicción")
    st.success(prediction)


# =========================
# DATA STATUS
# =========================
st.markdown("---")
st.subheader("📊 Estado del sistema")

st.write(status)
st.metric("Total sorteos", get_total_draws())
