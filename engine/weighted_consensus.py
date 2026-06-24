from collections import defaultdict


def build_weighted_consensus(
    predictions,
    strategy_weights
):
    """
    ==================================================
    WEIGHTED CONSENSUS ENGINE
    ==================================================

    Cada estrategia aporta votos ponderados.

    Una estrategia con mejor backtest tiene
    mayor influencia.

    Además se premian posiciones superiores.

    Ejemplo:

    posición 1 = 5 puntos
    posición 2 = 4 puntos
    posición 3 = 3 puntos
    posición 4 = 2 puntos
    posición 5 = 1 punto

    multiplicado por el peso histórico.
    ==================================================
    """

    scores = defaultdict(float)

    for strategy_name, numbers in predictions.items():

        weight = strategy_weights.get(
            strategy_name,
            0
        )

        for position, number in enumerate(numbers):

            rank_score = 5 - position

            scores[number] += (
                rank_score * weight
            )

    ordered = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return {

        number: round(score, 4)

        for number, score

        in ordered

    }
