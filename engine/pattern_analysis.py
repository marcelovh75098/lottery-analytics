from collections import Counter


def analyze_patterns(draws):
    """
    ==================================================
    PATTERN ANALYSIS ENGINE
    ==================================================

    Analiza patrones históricos de los sorteos.

    Calcula:

    - Pares / Impares
    - Bajos / Altos
    - Suma total
    - Consecutivos

    ==================================================
    """

    even_odd = Counter()

    low_high = Counter()

    sums = []

    consecutive_counts = Counter()

    for draw in draws:

        numbers = sorted([

            draw[3],
            draw[4],
            draw[5],
            draw[6],
            draw[7]

        ])

        even = len(
            [n for n in numbers if n % 2 == 0]
        )

        odd = 5 - even

        even_odd[
            f"{even}-{odd}"
        ] += 1

        low = len(
            [n for n in numbers if n <= 22]
        )

        high = 5 - low

        low_high[
            f"{low}-{high}"
        ] += 1

        sums.append(
            sum(numbers)
        )

        consecutive = 0

        for i in range(4):

            if numbers[i + 1] - numbers[i] == 1:
                consecutive += 1

        consecutive_counts[
            consecutive
        ] += 1

    avg_sum = round(
        sum(sums) / len(sums),
        2
    )

    return {

        "even_odd_distribution":
            dict(even_odd),

        "low_high_distribution":
            dict(low_high),

        "average_sum":
            avg_sum,

        "consecutive_distribution":
            dict(consecutive_counts)

    }
