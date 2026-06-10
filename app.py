import streamlit as st

from database.db import init_db, get_all_draws, get_total_draws
from engine.bootstrap_data import ensure_bootstrap


# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Hedge Fund Engine", layout="wide")

st.title("🏛️ Hedge Fund Quant Engine")


# =========================
# 🔥 1. INICIALIZAR DB (PRIMERO SIEMPRE)
# =========================
init_db()


# =========================
# 🔥 2. BOOTSTRAP (DESPUÉS DE INIT)
# =========================
bootstrap = ensure_bootstrap()


# =========================
# 🔥 3. AHORA SÍ SE PUEDE CONSULTAR DB
# =========================
total = get_total_draws()


st.subheader("📡 Estado del sistema")
st.write(bootstrap)
st.metric("Total sorteos", total)


# =========================
# 🔥 4. CARGA DE DATOS
# =========================
draws = get_all_draws()


# =========================
# 🔥 5. VALIDACIÓN SEGURA
# =========================
if not draws or len(draws) < 5:

    st.error("Dataset no inicializado correctamente")
    st.stop()


# =========================
# 🔥 6. MOTOR CUANTITATIVO
# =========================
if st.button("🚀 Ejecutar Backtest"):

    from strategies.frequency import FrequencyStrategy
    from strategies.hot import HotStrategy
    from engine.backtester import backtest
    from engine.portfolio import build_portfolio

    strategies = [
        FrequencyStrategy(),
        HotStrategy()
    ]

    results = backtest(strategies, draws)

    portfolio, metrics = build_portfolio(results)

    st.write(portfolio)
    st.write(metrics)
