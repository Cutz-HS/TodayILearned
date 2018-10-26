import numpy as np

np.random.seed(777)

## softmax ##
def sigmoid(z):
    return 1. / (1. + np.exp(-z))

def hypothesis(W, X):
    return np.matmul(X, W)

def softmax(y):
    return np.exp(y) / (np.sum(np.exp(y), axis=1)).reshape(len(y), 1)

W = np.random.normal(size=[3, 3])
X = np.random.normal(size=[1, 3]) * 10

hp = hypothesis(W, X)
sig = sigmoid(hp)
print(sig)
sm = softmax(sig)
print(sm)