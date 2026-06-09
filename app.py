import streamlit as st

# =========================
# IMPORTACIÓN DE ESTRATEGIAS
# =========================
from strategies.frequency import FrequencyStrategy  # Estrategia por frecuencia histórica
from strategies.hot import HotStrategy  # Estrategia por números recientes

# =========================
# MOTOR INSTITUCIONAL
# =========================
from engine.backtester import backtest  # Simula desempeño histórico de estrategias
from engine.portfolio import build_portfolio  # Selecciona mejores estrategias
from engine.ensemble import ensemble_predict  # Combina estrategias en una sola predicción

# =========================
# BASE DE DATOS (YA EXISTE EN TU PROYECTO)
# =========================
from database.db import get_all_draws  # Trae todos los sorteos almacenados


# =========================
# CONFIGURACIÓN STREAMLIT
# =========================
st.set_page_config(
    page_title="Lottery Analytics - Institutional Engine",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Lottery Analytics - Institutional Quant Engine")
st.markdown("Sistema de evaluación de estrategias basado en backtesting y scoring financiero")


# =========================
# BOTÓN PRINCIPAL DEL SISTEMA
# =========================
if st.button("🚀 Ejecutar Motor Institucional"):

    # =========================
    # 1. CARGAR DATOS
    # =========================
    draws = get_all_draws()
    # Trae todos los sorteos desde SQLite para análisis histórico

    if not draws or len(draws) < 30:
        st.error("No hay suficientes datos para ejecutar el motor (mínimo 30 sorteos)")
        st.stop()

    # =========================
    # 2. DEFINIR ESTRATEGIAS
    # =========================
    strategies = [
        FrequencyStrategy(),  # estrategia basada en frecuencia histórica
        HotStrategy()         # estrategia basada en números recientes
    ]

    # =========================
    # 3. BACKTESTING
    # =========================
    results = backtest(strategies, draws)
    # Evalúa cómo habría funcionado cada estrategia en el pasado

    # =========================
    # 4. CONSTRUIR PORTAFOLIO INSTITUCIONAL
    # =========================
    portfolio, scores = build_portfolio(results)
    # Selecciona las mejores estrategias según scoring tipo financiero

    # =========================
    # 5. FILTRAR ESTRATEGIAS GANADORAS
    # =========================
    selected_strategies = [
        s for s in strategies if s.name() in portfolio
    ]
    # Solo usamos las estrategias más fuertes

    # =========================
    # 6. GENERAR PREDICCIÓN FINAL (ENSEMBLE)
    # =========================
    prediction = ensemble_predict(selected_strategies, draws, scores)
    # Combina estrategias con pesos para generar resultado final

    # =========================
    # 7. MOSTRAR RESULTADOS
    # =========================
    st.subheader("🏆 Portfolio Institucional (mejores estrategias)")
    st.write(portfolio)

    st.subheader("📊 Scores de estrategias (tipo financiero)")
    st.write(scores)

    st.subheader("🎯 Predicción del sistema (ensemble)")
    st.success(prediction)


# =========================
# VISUALIZACIÓN DE DATOS
# =========================
st.markdown("---")
st.subheader("📊 Historial de sorteos")

try:
    draws = get_all_draws()
    st.write(draws)

except Exception as e:
    st.error(f"Error cargando datos: {str(e)}")
