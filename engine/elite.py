from engine.ticket_generator import TicketGenerator
from engine.trainer import StrategyTrainer


class EliteEngine:
    """
    Genera el mejor boleto utilizando
    el rendimiento histórico de las estrategias.
    """

    def __init__(self):

        self.trainer = StrategyTrainer()

        self.generator = TicketGenerator()

    def build(

        self,

        predictions,

        metrics

    ):

        weights = self.trainer.train(metrics)

        ticket = self.generator.generate(

            predictions,

            weights

        )

        return {

            "ticket": ticket,

            "weights": weights,

            "summary": self.trainer.summary()

        }
