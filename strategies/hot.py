from collections import Counter  # Para contar ocurrencias recientes


class HotStrategy:
    # Estrategia basada en los números más recientes

    def name(self):
        # Identificador de la estrategia
        return "hot"

    def predict(self, history):
        # history = historial completo de sorteos

        recent = history[-10:]
        # Solo usamos los últimos 10 sorteos (recencia = tendencia)

        numbers = []
        # Lista para guardar números recientes

        for row in recent:
            numbers.extend(row)
            # Aplanamos los últimos sorteos

        counter = Counter(numbers)
        # Contamos frecuencia reciente

        return [num for num, _ in counter.most_common(6)]
        # Retorna los 6 números más repetidos recientemente
