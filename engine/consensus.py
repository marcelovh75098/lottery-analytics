from collections import defaultdict


def build_consensus(predictions):
    """
    ==================================================
    WEIGHTED CONSENSUS ENGINE
    ==================================================

    Asigna puntuación considerando:

    - Calidad histórica de la estrategia
    - Posición dentro de la predicción

    Momentum      -> peso 5
    Hot Numbers   -> peso 4
    Cold Numbers  -> peso 3
    Meta          -> peso 2
    Frequency     -> peso 1

    Además:

    posición 1 = +5
    posición 2 = +4
    posición 3 = +3
    posición 4 = +2
    posición 5 = +1

    El resultado es un ranking mucho más robusto.
    ==================================================
    """

    strategy_weights = {

        "momentum": 5,

        "hot_numbers": 4,

        "cold_numbers": 3,

        "meta_portfolio": 2,

        "frequency": 1

    }

    scores = defaultdict(float)

    for strategy_name, numbers in predictions.items():

        strategy_weight = strategy_weights.get(
            strategy_name,
            1
        )

        for position, number in enumerate(numbers):

            rank_bonus = 5 - position

            scores[number] += (
                strategy_weight *
                rank_bonus
            )

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return dict(ranked)
