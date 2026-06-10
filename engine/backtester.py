def evaluate_prediction(pred, actual):
    return len(set(pred) & set(actual[:5]))


def backtest(strategies, draws):

    results = {}

    for s in strategies:

        scores = []

        for i in range(len(draws) - 1):

            features_draw = draws[:i+1]
            actual = draws[i+1]

            features = {"history": features_draw}

            pred = s.predict(features)

            score = evaluate_prediction(pred, actual)

            scores.append(score)

        results[s.name()] = scores

    return results
