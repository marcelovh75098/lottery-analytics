from engine.consensus import weighted_consensus


class TicketGenerator:

    def generate(

        self,

        predictions,

        weights

    ):

        ticket = weighted_consensus(

            predictions,

            weights

        )

        return {

            "elite": ticket

        }
