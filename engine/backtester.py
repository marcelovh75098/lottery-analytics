def backtest(strategies, draws):
    # Función principal de simulación histórica (backtesting)

    results = {}
    # Diccionario donde guardamos resultados por estrategia

    for s in strategies:
        # Recorre cada estrategia

        hits = []
        # Lista de aciertos por cada simulación

        for i in range(20, len(draws)):
            # Empezamos en 20 para tener historial suficiente (evita sesgo)

            history = draws[:i]
            # Solo usamos pasado (evita "future leak")

            real = draws[i]
            # Sorteo real a predecir

            pred = s.predict(history)
            # Predicción de la estrategia

            hits.append(len(set(pred) & set(real)))
            # Cuenta cuántos números acertó (intersección)

        results[s.name()] = hits
        # Guarda resultados de la estrategia

    return results
    # Devuelve todas las métricas para análisis
