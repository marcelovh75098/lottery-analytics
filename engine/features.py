from collections import Counter


def build_features(draws):
    """
    Convierte historial en frecuencia simple.
    """

    flat = []
    for d in draws:
        flat.extend(d[:5])

    freq = Counter(flat)

    total = sum(freq.values())

    frequency = {k: v / total for k, v in freq.items()}

    return {"frequency": frequency}
