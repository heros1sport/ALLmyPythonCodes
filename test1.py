import numpy
import math
training_inputs = [[1,5,0],
                   [2,3,1],
                   [2.5,3,1],
                   [1,4,0],
                   [3,2,1]]
w1 = numpy.random.randn()
w2 = numpy.random.randn()

def sigmoid(x):
    return 1 / ( 1 - numpy.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

def think(a1,a2):
    return sigmoid(w1 * a1 + w2 * a2)

for i in range(15000):
    for j in training_inputs:
        output = think(j[0],j[1])
        error = j[2] - output
        w1 += j[0] * error * sigmoid_derivative(output)
        w2 += j[1] * error * sigmoid_derivative(output)
        print(error)
