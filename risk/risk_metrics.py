import numpy as np  # Librería matemática para calcular medias y desviaciones


def sharpe_like_score(hits):
    # 'hits' es una lista de aciertos por cada simulación del backtesting

    mean = np.mean(hits)
    # Calcula el promedio de aciertos → mide rendimiento general

    std = np.std(hits)
    # Calcula la desviación estándar → mide qué tan inestable es la estrategia

    if std == 0:
        # Si no hay variación, la estrategia no aporta información útil
        return 0

    return mean / std
    # Score final tipo financiero:
    # más alto = buena + estable
    # más bajo = mala o inestable
