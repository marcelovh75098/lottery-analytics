import numpy as np


def compute_metrics(scores):

    avg = np.mean(scores)
    std = np.std(scores) + 1e-9

    sharpe_like = avg / std

    return {
        "mean_hits": avg,
        "volatility": std,
        "score_ratio": sharpe_like
    }
