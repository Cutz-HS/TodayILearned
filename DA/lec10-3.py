import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import tensorflow as tf

np.random.seed(777)

''' 배열 합치기 '''
x=np.arange(18).reshape(3,6)
#print(x)
#print(np.hsplit(x,3))
#print(np.split(x, 3,axis=1))
#print(np.split(x, (2,4), axis=1))

x1,x2,x3=np.split(x, 3, axis=0)
#print(x1)
x=np.array([15,14,13,12,11,10,9])
#print(x.argmax())

x[x>=13]=100
#print(x)
x=np.array([1,2,3,1,2,4])
#print(np.unique(x))
y=np.array([3,4,6,5])
#print(np.intersect1d(x,y))
#print(np.union1d(x,y))
#print(np.setdiff1d(x,y))
#print(np.setxor1d(x,y))
x=np.array([1,2,3,4,5,6])
y=np.array([2,4])
#print(np.in1d(x,y))

a=np.array([1,2,3])
b=np.array([4,5,6])
#print(np.r_[a,b])
#print(np.hstack((a,b)))
#print(np.vstack((a,b)))
#print(np.r_[[a],[b]])
#print(np.column_stack((a,b)))
#print(np.vstack((a,b)))

#print(np.c_[a,b])

''' 차원 감소/증가 '''
x=np.arange(12).reshape(3,4)
#print(np.ravel(x, order='F'))

y=np.arange(12).reshape(4,3)
#print(np.ravel(y, order='C'))

#df=DataFrame(y)
#print(x.flatten())

''' matplotlib '''
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.ylabel("some numbers")
#plt.show()
data={'a':np.arange(50),
      'c':np.random.randint(0,50,50),
      'd':np.random.randn(50)}
#print(data)

data['b']=data['a']+10*np.random.randn(50)
#print(data)
data['d']=np.abs(data['d'])*100
#print(data)

#plt.scatter('a','b',data=data, c='b')
#plt.xlabel('entry a')
#plt.ylabel('entry b')
#plt.show()

mu, sigma=100, 15
x=np.array(mu+sigma*np.random.randn(10000))
n, bins, patches=plt.hist(x, bins=100, density=1)
plt.title("hist")
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()
#plt.hist(data['d'], bins=10)














































