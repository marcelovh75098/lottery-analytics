import streamlit as st

# =========================
# DB INIT (OBLIGATORIO PRIMERO)
# =========================
from database.db import init_db, get_all_draws, get_total_draws

# =========================
# AUTOPILOT (CEREBRO DEL SISTEMA)
# =========================
from engine.autopilot import ensure_data

# =========================
# MOTOR INSTITUCIONAL
# =========================
from strategies.frequency import FrequencyStrategy
from strategies.hot import HotStrategy

from engine.backtester import backtest
from engine.portfolio import build_portfolio
from engine.ensemble import ensemble_predict


# =========================================================
# CONFIG STREAMLIT
# =========================================================
st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Lottery Analytics - Institutional Engine")


# =========================================================
# 1. INICIALIZACIÓN SISTEMA (CRÍTICO)
# =========================================================
init_db()

bootstrap = ensure_data(min_rows=30)

st.markdown("### 📡 Estado del sistema")
st.write(bootstrap)
st.metric("Total sorteos", get_total_draws())


# =========================================================
# 2. MOTOR INSTITUCIONAL
# =========================================================
if st.button("🚀 Ejecutar Motor Institucional"):

    draws = get_all_draws()

    # 🔒 seguridad contra base vacía
    if not draws or len(draws) < 30:
        st.error("No hay suficientes datos para ejecutar el motor (mínimo 30 sorteos)")
        st.stop()

    # =========================
    # ESTRATEGIAS
    # =========================
    strategies = [
        FrequencyStrategy(),
        HotStrategy()
    ]

    # =========================
    # BACKTEST
    # =========================
    results = backtest(strategies, draws)

    # =========================
    # PORTFOLIO
    # =========================
    portfolio, scores = build_portfolio(results)

    selected = [s for s in strategies if s.name() in portfolio]

    # =========================
    # PREDICCIÓN FINAL
    # =========================
    prediction = ensemble_predict(selected, draws, scores)

    # =========================
    # OUTPUT
    # =========================
    st.subheader("🏆 Portfolio Institucional")
    st.write(portfolio)

    st.subheader("📊 Scores de Estrategias")
    st.write(scores)

    st.subheader("🎯 Predicción del Sistema")
    st.success(prediction)


# =========================================================
# 3. HISTORIAL
# =========================================================
st.markdown("---")
st.subheader("📊 Historial de sorteos")

draws = get_all_draws()

if draws and len(draws) > 0:
    st.write(draws)
else:
    st.warning("Base de datos aún vacía. Autopilot intentando cargar datos...")
