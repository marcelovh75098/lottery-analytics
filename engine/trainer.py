from engine.weights import StrategyWeights


class StrategyTrainer:
    """
    Aprende automáticamente los pesos de cada estrategia
    utilizando los resultados del backtesting.
    """

    def __init__(self):

        self.weights = StrategyWeights()

        self.metrics = {}

    def train(self, metrics):

        self.metrics = metrics

        self.weights.fit(metrics)

        return self.weights.get()

    def best_strategy(self):

        if not self.metrics:

            return None

        ranking = sorted(

            self.metrics.items(),

            key=lambda x: x[1]["score_ratio"],

            reverse=True

        )

        return ranking[0][0]

    def summary(self):

        return {

            "strategies": len(self.metrics),

            "best_strategy": self.best_strategy(),

            "weights": self.weights.get()

        }
