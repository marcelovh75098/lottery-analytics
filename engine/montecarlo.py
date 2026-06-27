import random
from collections import Counter


class MonteCarloEngine:
    """
    Simulación Monte Carlo para estimar
    los números con mayor probabilidad
    según la distribución histórica.
    """

    def __init__(self, draws):

        self.draws = draws

        self.weights = self._build_weights()

    def _build_weights(self):

        counter = Counter()

        for draw in self.draws:

            counter.update(draw[:5])

        total = sum(counter.values())

        if total == 0:
            total = 1

        return {

            n: counter.get(n, 0) / total

            for n in range(1, 44)

        }

    def simulate(self, simulations=10000):

        scores = Counter()

        population = list(self.weights.keys())

        weights = list(self.weights.values())

        for _ in range(simulations):

            ticket = random.choices(

                population,

                weights=weights,

                k=5

            )

            ticket = list(set(ticket))

            while len(ticket) < 5:

                ticket.append(

                    random.choice(population)

                )

                ticket = list(set(ticket))

            for n in ticket:

                scores[n] += 1

        ranking = sorted(

            scores.items(),

            key=lambda x: x[1],

            reverse=True

        )

        return ranking

    def best_ticket(self):

        ranking = self.simulate()

        return [

            n

            for n, _ in ranking[:5]

        ]
