import random


def simulate_ticket(ticket, simulations=10000):

    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    ticket_set = set(ticket)

    for _ in range(simulations):

        draw = set(
            random.sample(range(1, 44), 5)
        )

        hits = len(
            ticket_set.intersection(draw)
        )

        results[hits] += 1

    probabilities = {}

    for hits, count in results.items():

        probabilities[f"p_{hits}_hits"] = round(
            count / simulations,
            6
        )

    probabilities["expected_hits"] = round(

        sum(
            hits * count
            for hits, count in results.items()
        ) / simulations,

        6
    )

    probabilities["probability_3_plus"] = round(

        (
            results[3]
            + results[4]
            + results[5]
        ) / simulations,

        6
    )

    probabilities["probability_4_plus"] = round(

        (
            results[4]
            + results[5]
        ) / simulations,

        6
    )

    return probabilities
