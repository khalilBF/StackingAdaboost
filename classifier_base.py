
import numpy as np

class Classifier:
    def __init__(self, K = 2):
        self.k = K

    def predict_score_of_an_example(self,x):
        raise NotImplementedError

    def predict_example(self,x):
        raise NotImplementedError

    def predict_score(self,X):
        return np.array(list(map(self.predict_score_of_an_example, X)))

    def predict(self,X):
        return np.array(list(map(self.predict, X)))