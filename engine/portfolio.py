from risk.risk_metrics import sharpe_like_score  # Importa métrica tipo financiera


def build_portfolio(strategy_results):
    # Construye portafolio de mejores estrategias

    scores = {}
    # Guardará score de cada estrategia

    for name, hits in strategy_results.items():
        # Recorre resultados del backtesting

        scores[name] = sharpe_like_score(hits)
        # Calcula score institucional (rendimiento + estabilidad)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    # Ordena estrategias de mejor a peor

    portfolio = [name for name, _ in ranked[:3]]
    # Selecciona top 3 estrategias (portafolio institucional)

    return portfolio, scores
    # Devuelve portafolio + scores
