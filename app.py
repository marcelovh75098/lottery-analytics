import streamlit as st

from database.db import init_db, get_all_draws, get_total_draws
from engine.bootstrap_data import ensure_bootstrap

from strategies.frequency import FrequencyStrategy
from strategies.hot import HotStrategy

from engine.backtester import backtest
from engine.portfolio import build_portfolio


# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(page_title="Hedge Fund Quant Engine", layout="wide")

st.title("🏛️ Hedge Fund Quant Engine (Lottery Research)")


# =========================
# INICIALIZACIÓN SISTEMA
# =========================
init_db()

bootstrap = ensure_bootstrap()


st.subheader("📡 Estado del sistema")
st.write(bootstrap)
st.metric("Total sorteos", get_total_draws())


# =========================
# CARGA DE DATOS
# =========================
draws = get_all_draws()


# =========================
# VALIDACIÓN INSTITUCIONAL
# =========================
if not draws or len(draws) < 5:

    st.error("Dataset no inicializado correctamente")
    st.write(bootstrap)
    st.stop()


# =========================
# MOTOR CUANTITATIVO
# =========================
if st.button("🚀 Ejecutar Backtest Institucional"):

    strategies = [
        FrequencyStrategy(),
        HotStrategy()
    ]

    results = backtest(strategies, draws)

    portfolio, metrics = build_portfolio(results)

    st.subheader("🏆 Portfolio Institucional")
    st.write(portfolio)

    st.subheader("📊 Métricas")
    st.write(metrics)
