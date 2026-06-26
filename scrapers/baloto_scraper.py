import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/resultados"

def obtener_ultimo_sorteo():
"""
Obtiene el último sorteo publicado en Baloto.

```
Retorna:
    {
        tipo_sorteo,
        sorteo_id,
        draw_date,
        n1,
        n2,
        n3,
        n4,
        n5,
        superbalota
    }
"""

try:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
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

    tabla = soup.find("table")

    if tabla is None:
        return {
            "success": False,
            "error": "No se encontró la tabla de resultados."
        }

    filas = tabla.find_all("tr")

    if len(filas) < 2:
        return {
            "success": False,
            "error": "No existen sorteos."
        }

    ultima = filas[1]

    td = ultima.find_all("td")

    if len(td) < 9:
        return {
            "success": False,
            "error": "Formato inesperado de la página."
        }

    return {

        "success": True,

        "tipo_sorteo": td[0].get_text(strip=True),

        "sorteo_id": int(
            td[1].get_text(strip=True)
        ),

        "draw_date": td[2].get_text(strip=True),

        "n1": int(td[3].get_text(strip=True)),
        "n2": int(td[4].get_text(strip=True)),
        "n3": int(td[5].get_text(strip=True)),
        "n4": int(td[6].get_text(strip=True)),
        "n5": int(td[7].get_text(strip=True)),

        "superbalota": int(
            td[8].get_text(strip=True)
        )
    }

except Exception as e:

    return {
        "success": False,
        "error": str(e)
    }
```

