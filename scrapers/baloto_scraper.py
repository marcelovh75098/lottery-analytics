import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/resultados"


def _to_int(text):
    """
    Convierte un texto en entero.
    Si no es posible retorna None.
    """

    try:
        return int(text.strip())
    except:
        return None


def obtener_ultimo_sorteo():
    """
    Obtiene el último sorteo publicado.

    Devuelve un diccionario uniforme que será usado
    por el resto del motor.
    """

    try:

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64)"
            )
        }

        response = requests.get(
            URL,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        tablas = soup.find_all("table")

        if not tablas:

            return {
                "success": False,
                "error": "No se encontraron tablas."
            }

        tabla = tablas[0]

        filas = tabla.find_all("tr")

        if len(filas) < 2:

            return {
                "success": False,
                "error": "No existen filas."
            }

        for fila in filas[1:]:

            td = fila.find_all("td")

            if len(td) < 9:
                continue

            resultado = {

                "success": True,

                "tipo_sorteo": td[0].get_text(strip=True),

                "sorteo_id": _to_int(
                    td[1].get_text(strip=True)
                ),

                "draw_date": td[2].get_text(strip=True),

                "n1": _to_int(td[3].get_text(strip=True)),
                "n2": _to_int(td[4].get_text(strip=True)),
                "n3": _to_int(td[5].get_text(strip=True)),
                "n4": _to_int(td[6].get_text(strip=True)),
                "n5": _to_int(td[7].get_text(strip=True)),

                "superbalota": _to_int(
                    td[8].get_text(strip=True)
                )
            }

            if None not in (
                resultado["n1"],
                resultado["n2"],
                resultado["n3"],
                resultado["n4"],
                resultado["n5"],
                resultado["superbalota"]
            ):

                return resultado

        return {
            "success": False,
            "error": "No se encontró un sorteo válido."
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
