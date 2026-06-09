def ensemble_predict(strategies, history, weights):
    # Combina varias estrategias (votación ponderada)

    votes = {}
    # Diccionario de votación de números

    for s in strategies:
        # Recorre estrategias seleccionadas

        pred = s.predict(history)
        # Predicción de cada estrategia

        weight = weights.get(s.name(), 1)
        # Peso según rendimiento (estrategias mejores pesan más)

        for n in pred:
            # Recorre números predichos

            votes[n] = votes.get(n, 0) + weight
            # Suma votos ponderados

    ranked = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    # Ordena por votos (más probables primero)

    return [n for n, _ in ranked[:6]]
    # Devuelve top 6 números recomendados
