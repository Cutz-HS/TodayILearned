'''
lec1
'''
a=132
if a%2 == 1:
    print("odd")
else: print("even")


if a%2:
    print("odd")
else: print("even")

a=0
if a:
    print("odd")
else: print("even")

 입력받은 정수가 음수인지 양수인지 0인지 출력
b=int(input())
print(b+1)
print(type(b))

if b<0:
    print("음수")
else:
    if b>0:
        print("양수")
    else:
        print("0")
for i in range(10):
    print(i, end=" ")
print()

for i in range(9, -1, -1):
    print(i, end=" ")
print()

for i in reversed(range(10)):
    print(i, end=" ")
print()

s=''
for i in range(5):
    s+=str(i+1)+" "
    print(s, end=" ")
print()
    
    
a=[1,3,5]
print(a[0], a[1], a[2])
print(a)
a[0]=a[2]
print(a)
a.append(11)
print(a)

# a리스트를 역순으로 출력
for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")
    
for i in reversed(a):
    print(i, end=" ")
print()

a,b = 3, 8
print(a,b)
a,b = b,a
print(a,b)

t=(1,3,5)
print(t)

t2= 100, 200
t3, t4= t2
print(t3, t4, type(t2))

def order(a,b):
    if a<b:
        return a+b
    return a,b
print(order(4,9))
maxn, _=order(9,4)
print(maxn)

ns=[1,3,5,1,3,5,1,3,5]
unique=[]

for i in set(ns):
    unique.append(i)
print(unique)

for i in ns:
    if i not in unique:
        unique.append(i)
print(unique)

ns=[2,4,6,1,3,5]
for i in range(len(ns)):
    print(ns[i], end=" ")
print()
j=0

for i in ns:
    print(j, i, end=" ")
    j+=1
print() 
    
for i, j in enumerate(ns):
    print(i, j, end=" ")
print()

def dummy():
    pass
























