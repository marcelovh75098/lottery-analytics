from collections import Counter


class MomentumStrategy:
    """
    ==================================================
    MOMENTUM STRATEGY
    ==================================================

    Compara frecuencia reciente contra frecuencia
    histórica.

    Hipótesis:
    Los números que aceleran su frecuencia pueden
    continuar haciéndolo.

    Score:

    frecuencia_30
    -
    frecuencia_200

    Selecciona los 5 mejores.
    ==================================================
    """

    def name(self):
        return "momentum"

    def predict(self, features):

        recent = features.get(
            "recent_draws",
            []
        )

        long_term = features.get(
            "long_term_draws",
            []
        )

        recent_counter = Counter()
        long_counter = Counter()

        for draw in recent:

            recent_counter.update([
                draw[3],
                draw[4],
                draw[5],
                draw[6],
                draw[7]
            ])

        for draw in long_term:

            long_counter.update([
                draw[3],
                draw[4],
                draw[5],
                draw[6],
                draw[7]
            ])

        scores = {}

        for n in range(1, 44):

            recent_freq = recent_counter[n]

            long_freq = long_counter[n]

            scores[n] = (
                recent_freq -
                long_freq
            )

        ordered = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            number
            for number, _
            in ordered[:5]
        ]
