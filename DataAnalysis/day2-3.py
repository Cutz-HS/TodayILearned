#print(range(5))
#print(list(range(5)))
#
#print(list(range(8,-5,-2)))
#
## sorted & sort
#a=[3,4,1,2,5,8]
##ordered=sorted(a)
#print(sorted("seoul"))
#a.sort()
#print(a)
#
## zip
#b=[4,24,2,41,5,3]
#c=["3","34","5","6","1","b"]
#d=zip(a,b,c)
#print(list(d))

# pickle
# dump

import pickle
f=open("sleep.txt","wb") #write, binary
data={1:"big", 2:"data"}
pickle.dump(data, f)
f.close()

f=open("sleep.txt","rb")
print(pickle.load(f))

# glob
import glob
print(glob.glob("d*"))

# 난수생성기
import random
print(random.random())

# Q1



    