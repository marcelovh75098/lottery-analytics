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

        if len(filas) <= 1:
            return {
                "error": "No se encontraron sorteos"
            }

        fila = filas[1]

        columnas = fila.find_all("td")

        fecha = columnas[1].get_text(strip=True)

        resultado_texto = columnas[2].get_text(
            separator=" ",
            strip=True
        )

        numeros = resultado_texto.replace("-", " ").split()

        return {
            "fecha": fecha,
            "n1": numeros[0],
            "n2": numeros[1],
            "n3": numeros[2],
            "n4": numeros[3],
            "n5": numeros[4],
            "superbalota": numeros[5]
        }

    except Exception as e:

        return {
            "error": str(e)
        }
