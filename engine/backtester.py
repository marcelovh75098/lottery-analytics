from engine.features import build_features


def evaluate(pred, actual):
    return len(set(pred) & set(actual[:5]))


def backtest(strategies, draws):

    results = {}

    for s in strategies:

        scores = []

        for i in range(len(draws) - 1):

            history = draws[:i+1]
            actual = draws[i+1]

            features = build_features(history)

            pred = s.predict(features)

            scores.append(evaluate(pred, actual))

        results[s.name()] = scores

    return results
