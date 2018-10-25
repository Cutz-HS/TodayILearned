import math
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(777)

def sigmoid(z):
    return 1. / (1. + np.exp(-z))

#print(sigmoid(-10))
#print(sigmoid(0))
#print(sigmoid(30))
    
X = np.arange(-100, 100, 0.1).reshape(2000, 1)
y = np.zeros([2000, 1])
y[:1000, :] = np.ones([1000, 1])
np.random.shuffle(y)
W = np.array([[0.1]])

hypothesis = sigmoid(np.matmul(X, W))
#
plt.figure()
plt.plot(np.matmul(X, W), hypothesis)
plt.show()
#
cost = (np.sum(np.square(hypothesis - y))) / len(X)
costList = []
wList = []

for i in range(-1000, 1000, 10):
    W[0][0] = i * 0.01
    cost = (np.sum(np.square(hypothesis - y))) / len(X)
    costList.append(cost)
    wList.append(i * 0.001)
#    
#
#plt.figure()
#plt.plot(wList, costList, 'r-')
#plt.show()