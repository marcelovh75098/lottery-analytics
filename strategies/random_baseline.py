import random

class RandomStrategy:

    def name(self):
        return "random"

    def predict(self, features):
        return random.sample(range(1, 43), 5)
