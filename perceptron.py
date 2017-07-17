import numpy as np
from random import random


class Perceptron:
    def __init__(self,perc_size):
        self.n = perc_size
        # n+1 for bias
        self.weight = np.ones((self.n +1,1))
        # Learning rate
        self.mu = 0.01

        # Initialize random weights
        for i in range(np.size(self.weight)):
            self.weight[i] = random()*2-1


    def predict(self,inpt1):
        inpt = np.concatenate((inpt1,[[1]]))
        sum  = np.transpose(self.weight).dot(inpt)
        output = np.sign(sum)
        if output.all()==0:
            output = 1
        return int(output[0][0])

    def train(self,point):
        inpt = np.concatenate((point.arr,[[1]]))
        error = point.label - self.predict(point.arr)
        self.weight = self.weight + self.mu * error * inpt
