import numpy as np
np.random.seed(1)
yes = 1
no = 0                       #smoking,drinking,exercise,obese
training_inputs =  np.array([[  yes  ,   yes  ,   no   , yes ],
                             [  no   ,   yes  ,   yes  , no  ],
                             [  no   ,   no   ,   yes  , no  ],
                             [  yes  ,   no   ,   yes  , no ]])
                                         #DIABETIC
training_outputs = np.array([[  yes  ,   no   ,   no   , no ]]).T

weights = 2 * np.random.random((4,1)) - 1

print("Weights before training : " + str(weights))
def sigmoid(x):
    x = 1 / ( 1 + np.exp(-x))
    return x
def sigmoid_derivative(x):
    x = x * ( 1 - x )
    return x
def think(inputs):
    inputs = inputs.astype(float)
    guess = sigmoid(np.dot(inputs, weights))
    return guess
for i in range(15000):
    
    output = think(training_inputs)

    error = training_outputs - output

    adjustments = np.dot(training_inputs.T, error * sigmoid_derivative(output))

    weights += adjustments

print("Weights after training : " + str(weights))
print("Error : " + str(error))

a = input('Smoking?? : ')
if a == 'yes':
    a = yes
if a == 'no':
    a = no
b = input('Drinking?? : ')
if b == 'yes':
    b = yes
if b == 'no':
    b = no
c = input('Exercise?? : ')
if c == 'yes':
    c = yes
if c == 'no':
    c = no
d = input('Obese?? : ')
if d == 'yes':
    d = yes
if d == 'no':
    d = no
print(str(think(np.array([[a,b,c,d]]))[0][0] * 100) + "%" + " Diabetic")
print("WOW, we did it!!")
# step 1 : trains on input and output based on how close its predictions are compared to the actual outputs
# step 2 : predict outcome of the given situatuation according to given pattern or data
