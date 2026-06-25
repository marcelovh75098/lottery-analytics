from collections import defaultdict


def build_global_ranking(
    weighted_consensus,
    analytics
):
    """
    ==================================================
    GLOBAL RANKING ENGINE
    ==================================================

    Combina:

    1. Weighted Consensus
    2. Number Analytics Score

    Genera un ranking único de números.

    ==================================================
    """

    scores = defaultdict(float)

    #
    # Consensus
    #

    max_consensus = max(
        weighted_consensus.values()
    )

    for number, score in weighted_consensus.items():

        scores[number] += (
            score / max_consensus
        ) * 50

    #
    # Analytics
    #

    max_analytics = max(
        data["score"]
        for data in analytics.values()
    )

    for number, data in analytics.items():

        scores[number] += (
            data["score"] / max_analytics
        ) * 50

    ranked = sorted(

        scores.items(),

        key=lambda x: x[1],

        reverse=True

    )

    return ranked
