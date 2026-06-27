from database.db import (
    draw_exists,
    insert_draw
)

from scrapers.baloto_scraper import (
    obtener_ultimo_sorteo
)


def actualizar_base_datos():
    """
    Consulta el último sorteo publicado.

    Si ya existe en SQLite no hace nada.

    Si es nuevo lo agrega automáticamente.
    """

    ultimo = obtener_ultimo_sorteo()

    if not ultimo["success"]:
        return ultimo

    if draw_exists(ultimo["sorteo_id"]):

        return {
            "success": True,
            "updated": False,
            "message": "La base ya está actualizada.",
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
        "message": "Nuevo sorteo agregado correctamente.",
        "draw": ultimo
    }
