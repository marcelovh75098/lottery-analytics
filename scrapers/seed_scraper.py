import random
from datetime import datetime, timedelta


# =========================================================
# GENERADOR DE DATOS DE PRUEBA
# =========================================================
def generar_sorteos_fake(n=50):
    """
    Genera datos simulados para pruebas del sistema institucional.
    """

    base_date = datetime.today()

    sorteos = []

    for i in range(n):

        fecha = (base_date - timedelta(days=i)).strftime("%Y-%m-%d")

        numeros = random.sample(range(1, 43), 5)
        superbalota = random.randint(1, 16)

        sorteos.append({
            "draw_date": fecha,
            "n1": numeros[0],
            "n2": numeros[1],
            "n3": numeros[2],
            "n4": numeros[3],
            "n5": numeros[4],
            "superbalota": superbalota
        })

    return sorteos


# =========================================================
# CARGAR EN DB (FAKE MODE)
# =========================================================
def cargar_fake_en_db(insert_draw, n=50):

    sorteos = generar_sorteos_fake(n)

    inserted = 0

    for s in sorteos:

        try:
            insert_draw(
                s["draw_date"],
                s["n1"],
                s["n2"],
                s["n3"],
                s["n4"],
                s["n5"],
                s["superbalota"]
            )

            inserted += 1

        except:
            continue

    return {
        "status": "ok",
        "inserted": inserted
    }
