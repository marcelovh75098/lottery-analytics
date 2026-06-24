from collections import Counter


class HotNumbersStrategy:
    """
    ==================================================
    HOT NUMBERS STRATEGY
    ==================================================

    Utiliza únicamente los últimos 30 sorteos.

    Hipótesis:
    Los números que están apareciendo con frecuencia
    recientemente pueden continuar mostrando fuerza.

    Selecciona los 5 números más frecuentes del
    periodo reciente.
    ==================================================
    """

    def name(self):
        return "hot_numbers"

    def predict(self, features):

        recent_draws = features.get(
            "recent_draws",
            []
        )

        counter = Counter()

        for draw in recent_draws:

            counter.update([
                draw[3],
                draw[4],
                draw[5],
                draw[6],
                draw[7]
            ])

        if len(counter) == 0:
            return []

        return [
            number
            for number, _
            in counter.most_common(5)
        ]
