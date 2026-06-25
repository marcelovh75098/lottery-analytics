from collections import defaultdict


def build_global_score(
    analytics,
    weighted_consensus,
    predictions
):
    """
    ============================================
    GLOBAL SCORE ENGINE
    ============================================

    Score final para cada número.

    Combina:

    35% Analytics
    30% Consensus
    20% Momentum
    15% Hot Numbers

    ============================================
    """

    scores = defaultdict(float)

    #
    # Analytics
    #

    max_score = max(
        x["score"]
        for x in analytics.values()
    )

    for number, data in analytics.items():

        scores[number] += (
            (data["score"] / max_score)
            * 35
        )

    #
    # Weighted Consensus
    #

    max_consensus = max(
        weighted_consensus.values()
    )

    for number, value in weighted_consensus.items():

        scores[number] += (
            (value / max_consensus)
            * 30
        )

    #
    # Momentum
    #

    for pos, number in enumerate(
        predictions["momentum"]
    ):

        scores[number] += (
            (5 - pos)
            * 4
        )

    #
    # Hot Numbers
    #

    for pos, number in enumerate(
        predictions["hot_numbers"]
    ):

        scores[number] += (
            (5 - pos)
            * 3
        )

    ranking = sorted(

        scores.items(),

        key=lambda x: x[1],

        reverse=True

    )

    return ranking
