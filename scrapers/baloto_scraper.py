import re
import requests

from bs4 import BeautifulSoup


URL = "https://baloto.com/resultados?page=1"


def obtener_ultimo_sorteo():
    """
    Obtiene el último sorteo publicado
    desde la página oficial de Baloto.
    """

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
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

        tabla = soup.find(
            "table",
            id="results-table"
        )

        if tabla is None:

            return {
                "success": False,
                "error": "No existe la tabla."
            }

        fila = tabla.find("tbody").find("tr")

        columnas = fila.find_all("td")

        fecha = columnas[1].get_text(strip=True)

        texto = columnas[2].get_text(
            " ",
            strip=True
        )

        numeros = list(
            map(
                int,
                re.findall(r"\d+", texto)
            )
        )

        if len(numeros) != 6:

            return {
                "success": False,
                "error": "No se pudieron leer las balotas."
            }

        enlace = columnas[3].find("a")

        href = enlace["href"]

        sorteo = int(
            href.rstrip("/").split("/")[-1]
        )

        return {

            "success": True,

            "tipo_sorteo": "Baloto",

            "sorteo_id": sorteo,

            "draw_date": fecha,

            "n1": numeros[0],
            "n2": numeros[1],
            "n3": numeros[2],
            "n4": numeros[3],
            "n5": numeros[4],

            "superbalota": numeros[5]

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
