import streamlit as st
from datetime import date

from database.db import (
    init_db,
    get_all_draws,
    get_total_draws,
    save_prediction,
    get_predictions_history
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
from engine.number_analytics import (
    build_number_analytics
)

from strategies.frequency import FrequencyStrategy
from strategies.hot_numbers import HotNumbersStrategy
from strategies.cold_numbers import ColdNumbersStrategy
from strategies.momentum import MomentumStrategy
from strategies.meta_portfolio import MetaPortfolioStrategy


from engine.strategy_weights import (
    build_strategy_weights
)

from engine.weighted_consensus import (
    build_weighted_consensus
)

from engine.portfolio_generator import (
    generate_portfolios
)
from engine.portfolio_backtester import (
    backtest_portfolios
)
from engine.best_portfolio import (
    find_best_portfolio
)
from engine.hybrid_recommendation import (
    build_hybrid_recommendation
)
from engine.score_engine import (
    build_global_score
)
from engine.global_ranking import (
    build_global_ranking
)
from engine.ultimate_ticket import (
    build_ultimate_ticket
)

st.set_page_config(
    page_title="Lottery Quant Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Quant Engine")

# ==================================================
# DATABASE
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
# ENGINE STATUS
# ==================================================

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

results = backtest(
    strategies,
    draws
)

portfolio, metrics = build_portfolio(
    results
)

if st.button(
    "Run Engine"
):

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

# ==================================================
# FEATURES
# ==================================================

features = build_features(
    draws
)

# ==================================================
# PREDICTIONS
# ==================================================

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

# ==================================================
# BACKTEST AUTOMÁTICO
# ==================================================

results = backtest(
    strategies,
    draws
)

portfolio, metrics = build_portfolio(
    results
)

strategy_weights = build_strategy_weights(
    metrics
)

weighted_consensus = build_weighted_consensus(
    predictions,
    strategy_weights
)

# ==================================================
# CONSENSUS
# ==================================================

consensus = weighted_consensus

st.subheader(
    "Strategy Weights"
)

st.write(
    strategy_weights
)

st.subheader(
    "Weighted Consensus"
)

st.write(
    weighted_consensus
)

# ==================================================
# RECOMMENDATIONS
# ==================================================

recommendations = build_recommendations(
    predictions,
    weighted_consensus

)

st.subheader(
    "Recommended Tickets"
)

st.write(
    recommendations
)

# ==================================================
# TICKET BACKTEST
# ==================================================

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

# ==================================================
# NUMBER ANALYTICS
# ==================================================

analytics = build_number_analytics(
    draws
)
global_score = build_global_score(

    analytics,

    weighted_consensus,

    predictions

)
global_ranking = build_global_ranking(
    weighted_consensus,
    analytics
)

ranked_numbers = sorted(
    analytics.items(),
    key=lambda x: x[1]["score"],
    reverse=True
)

st.subheader(
    "Number Analytics"
)

for number, data in ranked_numbers[:10]:

    st.write({

        "number":
            number,

        "score":
            data["score"],

        "historical_count":
            data["historical_count"],

        "recent_30":
            data["recent_30"],

        "recent_100":
            data["recent_100"],

        "recent_200":
            data["recent_200"],

        "last_seen_draws_ago":
            data[
                "last_seen_draws_ago"
            ],

        "momentum_score":
            data[
                "momentum_score"
            ]

    })

# ==================================================
# TOP RANKED NUMBERS
# ==================================================

top_ranked_numbers = [

    number

    for number, _
    in ranked_numbers[:10]

]

st.subheader(
    "Top Ranked Numbers"
)

st.write(
    top_ranked_numbers
)
st.subheader(
    "Global Score Ranking"
)

for rank, (number, score) in enumerate(

    global_score[:20],

    start=1

):

    st.write({

        "rank": rank,

        "number": number,

        "score": round(score,4)

    })
# ==================================================
# GLOBAL RANKING
# ==================================================

st.subheader(
    "Global Ranking Top 20"
)

for position, (number, score) in enumerate(
    global_ranking[:20],
    start=1
):

    st.write({

        "rank": position,

        "number": number,

        "score": round(
            score,
            4
        )

    })
# ==================================================
# ELITE TICKET
# ==================================================

elite_ticket = [

    number

    for number, score

    in global_score[:5]

]
# ==================================================
# ELITE TICKET
# ==================================================

elite_ticket = build_hybrid_recommendation(
    weighted_consensus,
    ranked_numbers
)

st.subheader(
    "Elite Ticket"
)

st.write(
    elite_ticket
)

# ==================================================
# ELITE TICKET BACKTEST
# ==================================================

elite_results = backtest_tickets(

    {
        "elite": elite_ticket
    },

    draws

)

st.subheader(
    "Elite Ticket Backtest"
)

st.write(
    elite_results
)

# ==================================================
# BEST NUMBERS PORTFOLIO
# ==================================================
# ==================================================
# BEST NUMBERS PORTFOLIO
# ==================================================

portfolio_tickets = {

    "ticket_a":

        [
            number
            for number, _
            in ranked_numbers[:5]
        ],

    "ticket_b":

        [
            number
            for number, _
            in ranked_numbers[1:6]
        ],

    "ticket_c":

        [
            number
            for number, _
            in ranked_numbers[2:7]
        ]

}

st.subheader(
    "Best Numbers Portfolio"
)

st.write(
    portfolio_tickets
)

# ==================================================
# PORTFOLIO BACKTEST
# ==================================================

portfolio_results = backtest_portfolios(
    portfolio_tickets,
    draws
)

st.subheader(
    "Portfolio Backtest"
)

st.write(
    portfolio_results
)
best_portfolio = find_best_portfolio(
    portfolio_results
)

st.subheader(
    "Best Historical Portfolio"
)

st.write(
    best_portfolio
)

# ==================================================
# ENGINE SUMMARY
# ==================================================

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
        ],

    "top_ranked_numbers":
        top_ranked_numbers[:5]

})
