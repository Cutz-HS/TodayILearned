import numpy as np
import pandas as pd

'''
pandas df
'''
a1=np.arange(24)
a2=np.arange(24).reshape(4,6)
a3=np.arange(24).reshape((2,4,3))

a1[5]=1000
a2[0,1]=1000
a3[1,0,1]=1000

#print(a1, "\n",a2,"\n", a3)

#print(a2[1:3, 1:-1])

a2[:, 1:3]=99
#print(a2)

more=a2>=50
#print(more)

df=pd.read_csv("D:/data/seattle.csv")
rain_r=df['PRCP'].values
#print(rain_r)
#print(type(rain_r))
#print(len(rain_r))
days_a=np.arange(0, 365)
con_jan=days_a<31 # True:31, False: 365-31
#print(con_jan[:40])
conr=rain_r[con_jan]
#print(conr)
#print(np.sum(conr))
#print(np.mean(conr))

'''
펜시 인덱싱
'''
a=np.arange(1,25).reshape(4,6)
#print([a[0,0], a[1,1], a[2,2], a[3,3]])
#print(a[0,1,2,3], [0,1,2,3])

'''
배열형태변경
'''
a=np.random.randint(1,10,(2,5))
#print(a)
#print(a.ravel())
a.resize(3,3)

'''
append 방향지정
'''
a=np.arange(1,13).reshape(2,3,2)
b=np.arange(13,25).reshape(2,3,2)
#apb=np.append(a,b, axis=1)
#print(apb)

a=np.arange(1,10).reshape(3,3)
#a=np.insert(a, 2, 99, axis=0)
#print(a)

# Q. a배열의 1번 인덱스 행 제거
print(np.delete(a, 1, axis=0))
print(np.delete(a, 1, axis=1))

'''
배열결합
'''
a=np.arange(1,7).reshape(2,3)
b=np.arange(7,13).reshape(2,3)
res=np.concatenate((a,b))
print(res)
res1=np.append(a,b, axis=0)
print(res1)

x=np.arange(1,5).reshape(2,2)
y=np.arange(5,9).reshape(2,2)
v=np.array([9,10])

print(x.dot(v))
print(np.dot(x,y))
print(x.T)

x=np.arange(1,13).reshape(4,3)
v=np.array([1,0,1])
y=np.empty_like(x)
#print(em)

for i in range(4):
    y[i,:]=x[i,:]+v
print(y)

print(x+v)

vv=np.tile(v, (4,1))
print(vv)

a=np.arange(1,7).reshape(3,2)
a=np.delete(a, 1, axis=0)
print(a)
s=np.max(np.prod(a, axis=0))
print(s)





































