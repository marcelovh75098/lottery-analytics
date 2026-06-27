from database.db import insert_draw
from database.db import draw_exists

from scrapers.baloto_scraper import obtener_ultimo_sorteo


def auto_update():

    """
    Consulta Baloto.

    Si existe un sorteo nuevo
    lo agrega automáticamente.

    Si no existe simplemente continúa.
    """

    ultimo = obtener_ultimo_sorteo()

    if not ultimo["success"]:
        return ultimo

    if draw_exists(ultimo["sorteo_id"]):

        return {

            "success": True,

            "updated": False,

            "message": "Base de datos actualizada.",

            "draw": ultimo

        }

    insert_draw(

        ultimo["tipo_sorteo"],

        ultimo["sorteo_id"],

        ultimo["draw_date"],

        ultimo["n1"],
        ultimo["n2"],
        ultimo["n3"],
        ultimo["n4"],
        ultimo["n5"],

        ultimo["superbalota"]

    )

    return {

        "success": True,

        "updated": True,

        "message": "Nuevo sorteo agregado.",

        "draw": ultimo

    }
