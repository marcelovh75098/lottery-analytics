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

    Solo deben utilizarse los cinco números
    principales para construir las frecuencias.

    La versión anterior utilizaba d[:5] y mezclaba:

    - tipo_sorteo
    - sorteo_id
    - draw_date

    contaminando completamente las estadísticas.
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
            "frequency": {}
        }

    frequency = {
        number: count / total
        for number, count in freq.items()
    }

    return {
        "frequency": frequency
    }
