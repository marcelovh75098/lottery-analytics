import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/resultados"


# =========================================================
# OBTENER ÚLTIMO SORTEO (VERSIÓN ESTABLE)
# =========================================================
def obtener_ultimo_sorteo():

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # =========================
        # VALIDACIÓN DE TABLA
        # =========================
        tabla = soup.find("table")

        if tabla is None:
            return {"error": "No se encontró tabla en la página"}

        fila = tabla.find("tr")

        if fila is None:
            return {"error": "No se encontró fila de datos"}

        celdas = fila.find_all("td")

        if len(celdas) < 7:
            return {"error": "Estructura de datos inválida"}

        # =========================
        # EXTRACCIÓN SEGURA
        # =========================
        draw_date = celdas[0].get_text(strip=True)

        n1 = int(celdas[1].get_text(strip=True))
        n2 = int(celdas[2].get_text(strip=True))
        n3 = int(celdas[3].get_text(strip=True))
        n4 = int(celdas[4].get_text(strip=True))
        n5 = int(celdas[5].get_text(strip=True))

        superbalota = int(celdas[6].get_text(strip=True))

        # =========================
        # FORMATO COMPATIBLE DB
        # =========================
        resultado = {
            "draw_date": draw_date,  # 🔥 corregido (antes "fecha")
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "n4": n4,
            "n5": n5,
            "superbalota": superbalota
        }

        return resultado

    except Exception as e:
        return {"error": f"Error en scraper: {str(e)}"}
