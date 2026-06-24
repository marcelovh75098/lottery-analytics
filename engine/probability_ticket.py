def build_probability_ticket(
    montecarlo_results
):
    """
    ==================================================
    MOST PROBABLE TICKET
    ==================================================

    Selecciona los cinco números con mayor
    probabilidad de aparición.

    ==================================================
    """

    return list(
        montecarlo_results.keys()
    )[:5]
