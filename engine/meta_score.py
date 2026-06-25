from collections import defaultdict

def build_meta_score(
    analytics,
    weighted_consensus
):

    scores = defaultdict(float)

    for number, data in analytics.items():

        scores[number] += data["score"] * 5

        scores[number] += data["historical_count"] * 0.05

        scores[number] += data["recent_30"] * 2

        scores[number] += data["recent_100"] * 1.5

        scores[number] += data["recent_200"]

        scores[number] += data["momentum_score"] * 3

    for number, weight in weighted_consensus.items():

        scores[int(number)] += weight * 15

    ranking = sorted(

        scores.items(),

        key=lambda x: x[1],

        reverse=True

    )

    return ranking
