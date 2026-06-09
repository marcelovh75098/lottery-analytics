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

        filas_info = []

        for i, fila in enumerate(filas):

            filas_info.append(
                {
                    "fila": i,
                    "columnas": len(
                        fila.find_all("td")
                    )
                }
            )

        return {
            "total_filas": len(filas),
            "detalle": filas_info
        }

    except Exception as e:

        return {
            "error": str(e)
        }
