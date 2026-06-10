from collections import Counter
import numpy as np


def build_features(draws):
    """
    Convierte historial en señales cuantitativas.
    """

    flat = []

    for d in draws:
        flat.extend(d[:5])

    freq = Counter(flat)

    total = sum(freq.values())

    freq_score = {k: v / total for k, v in freq.items()}

    return {
        "frequency": freq_score
    }
