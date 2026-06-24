def build_recommendations(
    predictions,
    consensus
):
    """
    ==================================================
    RECOMMENDATION ENGINE
    ==================================================

    Genera tres boletos:

    Conservative
    Momentum
    Balanced

    ==================================================
    """

    conservative = list(
        consensus.keys()
    )[:5]

    momentum = predictions[
        "momentum"
    ]

    balanced = []

    for number in predictions["momentum"]:

        if number not in balanced:
            balanced.append(number)

    for number in predictions["hot_numbers"]:

        if number not in balanced:
            balanced.append(number)

    for number in consensus.keys():

        if number not in balanced:
            balanced.append(number)

    balanced = balanced[:5]

    return {

        "conservative": conservative,

        "momentum": momentum,

        "balanced": balanced

    }
