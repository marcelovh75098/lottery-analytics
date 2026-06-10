import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/resultados"


def obtener_ultimo_sorteo():

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        tabla = soup.find("table")
        if not tabla:
            return {"error": "No se encontró tabla"}

        fila = tabla.find("tr")
        if not fila:
            return {"error": "No se encontró fila"}

        celdas = fila.find_all("td")

        if len(celdas) < 7:
            return {"error": "Estructura inválida"}

        return {
            "draw_date": celdas[0].get_text(strip=True),
            "n1": int(celdas[1].get_text(strip=True)),
            "n2": int(celdas[2].get_text(strip=True)),
            "n3": int(celdas[3].get_text(strip=True)),
            "n4": int(celdas[4].get_text(strip=True)),
            "n5": int(celdas[5].get_text(strip=True)),
            "superbalota": int(celdas[6].get_text(strip=True))
        }

    except Exception as e:
        return {"error": str(e)}
