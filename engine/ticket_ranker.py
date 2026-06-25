from engine.monte_carlo import (
    simulate_ticket
)


def rank_portfolios(
    portfolio_results,
    simulations=10000
):
    """
    ==================================================
    PORTFOLIO RANKER
    ==================================================

    Combina:

    - Backtest histórico
    - Monte Carlo

    ==================================================
    """

    ranking = []

    for name, data in portfolio_results.items():

        ticket = data["numbers"]

        historical_mean = data[
            "metrics"
        ][
            "mean_hits"
        ]

        montecarlo = simulate_ticket(
            ticket,
            simulations
        )

        ranking.append({

            "portfolio":
                name,

            "numbers":
                ticket,

            "historical_mean":
                historical_mean,

            "expected_hits":
                montecarlo[
                    "expected_hits"
                ],

            "probability_3_plus":
                montecarlo[
                    "probability_3_plus"
                ],

            "probability_4_plus":
                montecarlo[
                    "probability_4_plus"
                ]
        })

    ranking = sorted(

        ranking,

        key=lambda x: (

            x["historical_mean"],

            x["probability_3_plus"],

            x["probability_4_plus"]

        ),

        reverse=True
    )

    return ranking
