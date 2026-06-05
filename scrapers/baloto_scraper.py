import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/resultados"

def obtener_ultimo_sorteo():

    try:

        response = requests.get(
            URL,
            timeout=30
        )

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        return {
            "fecha": "pendiente",
            "n1": 0,
            "n2": 0,
            "n3": 0,
            "n4": 0,
            "n5": 0,
            "superbalota": 0
        }

    except Exception as e:

        print(e)

        return None
