from database.db import (
    get_connection,
    insert_draw
)

from scrapers.baloto_scraper import (
    obtener_ultimo_sorteo
)


def actualizar_base_datos():
    """
    Consulta la página oficial de Baloto.

    Si el último sorteo no existe en SQLite,
    lo inserta automáticamente.

    Nunca duplica registros.
    """

    resultado = obtener_ultimo_sorteo()

    if not resultado.get("success", False):
        return resultado

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM baloto_draws
        WHERE sorteo_id=?
        """,
        (
            resultado["sorteo_id"],
        )
    )

    existe = cur.fetchone()[0]

    if existe > 0:

        conn.close()

        return {
            "success": True,
            "updated": False,
            "message": "La base ya está actualizada."
        }

    insert_draw(

        resultado["tipo_sorteo"],

        resultado["sorteo_id"],

        resultado["draw_date"],

        resultado["n1"],

        resultado["n2"],

        resultado["n3"],

        resultado["n4"],

        resultado["n5"],

        resultado["superbalota"]

    )

    conn.close()

    return {
        "success": True,
        "updated": True,
        "message": "Nuevo sorteo agregado.",
        "draw": resultado
    }
