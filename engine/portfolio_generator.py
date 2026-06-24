def generate_portfolios(
    weighted_consensus
):
    """
    ==================================================
    PORTFOLIO GENERATOR
    ==================================================

    Genera múltiples boletos utilizando
    los números mejor clasificados.

    Ticket A:
    Top 5

    Ticket B:
    Posiciones 2-6

    Ticket C:
    Posiciones 3-7

    Ticket D:
    Posiciones 4-8

    Ticket E:
    Posiciones 5-9

    ==================================================
    """

    ranked_numbers = list(
        weighted_consensus.keys()
    )

    return {

        "ticket_a":
            ranked_numbers[0:5],

        "ticket_b":
            ranked_numbers[1:6],

        "ticket_c":
            ranked_numbers[2:7],

        "ticket_d":
            ranked_numbers[3:8],

        "ticket_e":
            ranked_numbers[4:9]

    }
