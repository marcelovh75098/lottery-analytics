def build_strategy_weights(metrics):
    """
    ==================================================
    STRATEGY WEIGHTS ENGINE
    ==================================================

    Convierte resultados históricos del backtest
    en pesos automáticos.

    Utiliza score_ratio como medida principal.

    Cuanto mejor sea la estrategia históricamente,
    mayor influencia tendrá en el consenso final.
    ==================================================
    """

    raw_scores = {}

    for strategy_name, strategy_metrics in metrics.items():

        raw_scores[strategy_name] = max(
            strategy_metrics["score_ratio"],
            0.0001
        )

    total = sum(raw_scores.values())

    weights = {}

    for strategy_name, score in raw_scores.items():

        weights[strategy_name] = score / total

    return weights
