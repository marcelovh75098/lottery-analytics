from engine.features import build_features


def evaluate(prediction, actual_draw):
    """
    ==================================================
    EVALUACIÓN DE ACIERTOS

    Estructura real:

    (
        tipo_sorteo,
        sorteo_id,
        draw_date,
        n1,
        n2,
        n3,
        n4,
        n5,
        superbalota
    )

    Se comparan únicamente los cinco números
    principales del sorteo.
    ==================================================
    """

    actual_numbers = {
        actual_draw[3],
        actual_draw[4],
        actual_draw[5],
        actual_draw[6],
        actual_draw[7]
    }

    prediction_numbers = set(prediction)

    return len(
        prediction_numbers.intersection(
            actual_numbers
        )
    )


def backtest(strategies, draws):
    """
    ==================================================
    WALK FORWARD BACKTEST

    Para cada punto temporal:

    1. Usa el histórico disponible.
    2. Construye features.
    3. Genera predicción.
    4. Evalúa contra el siguiente sorteo.

    Esto evita look-ahead bias.
    ==================================================
    """

    results = {}

    for strategy in strategies:

        scores = []

        for i in range(len(draws) - 1):

            history = draws[: i + 1]

            next_draw = draws[i + 1]

            features = build_features(history)

            prediction = strategy.predict(features)

            score = evaluate(
                prediction,
                next_draw
            )

            scores.append(score)

        results[
            strategy.name()
        ] = scores

    return results
