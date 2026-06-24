import streamlit as st

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws
)

from engine.bootstrap import bootstrap_if_empty
from engine.backtester import backtest
from engine.portfolio import build_portfolio
from engine.features import build_features
from engine.consensus import build_consensus

from strategies.frequency import FrequencyStrategy
from strategies.hot_numbers import HotNumbersStrategy
from strategies.cold_numbers import ColdNumbersStrategy
from strategies.momentum import MomentumStrategy
from strategies.meta_portfolio import MetaPortfolioStrategy

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Quant Engine")

# ==================================================
# DB
# ==================================================

init_db()

boot = bootstrap_if_empty()

st.write(boot)

draws = get_all_draws()

total_draws = get_total_draws()

st.metric(
    "Total Draws",
    total_draws
)

if total_draws < 10:

    st.error(
        "Dataset insuficiente."
    )

    st.stop()

# ==================================================
# STATUS
# ==================================================

st.subheader("Engine Status")

st.write({

    "draws_loaded": total_draws,

    "strategies": 5,

    "database": "ready"

})

# ==================================================
# STRATEGIES
# ==================================================

frequency = FrequencyStrategy()

hot = HotNumbersStrategy()

cold = ColdNumbersStrategy()

momentum = MomentumStrategy()

meta = MetaPortfolioStrategy(
    frequency,
    hot,
    cold,
    momentum
)

strategies = [

    frequency,

    hot,

    cold,

    momentum,

    meta

]

# ==================================================
# BACKTEST
# ==================================================

if st.button("Run Engine"):

    results = backtest(
        strategies,
        draws
    )

    portfolio, metrics = build_portfolio(
        results
    )

    st.subheader("Portfolio Ranking")

    st.write(portfolio)

    st.subheader("Strategy Metrics")

    st.write(metrics)

    st.subheader("Detailed Metrics")

    for strategy_name, values in metrics.items():

        st.write(
            f"Strategy: {strategy_name}"
        )

        st.write(values)

# ==================================================
# TODAY PICKS
# ==================================================

st.subheader("Today's Picks")

features = build_features(draws)

predictions = {

    "frequency":
        frequency.predict(features),

    "hot_numbers":
        hot.predict(features),

    "cold_numbers":
        cold.predict(features),

    "momentum":
        momentum.predict(features),

    "meta_portfolio":
        meta.predict(features)

}

st.write(predictions)

# ==================================================
# CONSENSUS PICKS
# ==================================================

st.subheader("Consensus Picks")

consensus = build_consensus(
    predictions
)

st.write(consensus)

top_consensus = list(
    consensus.keys()
)[:5]

st.subheader(
    "Top Consensus Numbers"
)

st.write(
    top_consensus
)
