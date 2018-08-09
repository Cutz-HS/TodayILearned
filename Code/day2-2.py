print(abs(-2))
print(all([2,5,'a',0]))

print(any([None,"",[],0]))

name=['gildong', 'sunsin', 'sejong']
for n in name:
    print(n)

# enumerate & eval
dictA={}
for n, name in enumerate(['gildong','sunsin','sejong']):
    dictA[n]=name

for n in enumerate(['gildong','sunsin','sejong']):
    print(n[1])
    

# len&list    
print(len("today"))
print(len([3,4,5]))
print(type("today"))
a=['t','o','d','a','y']
b="".join(a)
print(type(b))

print(list("today"))

a=list("today")
print(a)
print(type(a))

# map practice
def two_times(num):
    res1=[]
    for i in num:
        res1.append(i*2)
    return res1
    
res1=(two_times([1,2,3]))
print(res1)
b=[1,2,3,4,5]

# map
def two_times(num): return num*2
print(list(map(two_times, [1,2,3])))

# lambda
fun=lambda num: num*2
print(list(map(fun, [1,2,3])))