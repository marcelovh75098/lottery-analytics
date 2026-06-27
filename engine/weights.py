class StrategyWeights:
    """
    Administra los pesos históricos
    de cada estrategia.
    """

    def __init__(self):

        self.weights = {}

    def fit(self, metrics):

        total = 0

        for name, data in metrics.items():

            score = data["score_ratio"]

            self.weights[name] = score

            total += score

        if total == 0:
            total = 1

        for name in self.weights:

            self.weights[name] /= total

    def get(self):

        return self.weights
