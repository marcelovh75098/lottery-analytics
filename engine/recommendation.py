def build_recommendations(
    predictions,
    consensus
):
    """
    ==================================================
    RECOMMENDATION ENGINE v2
    ==================================================

    Genera tres tipos de boletos:

    Conservative:
        Números con mayor consenso.

    Momentum:
        Mejor estrategia histórica.

    Balanced:
        Combina Momentum + Hot + Consensus
        evitando duplicados para generar un
        boleto realmente diferente.

    ==================================================
    """

    conservative = list(
        consensus.keys()
    )[:5]

    momentum = predictions[
        "momentum"
    ]

    balanced = []

    #
    # 1 número líder de Momentum
    #

    balanced.append(
        predictions["momentum"][0]
    )

    #
    # 2 números de Hot Numbers
    #

    for number in predictions["hot_numbers"]:

        if number not in balanced:

            balanced.append(number)

        if len(balanced) >= 3:
            break

    #
    # Completar con consenso
    #

    for number in consensus.keys():

        if number not in balanced:

            balanced.append(number)

        if len(balanced) >= 5:
            break

    return {

        "conservative":
            conservative,

        "momentum":
            momentum,

        "balanced":
            balanced

    }

