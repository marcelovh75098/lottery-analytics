from engine.montecarlo import MonteCarloEngine


class MonteCarloStrategy:

    def name(self):
        return "montecarlo"

    def predict(self, features):

        draws = features["draws"]

        engine = MonteCarloEngine(draws)

        return engine.best_ticket()
