import random
from collections import defaultdict


def monte_carlo_simulation(
    weighted_consensus,
    simulations=10000,
    picks_per_ticket=5
):
    """
    ==================================================
    MONTE CARLO SIMULATION ENGINE
    ==================================================

    Utiliza el consenso ponderado como distribución
    de probabilidades.

    Ejecuta miles de simulaciones para estimar:

    - frecuencia esperada
    - probabilidad de aparecer
    - ranking probabilístico

    ==================================================
    """

    numbers = list(
        weighted_consensus.keys()
    )

    weights = list(
        weighted_consensus.values()
    )

    appearances = defaultdict(int)

    for _ in range(simulations):

        ticket = random.choices(
            population=numbers,
            weights=weights,
            k=picks_per_ticket
        )

        ticket = set(ticket)

        for number in ticket:
            appearances[number] += 1

    probabilities = {}

    for number in numbers:

        probabilities[number] = round(

            appearances[number]
            / simulations,

            4
        )

    ranked = dict(

        sorted(
            probabilities.items(),
            key=lambda x: x[1],
            reverse=True
        )

    )

    return ranked
