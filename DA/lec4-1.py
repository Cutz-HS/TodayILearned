import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

np.random.seed(777)

#print(np.__version__)



list1=[1,2,3,4]
arr1=np.array(list1)
#print(type(arr1))

b=np.array([[1,2,3], [4,5,6]])
#print(b.shape)

#data=np.random.randn(1,2*100000000)
#ans=[]
#start=time.time()
#for i in list(data):
#    ans.append(2*i)
#end=time.time()
#print(ans,"\nres:",end-start)

#data_a=np.array(data)
#start=time.time()
#print(data_a*2)
#end=time.time()
#print("time:", end-start)

a=np.array([1,2,3])
b=np.array([10,20,30])
#print(a*2+b)

a=np.zeros((2,2))
b=np.ones((5,5))
a=np.full((2,3),"a")
a=np.eye(5)
#print(a)

b=np.array(range(20)).reshape(4,5)
#print(len(b))
#print(len(b[0]))
#print(b.ndim) # 행렬의 rank와 다르다 // Array의 차원

c=np.random.randn(5,5)
#print(c.ndim)
c_df=DataFrame(c)
#print(b>10)
#print(b[b>10])

arr=np.arange(0, 3*2*4)
#print(arr)

v=arr.reshape([3,2,4])
#print(v)
#print(len(v))
#print(len(v[0]))
#print(len(v[0][0]))

a=np.arange(0, 3*4).reshape(3,4)
#print(a)

b=np.array([0,1,2,3,4])
#print(b[2])
#print(b[-1])
#
#print("차원", np.ndim(a))
#print(a[0,1])
#print(a[0, :2])
#print(a[:,1])
#print(a[1,1:])

a=np.array([[1,2],[3,4],[5,6]])
#print(a.shape)
#print(a[[0,1,2], [0,1,0]])
#print(a.ndim)
#print(np.array([a[0,1],a[1,1], a[2,0]]))

#print(type(a[0,0]))

s=a[[0,1], [1,1]]
#print(s)

x=np.array([[1,2,3],
     [4,5,6],
     [7,8,9]])

lst1=np.array(range(1,10)).reshape(3,3)

bool_ind_arr=np.array([
        [False, True, False],
        [True, False, True],
        [False, True, False]
        ])

res=x[bool_ind_arr]

bool_ind=(x%2==0)
#print(bool_ind)

#print(x[x%2==0])

a=np.array([[1,2,3], [4,5,6]]).reshape(2,3)
b=np.ones_like(a)
#print(b)

a=np.linspace(0,10)
#print(a)
#plt.plot(a, 'o')
#plt.show()

a=np.arange(0, 10, 2, np.float)
#print(a)
#plt.plot(a, 'o')
#plt.show()

a=np.random.normal(0,1, 10000)
#print(a)
#plt.hist(a,bins=150)
#plt.show()
a=np.random.rand(10000)
#plt.hist(a,bins=100)
#plt.show()
a=np.random.randint(1,7, 100000)
#print(a)
#plt.hist(a)

a=np.random.randint(0,10,(2,3))
b=np.random.normal(0,1, (2,3))

#np.save("myarr1",a)
#np.savez("myarr2",b,a)
#print(np.load("myarr1.npy"))
#npzfiles=np.load("myarr2.npz")
#print(npzfiles['arr_0'])

#print(np.loadtxt("simple.csv", dtype=np.int))
#data=np.loadtxt("height.csv", delimiter=",", dtype={
#        'names':("order","name","height(cm)"),
#        'formats':("i", "S20", "f")
#        }, skiprows=1)


#data=np.random.random((3,4))
#np.savetxt("mytxt.csv", data, delimiter=",")

arr=np.random.random((5,2,3))
#print(arr)
#print(np.shape(arr))
#print(arr.ndim)
#print(arr.size)
arr1=arr.astype(np.int)
#print(arr1)
#print(np.info(np.ndarray.dtype))

a=np.arange(1,10).reshape(3,3)
#print(a)

b=np.arange(9,0,-1).reshape(3,3)
#print(b)

#print(a-b)
#print(np.div(a,b))

#print(np.sin(a))
#print(np.cos(a))
#print(np.tan(a))
#print(np.log(a))
print(np.dot(a,b))

#print(a==b)
#print(a)
#print(a.sum(axis=0))
#print(a.sum(axis=1))




