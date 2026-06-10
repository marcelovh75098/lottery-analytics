import streamlit as st

from database.db import init_db, get_all_draws
from ingestion.seed_loader import load_seed
from database.db import get_total_draws

if get_total_draws() < 30:
    load_seed()
    from engine.bootstrap_data import ensure_bootstrap
from database.db import get_total_draws

bootstrap = ensure_bootstrap()

from engine.features import build_features
from engine.backtester import backtest
from engine.portfolio import build_portfolio
from engine.ensemble import ensemble_predict

from strategies.frequency import FrequencyStrategy
from strategies.random_baseline import RandomStrategy


init_db()

st.title("🏛️ Hedge Fund Quant Engine (Lottery Research)")

draws = get_all_draws()

if len(draws) < 30:
    st.warning("Insuficient data for institutional backtest")
    st.stop()


strategies = [
    FrequencyStrategy(),
    RandomStrategy()
]


# BACKTEST
results = backtest(strategies, draws)

# PORTFOLIO
portfolio, metrics = build_portfolio(results)

# FEATURES
features = build_features(draws)

# ENSEMBLE
selected = [s for s in strategies if s.name() in portfolio]
prediction = ensemble_predict(selected, features)


st.subheader("📊 Portfolio institucional")
st.write(portfolio)

st.subheader("📈 Métricas")
st.write(metrics)

st.subheader("🎯 Signal final")
st.success(prediction)
