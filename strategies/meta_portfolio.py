class MetaPortfolioStrategy:
    """
    ==================================================
    META PORTFOLIO STRATEGY
    ==================================================

    Combina las señales de:

    - Momentum
    - Hot Numbers
    - Cold Numbers
    - Frequency

    Asigna pesos según el ranking obtenido
    durante el backtesting histórico.

    Momentum      = 40%
    Hot Numbers   = 30%
    Cold Numbers  = 20%
    Frequency     = 10%

    La salida son los 5 números con mayor
    puntuación agregada.
    ==================================================
    """

    def __init__(
        self,
        frequency_strategy,
        hot_strategy,
        cold_strategy,
        momentum_strategy
    ):

        self.frequency_strategy = frequency_strategy
        self.hot_strategy = hot_strategy
        self.cold_strategy = cold_strategy
        self.momentum_strategy = momentum_strategy

    def name(self):
        return "meta_portfolio"

    def predict(self, features):

        scores = {}

        weights = {
            "frequency": 0.10,
            "hot": 0.30,
            "cold": 0.20,
            "momentum": 0.40
        }

        predictions = {

            "frequency":
                self.frequency_strategy.predict(features),

            "hot":
                self.hot_strategy.predict(features),

            "cold":
                self.cold_strategy.predict(features),

            "momentum":
                self.momentum_strategy.predict(features)
        }

        for strategy_name, numbers in predictions.items():

            weight = weights[strategy_name]

            for position, number in enumerate(numbers):

                rank_bonus = 5 - position

                scores[number] = (
                    scores.get(number, 0)
                    + weight * rank_bonus
                )

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            number
            for number, score
            in ranked[:5]
        ]
