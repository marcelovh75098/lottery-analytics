"""
==================================================
Lottery Analytics SaaS
Archivo: engine/backtester.py

Backtester completamente robusto.

Características:

- Compatible con múltiples estructuras de registros.
- Detecta automáticamente dónde están los números.
- Evita errores IndexError.
- Mantiene la filosofía Walk Forward.
- Compatible con SQLite, CSV y futuras fuentes.
==================================================
"""

from engine.features import build_features


def _extract_numbers(draw):
    """
    ==================================================
    Extrae automáticamente los cinco números principales
    independientemente del formato del registro.

    Formatos soportados:

    (tipo, sorteo, fecha, n1, n2, n3, n4, n5, super)

    (id, tipo, sorteo, fecha, n1, n2, n3, n4, n5, super)

    (n1, n2, n3, n4, n5, super)

    (id, n1, n2, n3, n4, n5, super)

    Si el formato cambia en futuras versiones,
    se intentará localizar automáticamente cinco
    enteros consecutivos.
    ==================================================
    """

    if draw is None:
        return []

    size = len(draw)

    # -------------------------------------------------
    # Formato:
    # (tipo, sorteo, fecha, n1, n2, n3, n4, n5, super)
    # -------------------------------------------------
    if size == 9:
        return list(draw[3:8])

    # -------------------------------------------------
    # Formato:
    # (id, tipo, sorteo, fecha, n1, n2, n3, n4, n5, super)
    # -------------------------------------------------
    if size == 10:
        return list(draw[4:9])

    # -------------------------------------------------
    # Formato:
    # (n1,n2,n3,n4,n5,super)
    # -------------------------------------------------
    if size == 6:
        return list(draw[0:5])

    # -------------------------------------------------
    # Formato:
    # (id,n1,n2,n3,n4,n5,super)
    # -------------------------------------------------
    if size == 7:
        return list(draw[1:6])

    # -------------------------------------------------
    # Búsqueda automática.
    # Localiza cinco enteros consecutivos.
    # -------------------------------------------------
    numbers = []

    for value in draw:

        if isinstance(value, int):
            numbers.append(value)

            if len(numbers) == 5:
                return numbers

    return numbers[:5]


def evaluate(prediction, actual_draw):
    """
    ==================================================
    Evalúa la cantidad de aciertos.

    Devuelve:

        0
        1
        2
        3
        4
        5

    Nunca produce IndexError.
    ==================================================
    """

    actual_numbers = set(
        _extract_numbers(actual_draw)
    )

    prediction_numbers = set(prediction)

    return len(
        prediction_numbers.intersection(
            actual_numbers
        )
    )


def backtest(strategies, draws):
    """
    ==================================================
    WALK FORWARD BACKTEST

    Procedimiento:

    1. Se toma únicamente el histórico disponible.
    2. Se construyen features.
    3. La estrategia genera una predicción.
    4. Se compara con el siguiente sorteo.
    5. Se almacena el score.

    No existe look-ahead bias.

    Además:

    - Ignora registros incompletos.
    - Nunca interrumpe toda la simulación por una
      estrategia defectuosa.
    - Devuelve estadísticas listas para Streamlit.
    ==================================================
    """

    results = {}

    if not draws:
        return results

    for strategy in strategies:

        scores = []

        for i in range(len(draws) - 1):

            history = draws[: i + 1]

            next_draw = draws[i + 1]

            try:

                features = build_features(history)

                prediction = strategy.predict(features)

                score = evaluate(
                    prediction,
                    next_draw
                )

                scores.append(score)

            except Exception as error:

                print(
                    f"[BACKTEST][{strategy.name()}] "
                    f"Iteración {i} omitida: {error}"
                )

                continue

        results[strategy.name()] = scores

    return results
