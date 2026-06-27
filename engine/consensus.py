from collections import defaultdict


def weighted_consensus(predictions, weights):
    """
    Une todas las estrategias
    mediante voto ponderado.
    """

    scores = defaultdict(float)

    for strategy, ticket in predictions.items():

        weight = weights.get(strategy, 0)

        for number in ticket:

            scores[number] += weight

    ranking = sorted(

        scores.items(),

        key=lambda x: x[1],

        reverse=True

    )

    return [

        n

        for n, _ in ranking[:5]

    ]
