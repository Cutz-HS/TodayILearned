import random

# Q1
fun = lambda num: num*5
mapList=list(map(fun, [5,7,9]))
#print(mapList)

# Q2
a=[1,2,3,4]
b=['a','b','c','d']
c=list(zip(a,b))
#print(c)

# Q3
randList=[]
while True:
    randList.append(random.randint(1,45))
    setList=set(randList)
    if len(setList)==6:
        break
print(setList)

randset=set()
while True:
    if len(randset)==6:
        break
    randset.add(random.randint(1,45))

print(randset)