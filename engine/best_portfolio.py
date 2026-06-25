def find_best_portfolio(
    portfolio_results
):
    """
    ==================================================
    BEST PORTFOLIO SELECTOR
    ==================================================

    Selecciona automáticamente el portafolio
    con mejor mean_hits histórico.
    ==================================================
    """

    best_name = None
    best_score = -1

    for name, data in portfolio_results.items():

        score = data["metrics"][
            "mean_hits"
        ]

        if score > best_score:

            best_score = score
            best_name = name

    return {

        "portfolio":
            best_name,

        "mean_hits":
            best_score,

        "numbers":
            portfolio_results[
                best_name
            ]["numbers"]

    }
