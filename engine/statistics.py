from collections import Counter


def global_frequency(draws):
    """
    Calcula la frecuencia histórica de cada número.
    """

    counter = Counter()

    for draw in draws:
        counter.update(draw[:5])

    return dict(counter)


def recent_frequency(draws, window):
    """
    Calcula la frecuencia en una ventana reciente.
    """

    counter = Counter()

    recent = draws[-window:]

    for draw in recent:
        counter.update(draw[:5])

    return dict(counter)


def last_seen(draws):
    """
    Calcula cuántos sorteos han pasado desde la última aparición.
    """

    total = len(draws)

    result = {n: total for n in range(1, 44)}

    for index in range(total - 1, -1, -1):

        draw = draws[index][:5]

        for n in draw:

            if result[n] == total:
                result[n] = total - index - 1

    return result


def hot_numbers(draws, window=100):
    """
    Devuelve los números más frecuentes en una ventana.
    """

    freq = recent_frequency(draws, window)

    return sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )


def cold_numbers(draws, window=100):
    """
    Devuelve los números menos frecuentes.
    """

    freq = recent_frequency(draws, window)

    numbers = []

    for n in range(1, 44):
        numbers.append(
            (
                n,
                freq.get(n, 0)
            )
        )

    return sorted(
        numbers,
        key=lambda x: x[1]
    )
