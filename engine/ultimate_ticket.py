from collections import defaultdict


def build_ultimate_ticket(
    weighted_consensus,
    global_ranking,
    momentum_numbers
):

    scores = defaultdict(float)

    #
    # 40% consensus
    #

    for pos, number in enumerate(
        weighted_consensus.keys()
    ):

        scores[number] += (
            (20 - pos) * 0.4
        )

    #
    # 40% ranking
    #

    for pos, (number, _) in enumerate(
        global_ranking[:20]
    ):

        scores[number] += (
            (20 - pos) * 0.4
        )

    #
    # 20% momentum
    #

    for pos, number in enumerate(
        momentum_numbers
    ):

        scores[number] += (
            (5 - pos) * 0.2
        )

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [

        number

        for number, score

        in ranked[:5]

    ]
