def evaluate_prediction(pred, actual):
    """
    JUSTIFICACIÓN:
    Mide aciertos entre predicción y resultado real.
    - Kernel básico de evaluación cuantitativa.
    """
    return len(set(pred) & set(actual[:5]))


def backtest(strategies, draws):
    """
    JUSTIFICACIÓN:
    Simula comportamiento histórico de estrategias.
    - Permite medir performance antes de producción.
    - Base de cualquier sistema cuantitativo.
    """

    results = {}

    for s in strategies:

        scores = []

        for i in range(len(draws) - 1):

            history = draws[:i+1]
            actual = draws[i+1]

            features = {"history": history}

            pred = s.predict(features)

            score = evaluate_prediction(pred, actual)

            scores.append(score)

        results[s.name()] = scores

    return results
