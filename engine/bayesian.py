from collections import Counter


class BayesianEngine:
    """
    Ranking Bayesiano utilizando frecuencia histórica
    y suavizado de Laplace.
    """

    def __init__(self, draws):

        self.draws = draws

        self.counter = Counter()

        for draw in draws:

            self.counter.update(draw[:5])

        self.total = sum(self.counter.values())

    def probability(self, number):

        return (

            self.counter.get(number, 0) + 1

        ) / (

            self.total + 43

        )

    def ranking(self):

        ranking = []

        for number in range(1, 44):

            ranking.append({

                "number": number,

                "probability": self.probability(number)

            })

        ranking.sort(

            key=lambda x: x["probability"],

            reverse=True

        )

        return ranking

    def best_ticket(self):

        ranking = self.ranking()

        return [

            row["number"]

            for row in ranking[:5]

        ]
