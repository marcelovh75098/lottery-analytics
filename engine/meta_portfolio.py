from collections import Counter


class MetaPortfolio:

    """
    Une las predicciones de todas
    las estrategias mediante votación.
    """

    def build(self, predictions):

        votes = Counter()

        for ticket in predictions:

            for number in ticket:

                votes[number] += 1

        ranking = sorted(

            votes.items(),

            key=lambda x: x[1],

            reverse=True

        )

        return [

            n

            for n, _ in ranking[:5]

        ]
