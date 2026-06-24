from collections import Counter


def build_features(draws):
    """
    ==================================================
    FEATURE ENGINEERING
    ==================================================

    Estructura real de cada sorteo:

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

    Índices válidos:

    3 = n1
    4 = n2
    5 = n3
    6 = n4
    7 = n5

    JUSTIFICACIÓN:

    La versión anterior utilizaba:

        d[:5]

    lo que incluía:

        tipo_sorteo
        sorteo_id
        draw_date

    contaminando completamente las frecuencias.

    Esta versión utiliza exclusivamente los
    cinco números principales del Baloto.
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
