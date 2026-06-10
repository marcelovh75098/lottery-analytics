import streamlit as st

# =========================
# DB INIT (OBLIGATORIO PRIMERO)
# =========================
from database.db import init_db, get_all_draws, get_total_draws

init_db()  # 🔥 CREA LA TABLA ANTES DE TODO


# =========================
# ESTRATEGIAS
# =========================
from strategies.frequency import FrequencyStrategy
from strategies.hot import HotStrategy

# =========================
# MOTOR INSTITUCIONAL
# =========================
from engine.backtester import backtest
from engine.portfolio import build_portfolio
from engine.ensemble import ensemble_predict


# =========================
# CONFIG STREAMLIT
# =========================
st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Lottery Analytics - Institutional Engine")


# =========================
# BOTÓN PRINCIPAL
# =========================
if st.button("🚀 Ejecutar Motor Institucional"):

    draws = get_all_draws()

    # 🔥 protección contra DB vacía
    if not draws or len(draws) < 20:
        st.warning("No hay suficientes datos para ejecutar el sistema (mínimo 20 sorteos)")
        st.stop()

    strategies = [
        FrequencyStrategy(),
        HotStrategy()
    ]

    results = backtest(strategies, draws)

    portfolio, scores = build_portfolio(results)

    selected = [
        s for s in strategies if s.name() in portfolio
    ]

    prediction = ensemble_predict(selected, draws, scores)

    st.subheader("🏆 Portfolio")
    st.write(portfolio)

    st.subheader("📊 Scores")
    st.write(scores)

    st.subheader("🎯 Predicción")
    st.success(prediction)


# =========================
# HISTORIAL
# =========================
st.markdown("---")
st.subheader("📊 Historial de sorteos")

draws = get_all_draws()

if draws:
    st.write(draws)
else:
    st.info("Base de datos aún vacía. Ejecuta el scraper.")
