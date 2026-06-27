from engine.bayesian import BayesianEngine


class BayesianStrategy:

    def name(self):

        return "bayesian"

    def predict(self, features):

        engine = BayesianEngine(

            features["draws"]

        )

        return engine.best_ticket()
