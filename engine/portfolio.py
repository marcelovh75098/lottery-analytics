from engine.metrics import compute_metrics


def build_portfolio(results):
    """
    JUSTIFICACIÓN:
    Construcción de portafolio cuantitativo.
    - Evalúa performance de cada estrategia.
    - Ordena por score_ratio (tipo Sharpe simplificado).
    - Selecciona estrategias más eficientes.
    """

    metrics = {}

    for name, scores in results.items():
        metrics[name] = compute_metrics(scores)

    ranked = sorted(
        metrics.items(),
        key=lambda x: x[1]["score_ratio"],
        reverse=True
    )

    portfolio = [r[0] for r in ranked]

    return portfolio, metrics
