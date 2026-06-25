def build_hybrid_recommendation(
    weighted_consensus,
    ranked_numbers
):
    """
    ==================================================
    HYBRID RECOMMENDATION ENGINE
    ==================================================

    Combina:

    1. Weighted Consensus
    2. Number Analytics

    Objetivo:

    Construir un boleto utilizando
    las dos fuentes más fuertes del motor.

    ==================================================
    """

    ticket = []

    consensus_numbers = list(
        weighted_consensus.keys()
    )

    analytics_numbers = [

        number

        for number, _
        in ranked_numbers

    ]

    # ==================================================
    # TOP 2 CONSENSUS
    # ==================================================

    for number in consensus_numbers[:2]:

        if number not in ticket:

            ticket.append(number)

    # ==================================================
    # TOP 3 ANALYTICS
    # ==================================================

    for number in analytics_numbers:

        if number not in ticket:

            ticket.append(number)

        if len(ticket) >= 5:
            break

    return ticket
