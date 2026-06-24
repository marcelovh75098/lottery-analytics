from collections import Counter


def build_consensus(predictions):
    """
    ==================================================
    CONSENSUS ENGINE
    ==================================================

    Recibe predicciones de todas las estrategias.

    Devuelve los números más repetidos.

    Ejemplo:

    frequency -> [1,2,3,4,5]
    momentum  -> [2,3,4,5,6]

    consenso:

    2
    3
    4
    5

    ==================================================
    """

    counter = Counter()

    for numbers in predictions.values():

        counter.update(numbers)

    return dict(
        sorted(
            counter.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )
