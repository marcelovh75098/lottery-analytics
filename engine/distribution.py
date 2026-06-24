from collections import Counter


def build_hit_distribution(scores):
    """
    ==================================================
    HIT DISTRIBUTION
    ==================================================

    Cuenta cuántas veces una estrategia obtuvo:

    0 hits
    1 hit
    2 hits
    3 hits
    4 hits
    5 hits

    Esto permite evaluar mejor el comportamiento
    de una estrategia que simplemente usando medias.
    ==================================================
    """

    distribution = Counter(scores)

    return {

        0: distribution.get(0, 0),

        1: distribution.get(1, 0),

        2: distribution.get(2, 0),

        3: distribution.get(3, 0),

        4: distribution.get(4, 0),

        5: distribution.get(5, 0)

    }
