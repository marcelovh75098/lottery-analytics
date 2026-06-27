from collections import Counter


def _extract_main_numbers(draw):
    """
    ============================================================
    Extrae siempre los cinco números principales del sorteo.

    Formatos soportados:

    (n1,n2,n3,n4,n5,super)

    (id,n1,n2,n3,n4,n5,super)

    (tipo,sorteo,fecha,n1,n2,n3,n4,n5,super)

    (id,tipo,sorteo,fecha,n1,n2,n3,n4,n5,super)

    Si el proyecto evoluciona y cambia el formato,
    se intentan localizar automáticamente cinco enteros.
    ============================================================
    """

    if draw is None:
        return []

    size = len(draw)

    if size == 6:
        return list(draw[0:5])

    if size == 7:
        return list(draw[1:6])

    if size == 9:
        return list(draw[3:8])

    if size == 10:
        return list(draw[4:9])

    numbers = []

    for value in draw:

        if isinstance(value, int):

            numbers.append(value)

            if len(numbers) == 5:
                break

    return numbers


def build_features(draws):
    """
    ============================================================
    Construcción central de Features.

    Este módulo es utilizado por todas las estrategias.

    Además de la frecuencia, genera estadísticas que serán
    utilizadas por los próximos motores predictivos sin tener
    que modificar nuevamente este archivo.

    El objetivo es mantener una única fuente de información
    para todo el Quant Engine.
    ============================================================
    """

    frequency_counter = Counter()

    last_10_counter = Counter()

    last_20_counter = Counter()

    even = 0

    odd = 0

    total_numbers = 0

    normalized_draws = []

    for draw in draws:

        numbers = _extract_main_numbers(draw)

        if len(numbers) != 5:
            continue

        normalized_draws.append(numbers)

        frequency_counter.update(numbers)

        total_numbers += len(numbers)

        for n in numbers:

            if n % 2 == 0:
                even += 1
            else:
                odd += 1

    for draw in normalized_draws[-10:]:

        last_10_counter.update(draw)

    for draw in normalized_draws[-20:]:

        last_20_counter.update(draw)

    if total_numbers == 0:
        total_numbers = 1

    frequency = {}

    for number in range(1, 44):

        frequency[number] = (
            frequency_counter[number] / total_numbers
        )

    last10_frequency = {}

    total10 = sum(last_10_counter.values())

    if total10 == 0:
        total10 = 1

    for number in range(1, 44):

        last10_frequency[number] = (
            last_10_counter[number] / total10
        )

    last20_frequency = {}

    total20 = sum(last_20_counter.values())

    if total20 == 0:
        total20 = 1

    for number in range(1, 44):

        last20_frequency[number] = (
            last_20_counter[number] / total20
        )

    return {

        "draws": normalized_draws,

        "total_draws": len(normalized_draws),

        "frequency": frequency,

        "last10_frequency": last10_frequency,

        "last20_frequency": last20_frequency,

        "global_counter": frequency_counter,

        "last10_counter": last_10_counter,

        "last20_counter": last_20_counter,

        "even": even,

        "odd": odd,

        "total_numbers": total_numbers

    }
