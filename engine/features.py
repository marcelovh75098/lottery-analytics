from collections import Counter


def build_features(draws):
    """
    ==================================================
    FEATURE ENGINEERING
    ==================================================

    Estructura del sorteo:

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

    JUSTIFICACIÓN

    El motor necesita distintas ventanas temporales
    para soportar múltiples estrategias:

    frequency:
        Historial completo.

    hot_numbers:
        Últimos 30 sorteos.

    cold_numbers:
        Últimos 100 sorteos.

    momentum:
        Compara últimos 30 contra últimos 200.

    Todas las estrategias reciben la información
    desde un único punto centralizado.
    ==================================================
    """

    flat = []

    for draw in draws:

        flat.extend([
            draw[3],
            draw[4],
            draw[5],
            draw[6],
            draw[7]
        ])

    freq = Counter(flat)

    total = sum(freq.values())

    if total == 0:

        return {
            "frequency": {},
            "recent_draws": [],
            "cold_window_draws": [],
            "long_term_draws": []
        }

    frequency = {
        number: count / total
        for number, count in freq.items()
    }

    recent_draws = draws[-30:]

    cold_window_draws = draws[-100:]

    long_term_draws = draws[-200:]

    return {
        "frequency": frequency,
        "recent_draws": recent_draws,
        "cold_window_draws": cold_window_draws,
        "long_term_draws": long_term_draws
    }
