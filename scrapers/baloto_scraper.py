import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/filtro-historico-de-resultados"

def test_connection():

    try:

        response = requests.get(URL, timeout=30)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("Conexion exitosa con Baloto")
        else:
            print("Error al conectar")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_connection()
