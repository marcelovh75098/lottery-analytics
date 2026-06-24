from collections import Counter


def build_number_analytics(draws):
    """
    ==================================================
    NUMBER ANALYTICS ENGINE
    ==================================================

    Calcula métricas por número:

    - frecuencia histórica
    - frecuencia últimos 30 sorteos
    - frecuencia últimos 100 sorteos
    - frecuencia últimos 200 sorteos
    - momentum
    - última aparición
    - score global

    ==================================================
    """

    historical = Counter()
    recent_30 = Counter()
    recent_100 = Counter()
    recent_200 = Counter()

    last_seen = {}

    total_draws = len(draws)

    for index, draw in enumerate(draws):

        numbers = [
            draw[3],
            draw[4],
            draw[5],
            draw[6],
            draw[7]
        ]

        for n in numbers:

            historical[n] += 1

            last_seen[n] = (
                total_draws - index - 1
            )

    for draw in draws[-30:]:

        for n in [
            draw[3],
            draw[4],
            draw[5],
            draw[6],
            draw[7]
        ]:

            recent_30[n] += 1

    for draw in draws[-100:]:

        for n in [
            draw[3],
            draw[4],
            draw[5],
            draw[6],
            draw[7]
        ]:

            recent_100[n] += 1

    for draw in draws[-200:]:

        for n in [
            draw[3],
            draw[4],
            draw[5],
            draw[6],
            draw[7]
        ]:

            recent_200[n] += 1

    analytics = {}

    max_hist = max(
        historical.values()
    )

    for n in range(1, 44):

        hist_score = (
            historical[n] / max_hist
            if max_hist > 0
            else 0
        )

        momentum_score = (
            recent_30[n]
            -
            (
                recent_200[n] / 6.6667
            )
        )

        score = (

            hist_score * 0.30 +

            recent_30[n] * 0.40 +

            recent_100[n] * 0.20 +

            momentum_score * 0.10

        )

        analytics[n] = {

            "historical_count":
                historical[n],

            "recent_30":
                recent_30[n],

            "recent_100":
                recent_100[n],

            "recent_200":
                recent_200[n],

            "last_seen_draws_ago":
                last_seen.get(
                    n,
                    total_draws
                ),

            "momentum_score":
                round(
                    momentum_score,
                    4
                ),

            "score":
                round(
                    score,
                    4
                )

        }

    return analytics
