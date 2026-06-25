from collections import Counter


def evaluate_ticket(ticket, draw):
    """
    ==================================================
    EVALUATE TICKET
    ==================================================

    Cuenta cuántos aciertos tiene un boleto
    frente a un sorteo real.

    Estructura draw:

    (
        tipo_sorteo,
        sorteo_id,
        draw_date,
        n1,
        n2,
        n3,
        n4,
        n5,
        superbalota
    )
    ==================================================
    """

    draw_numbers = {
        draw[3],
        draw[4],
        draw[5],
        draw[6],
        draw[7]
    }

    ticket_numbers = set(ticket)

    return len(
        ticket_numbers.intersection(
            draw_numbers
        )
    )


def compute_metrics(scores):
    """
    ==================================================
    METRICS
    ==================================================
    """

    if len(scores) == 0:

        return {
            "mean_hits": 0,
            "max_hits": 0,
            "distribution": {}
        }

    distribution = Counter(scores)

    return {

        "mean_hits":
            sum(scores) / len(scores),

        "max_hits":
            max(scores),

        "distribution":
            dict(
                sorted(
                    distribution.items()
                )
            )
    }


def backtest_portfolios(
    portfolios,
    draws
):
    """
    ==================================================
    PORTFOLIO BACKTESTER
    ==================================================

    Evalúa:

    ticket_a
    ticket_b
    ticket_c
    ticket_d
    ticket_e

    contra todo el histórico.

    ==================================================
    """

    results = {}

    for portfolio_name, ticket in portfolios.items():

        scores = []

        for draw in draws:

            hits = evaluate_ticket(
                ticket,
                draw
            )

            scores.append(hits)

        results[portfolio_name] = {

            "numbers":
                ticket,

            "metrics":
                compute_metrics(
                    scores
                )
        }

    return results
