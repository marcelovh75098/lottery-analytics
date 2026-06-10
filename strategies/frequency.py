class FrequencyStrategy:

    def name(self):
        return "frequency"

    def predict(self, features):

        freq = features["frequency"]

        # top 5 números más frecuentes
        return sorted(freq, key=freq.get, reverse=True)[:5]
