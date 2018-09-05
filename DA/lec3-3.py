import numpy as np

trees=np.loadtxt('../Data/trees.csv',delimiter=',',
                 skiprows=1, unpack=True)
print(trees.shape)#31행 3열 -> 3행 31열(unpack=True)
print(trees[:-1])#둘레, 높이
print("="*50)
print(trees[[-1]])#볼륨







