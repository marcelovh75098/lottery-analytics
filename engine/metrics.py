import numpy as np


def compute_metrics(scores):

    mean = np.mean(scores)
    std = np.std(scores) + 1e-9

    return {
        "mean_hits": float(mean),
        "volatility": float(std),
        "score_ratio": float(mean / std)
    }
