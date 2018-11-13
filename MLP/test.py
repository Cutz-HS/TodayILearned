import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[1, 2, 3, 4,], [46, 29, 10, 21], [81, 59, 90, 100]])

sort = np.argsort(arr[2,:])
res = arr[:, sort]
print(res)

# Q2
print(np.sum(arr, axis=1))

plt.scatter(arr[0], arr[1])