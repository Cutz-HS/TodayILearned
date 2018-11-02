import numpy as np

A = np.array([1,2,3,4])

# 내적 #
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
#print(np.dot(A, B))


def sigmoid(z):
    return 1. / (1 + np.exp(-z))

x = np.array([[1.0, 0.5]])

W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(x, W1) + b1
Z1 = sigmoid(A1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + b2
Z2 = sigmoid(A2)

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + b3

print(A3)