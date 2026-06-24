def analyze_ticket_risk(ticket):
    """
    ==================================================
    RISK ANALYSIS
    ==================================================

    Analiza:

    - pares/impares
    - bajos/altos
    - dispersión

    ==================================================
    """

    even = len(
        [n for n in ticket if n % 2 == 0]
    )

    odd = len(
        [n for n in ticket if n % 2 != 0]
    )

    low = len(
        [n for n in ticket if n <= 22]
    )

    high = len(
        [n for n in ticket if n > 22]
    )

    return {

        "ticket": ticket,

        "even_numbers": even,

        "odd_numbers": odd,

        "low_numbers": low,

        "high_numbers": high,

        "balance_score":
            min(even, odd)
            +
            min(low, high)

    }
