import random

data=[]
data2=[]
i,k=0,0
temp=0

for i in range(0,10):
    temp=hex(random.randrange(0,100000))
    data.append(temp)
    data2.append(temp)

#[print(num, end=" ") for num in data]

# selection sort
for i in range(0,len(data)-1):
    for j in range(i+1,len(data)):
        if int(data[i],16)>int(data[j],16):
            data[i], data[j]=data[j], data[i]

[print (int(num,16), end=" ") for num in data]
print("")

# bubble sort
for i in range(0, len(data2)-1):
    for j in range(0, (len(data2)-1)-i):
        if int(data2[j],16) > int(data2[j+1],16):
            data2[j], data2[j+1]=data2[j+1], data2[j]
[print (int(num,16), end=" ") for num in data2]