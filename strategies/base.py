class Strategy:
    def name(self):
        raise NotImplementedError

    def predict(self, features):
        raise NotImplementedError
