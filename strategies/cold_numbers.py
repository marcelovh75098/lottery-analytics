from collections import Counter


class ColdNumbersStrategy:
    """
    ==================================================
    COLD NUMBERS STRATEGY
    ==================================================

    Analiza los últimos 100 sorteos.

    Hipótesis:
    Los números que llevan mucho tiempo sin aparecer
    podrían revertir hacia su frecuencia histórica.

    Selecciona los 5 menos frecuentes.
    ==================================================
    """

    def name(self):
        return "cold_numbers"

    def predict(self, features):

        recent_draws = features.get(
            "cold_window_draws",
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

        all_numbers = list(range(1, 44))

        for n in all_numbers:
            if n not in counter:
                counter[n] = 0

        ordered = sorted(
            counter.items(),
            key=lambda x: x[1]
        )

        return [
            number
            for number, _
            in ordered[:5]
        ]
