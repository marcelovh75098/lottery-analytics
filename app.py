import streamlit as st

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws
)

from engine.bootstrap import bootstrap_if_empty
from engine.update_database import actualizar_base_datos
from engine.features import build_features
from engine.backtester import backtest
from engine.portfolio import build_portfolio
from engine.ranking import build_global_ranking
from engine.strategy_manager import load_strategies
from engine.predictor import Predictor
from engine.elite import EliteEngine
from engine.report import build_report

from ui.dashboard import load_theme
from ui.sidebar import render_sidebar
from ui.kpi import render_kpis
from ui.status import render_status
from ui.ranking_table import render_ranking


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🎯",
    layout="wide"
)

load_theme()

render_sidebar()

st.title("🎯 Lottery Quant Engine")


# ============================================================
# BASE DE DATOS
# ============================================================

init_db()

boot = bootstrap_if_empty()

update = actualizar_base_datos()

draws = get_all_draws()

total_draws = get_total_draws()

if total_draws < 3:

    st.error("Dataset insuficiente.")

    st.stop()


# ============================================================
# FEATURES
# ============================================================

features = build_features(draws)


# ============================================================
# ESTRATEGIAS
# ============================================================

strategies = load_strategies()


# ============================================================
# BACKTEST
# ============================================================

results = backtest(
    strategies,
    draws
)

portfolio, metrics = build_portfolio(
    results
)


# ============================================================
# PREDICCIONES
# ============================================================

predictor = Predictor()

predictions = predictor.predict(
    features
)


# ============================================================
# ELITE ENGINE
# ============================================================

elite = EliteEngine().build(
    predictions,
    metrics
)


# ============================================================
# RANKING
# ============================================================

ranking = build_global_ranking(draws)


# ============================================================
# REPORTE
# ============================================================

report = build_report(

    elite,

    metrics,

    ranking

)


# ============================================================
# UI
# ============================================================

render_kpis(

    total_draws,

    len(strategies),

    report["summary"]["best_strategy"]

)

render_status(

    boot,

    update,

    total_draws

)


st.divider()

st.subheader("🎯 Ticket Elite")

st.success(

    report["ticket"]["elite"]

)


st.divider()

st.subheader("⚖️ Pesos del Modelo")

st.json(

    report["weights"]

)


st.divider()

st.subheader("📈 Métricas")

st.json(

    report["metrics"]

)


st.divider()

render_ranking(

    report["ranking"]

)
