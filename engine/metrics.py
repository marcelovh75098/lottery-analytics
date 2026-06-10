import numpy as np


def compute_metrics(scores):
    """
    JUSTIFICACIÓN:
    Convierte resultados en métricas financieras simuladas.
    - mean_hits: rendimiento promedio
    - volatility: estabilidad
    - score_ratio: eficiencia tipo Sharpe ratio
    """

    avg = np.mean(scores)
    std = np.std(scores) + 1e-9

    return {
        "mean_hits": float(avg),
        "volatility": float(std),
        "score_ratio": float(avg / std)
    }
