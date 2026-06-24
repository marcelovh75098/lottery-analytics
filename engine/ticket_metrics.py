from collections import Counter
import numpy as np


def compute_ticket_metrics(scores):
    """
    ==================================================
    TICKET METRICS
    ==================================================

    Evalúa un boleto fijo sobre todos los sorteos.

    ==================================================
    """

    distribution = Counter(scores)

    return {

        "mean_hits": float(
            np.mean(scores)
        ),

        "max_hits": int(
            max(scores)
        ),

        "distribution": {

            0: distribution.get(0, 0),

            1: distribution.get(1, 0),

            2: distribution.get(2, 0),

            3: distribution.get(3, 0),

            4: distribution.get(4, 0),

            5: distribution.get(5, 0)

        }

    }
