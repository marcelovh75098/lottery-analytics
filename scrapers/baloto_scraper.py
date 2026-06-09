import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/resultados"

def obtener_ultimo_sorteo():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Buscar la primera fila del sorteo (ajustado a estructura real)
        tabla = soup.find("table")
        fila = tabla.find("tr")

        celdas = fila.find_all("td")

        if len(celdas) < 7:
            print("❌ No se pudo leer el sorteo correctamente")
            return None

        fecha = celdas[0].get_text(strip=True)

        n1 = int(celdas[1].get_text(strip=True))
        n2 = int(celdas[2].get_text(strip=True))
        n3 = int(celdas[3].get_text(strip=True))
        n4 = int(celdas[4].get_text(strip=True))
        n5 = int(celdas[5].get_text(strip=True))

        superbalota = int(celdas[6].get_text(strip=True))

        resultado = {
            "fecha": fecha,
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "n4": n4,
            "n5": n5,
            "superbalota": superbalota
        }

        print("✅ Sorteo extraído correctamente:", resultado)
        return resultado

    except Exception as e:
        print("❌ Error en scraper:", e)
        return None
