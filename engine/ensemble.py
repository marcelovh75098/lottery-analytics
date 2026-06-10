def ensemble_predict(strategies, features):

    votes = []

    for s in strategies:
        votes.extend(s.predict(features))

    # mayoría de votos
    return list(set(votes))[:5]
