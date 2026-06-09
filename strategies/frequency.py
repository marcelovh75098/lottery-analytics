from collections import Counter  # Permite contar frecuencia de números


class FrequencyStrategy:
    # Estrategia basada en frecuencia histórica de aparición de números

    def name(self):
        # Nombre identificador de la estrategia
        return "frequency"

    def predict(self, history):
        # history = lista de sorteos anteriores

        numbers = []
        # Lista donde acumulamos todos los números históricos

        for row in history:
            # Recorre cada sorteo
            numbers.extend(row)
            # Agrega todos los números al listado general

        counter = Counter(numbers)
        # Cuenta cuántas veces aparece cada número

        return [num for num, _ in counter.most_common(6)]
        # Retorna los 6 números más frecuentes
