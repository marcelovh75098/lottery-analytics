from engine.metrics import compute_metrics


def build_portfolio(results):

    metrics = {}

    for name, scores in results.items():
        metrics[name] = compute_metrics(scores)

    ranked = sorted(metrics.items(),
                    key=lambda x: x[1]["score_ratio"],
                    reverse=True)

    return [r[0] for r in ranked], metrics
