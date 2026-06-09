import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/resultados"

def obtener_ultimo_sorteo():

    try:

        response = requests.get(
            URL,
            timeout=30
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        tabla = soup.find(
            "table",
            {"id": "results-table"}
        )

        if tabla is None:
            return {
                "error": "No se encontró results-table"
            }

        filas = tabla.find_all("tr")

        if len(filas) > 0:

            return {
                "html_primera_fila": str(filas[0])
            }

        return {
            "error": "No se encontraron filas"
        }

    except Exception as e:

        return {
            "error": str(e)
        }
