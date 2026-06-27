from engine.markov import predict_next


class MarkovStrategy:

    def name(self):
        return "markov"

    def predict(self, features):

        draws = features["draws"]

        return predict_next(draws)
