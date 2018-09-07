import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(777)


'''
axis

'''
a=np.arange(1,10).reshape(3,3)
#print(a)
#print(np.sum(a, 0))
#print(np.sum(a, 1))

m=np.max(a, axis=1)
#m=np.argmax(a, axis=0)
#print(m)

c=np.cumsum(a, axis=1)
#print(c)

me=np.mean(a, axis=0)
#print(me)

a=np.arange(1,25).reshape(4,6)
b=np.arange(25,49).reshape(4,6)

#print(a+b)

a=np.arange(5).reshape((1,5))

a=np.random.randint(0,9,(3,3))

'''
copy

'''
a1=np.copy(a)
a1[:,0]=99
#print(a1, a)

uns=np.random.random((3,3))
#print(uns)

'''
sort

'''
uns1=uns
uns2=uns
uns3=uns.copy()
uns1.argsort()

a=np.array([40,30,10,20])
j=np.argsort(a)
#print(j)
#print(a.take(j))

x=np.array([4,3,1,5,2,6,0])
xrev=np.sort(x)[::-1]
#print(xrev)


'''
axis

'''
#print(x[np.argsort(-x)])
#
arr=np.arange(0, 2*3*4)
v=arr.reshape([2,3,4])
print(v)
#print(v[:,:,:])

print(v.ndim)
print(v.shape)
print(v.sum(0))




























