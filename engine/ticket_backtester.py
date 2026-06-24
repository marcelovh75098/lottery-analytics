from engine.ticket_metrics import (
    compute_ticket_metrics
)


def evaluate_ticket(
    ticket,
    draw
):
    """
    ==================================================
    COMPARA BOLETO VS SORTEO
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


def backtest_tickets(
    tickets,
    draws
):
    """
    ==================================================
    BACKTEST DE BOLETOS

    tickets:

    {
        "momentum": [...],
        "balanced": [...],
        "conservative": [...]
    }

    ==================================================
    """

    results = {}

    for ticket_name, numbers in tickets.items():

        scores = []

        for draw in draws:

            score = evaluate_ticket(
                numbers,
                draw
            )

            scores.append(score)

        results[ticket_name] = {

            "numbers": numbers,

            "metrics":
                compute_ticket_metrics(
                    scores
                )

        }

    return results
