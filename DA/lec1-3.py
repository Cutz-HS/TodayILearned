a=dict(name='kim', age=20)
print(a)
print(a['name'])
a['addr']='seoul'
print(a)

print(a.keys(),"\n",a.values(),"\n",a.items())

for k in a.keys():
    print(k, end=" ")
print()
    
for v in a.values():
    print(v, end=" ")
print()

for k, v in a.items():
    print(k, v, end=" ")
print()

for i in reversed(list(a.keys())):
    print(i)
