def score_ticket(ticket):
    """
    ==================================================
    TICKET QUALITY ENGINE
    ==================================================

    Evalúa calidad estructural.

    ==================================================
    """

    score = 0

    even = len(
        [n for n in ticket if n % 2 == 0]
    )

    odd = 5 - even

    if even in [2, 3]:
        score += 3

    low = len(
        [n for n in ticket if n <= 22]
    )

    high = 5 - low

    if low in [2, 3]:
        score += 3

    total = sum(ticket)

    if 80 <= total <= 150:
        score += 4

    return {

        "ticket": ticket,

        "quality_score": score,

        "even": even,

        "odd": odd,

        "low": low,

        "high": high,

        "sum": total

    }
