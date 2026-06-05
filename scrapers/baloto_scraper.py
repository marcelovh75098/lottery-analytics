import requests
from bs4 import BeautifulSoup

URL = "https://www.baloto.com/filtro-historico-de-resultados"

def test_connection():

    response = requests.get(URL, timeout=30)

    print("STATUS:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    print("TITULO PAGINA:")
    print(soup.title.text if soup.title else "Sin titulo")

if __name__ == "__main__":
    test_connection()
