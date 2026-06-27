from collections import Counter


def build_features(draws):
    """
    Construye las características usadas por las estrategias.
    """

    flat = []

    for draw in draws:
        flat.extend(draw[:5])

    freq = Counter(flat)

    total = sum(freq.values())

    if total == 0:
        total = 1

    frequency = {

        k: v / total

        for k, v in freq.items()

    }

    return {

        "draws": draws,

        "frequency": frequency

    }
