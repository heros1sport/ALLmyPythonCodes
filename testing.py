import matplotlib.pyplot as plt
from keras.datasets.mnist import load_data
# load the images into memory
(trainX, trainy), (testX, testy) = load_data()
# summarize the shape of the dataset
print('Train', trainX.shape, trainy.shape)
print('Test', testX.shape, testy.shape)


# plot raw pixel data
while True:
    for i in trainX[int(input())]:
        lmaoo =""
        for j in i:
            if j < 1:
                lmaoo += "    "
            else:
                lmaoo += "####"
        print(lmaoo)
        
        print("\n")


