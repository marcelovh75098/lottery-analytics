from engine.markov_strategy import MarkovStrategy
from engine.montecarlo_strategy import MonteCarloStrategy
from engine.bayesian_strategy import BayesianStrategy


class FrequencyStrategy:

    def name(self):

        return "frequency"

    def predict(self, features):

        freq = features["frequency"]

        return sorted(

            freq,

            key=freq.get,

            reverse=True

        )[:5]


def load_strategies():

    return [

        FrequencyStrategy(),

        MarkovStrategy(),

        MonteCarloStrategy(),

        BayesianStrategy()

    ]
