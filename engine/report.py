def build_report(

    elite,

    metrics,

    ranking

):
    """
    Construye un reporte único para la interfaz.
    """

    return {

        "summary": elite["summary"],

        "weights": elite["weights"],

        "ticket": elite["ticket"],

        "metrics": metrics,

        "ranking": ranking

    }
