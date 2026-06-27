from collections import Counter


def evaluate_ticket(ticket, draws):

    distribution = Counter()

    total_hits = 0

    maximum = 0

    games = 0

    for draw in draws:

        hits = len(

            set(ticket)

            &

            set(draw[:5])

        )

        distribution[hits] += 1

        total_hits += hits

        maximum = max(

            maximum,

            hits

        )

        games += 1

    return {

        "mean_hits":

            total_hits / games,

        "max_hits":

            maximum,

        "distribution":

            dict(distribution)

    }
