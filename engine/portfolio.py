from engine.metrics import compute_metrics


# =========================================================
# CONSTRUCCIÓN DE PORTAFOLIO INSTITUCIONAL
# =========================================================
def build_portfolio(results):

    metrics = {}

    # =========================
    # CALCULAR MÉTRICAS POR ESTRATEGIA
    # =========================
    for name, scores in results.items():

        metrics[name] = compute_metrics(scores)

    # =========================
    # RANKING TIPO HEDGE FUND
    # =========================
    ranked = sorted(
        metrics.items(),
        key=lambda x: x[1]["score_ratio"],
        reverse=True
    )

    # =========================
    # SELECCIÓN DE PORTAFOLIO
    # =========================
    portfolio = [r[0] for r in ranked]

    return portfolio, metrics
