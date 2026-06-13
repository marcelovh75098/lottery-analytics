from database.db import get_total_draws





def bootstrap_if_empty():

    """

    Ya NO cargamos datos ficticios.



    El histórico real será cargado desde el CSV.

    """



    total = get_total_draws()



    return {

        "status": "ready",

        "total_draws": total

    }
