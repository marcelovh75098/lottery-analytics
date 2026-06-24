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
from engine.recommendation import build_recommendations
from engine.ticket_backtester import (
    backtest_tickets
)

from strategies.frequency import FrequencyStrategy
from strategies.hot_numbers import HotNumbersStrategy
from strategies.cold_numbers import ColdNumbersStrategy
from strategies.momentum import MomentumStrategy
from strategies.meta_portfolio import MetaPortfolioStrategy

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Quant Engine")

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

st.subheader(
    "Engine Status"
)

st.write({

    "draws_loaded":
        total_draws,

    "strategies":
        5,

    "database":
        "ready"

})

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

if st.button(
    "Run Engine"
):

    results = backtest(
        strategies,
        draws
    )

    portfolio, metrics = build_portfolio(
        results
    )

    st.subheader(
        "Portfolio Ranking"
    )

    st.write(
        portfolio
    )

    st.subheader(
        "Strategy Metrics"
    )

    st.write(
        metrics
    )

features = build_features(
    draws
)

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

st.subheader(
    "Today's Picks"
)

st.write(
    predictions
)

consensus = build_consensus(
    predictions
)

st.subheader(
    "Consensus Picks"
)

st.write(
    consensus
)

recommendations = build_recommendations(
    predictions,
    consensus
)

st.subheader(
    "Recommended Tickets"
)

st.write(
    recommendations
)

ticket_results = backtest_tickets(

    {
        "conservative":
            recommendations[
                "conservative"
            ],

        "momentum":
            recommendations[
                "momentum"
            ],

        "balanced":
            recommendations[
                "balanced"
            ]
    },

    draws

)

st.subheader(
    "Ticket Backtest Results"
)

st.write(
    ticket_results
)

st.subheader(
    "Engine Summary"
)

st.write({

    "best_strategy":
        "momentum",

    "historical_draws":
        total_draws,

    "consensus_numbers":
        list(
            consensus.keys()
        )[:5],

    "recommended_ticket":
        recommendations[
            "balanced"
        ]

})
