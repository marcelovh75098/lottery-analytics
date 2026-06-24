import numpy as np

from engine.distribution import (
    build_hit_distribution
)


def compute_metrics(scores):
    """
    ==================================================
    PERFORMANCE METRICS
    ==================================================
    """

    mean = np.mean(scores)

    std = np.std(scores) + 1e-9

    distribution = build_hit_distribution(
        scores
    )

    return {

        "mean_hits": float(mean),

        "volatility": float(std),

        "score_ratio": float(mean / std),

        "distribution": distribution

    }
