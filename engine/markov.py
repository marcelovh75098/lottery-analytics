from collections import defaultdict


def build_transition_matrix(draws):
    """
    Construye una matriz de transición entre sorteos consecutivos.
    """

    transitions = defaultdict(lambda: defaultdict(int))

    if len(draws) < 2:
        return transitions

    for i in range(len(draws) - 1):

        current = draws[i][:5]
        nxt = draws[i + 1][:5]

        for a in current:
            for b in nxt:
                transitions[a][b] += 1

    return transitions


def predict_next(draws):

    matrix = build_transition_matrix(draws)

    scores = defaultdict(int)

    if not draws:
        return []

    last = draws[-1][:5]

    for number in last:

        for nxt, value in matrix[number].items():
            scores[nxt] += value

    ranking = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [n for n, _ in ranking[:5]]
