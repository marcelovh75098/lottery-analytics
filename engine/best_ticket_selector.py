from engine.ticket_quality import score_ticket


def select_best_ticket(portfolios):
    """
    ==================================================
    BEST TICKET SELECTOR
    ==================================================

    Selecciona el boleto con mejor calidad
    estructural.

    ==================================================
    """

    results = {}

    for name, ticket in portfolios.items():

        results[name] = score_ticket(
            ticket
        )

    ranked = sorted(

        results.items(),

        key=lambda x:
            x[1]["quality_score"],

        reverse=True

    )

    return {

        "best_ticket":
            ranked[0][0],

        "analysis":
            results

    }
