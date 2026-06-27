from engine.strategy_manager import load_strategies


class Predictor:
    """
    Ejecuta todas las estrategias disponibles
    y genera sus predicciones.
    """

    def __init__(self):

        self.strategies = load_strategies()

    def predict(self, features):

        predictions = {}

        for strategy in self.strategies:

            predictions[
                strategy.name()
            ] = strategy.predict(features)

        return predictions
