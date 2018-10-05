# comprehension
res= [num*2 for num in [1,2,3,4]]
print(res)

res= [num*2 for num in [1,2,3,4] if num%2==0]
print(res)

res=[x*y for x in range(2,5) for y in range(1,10)]
print(res)

a=[1,2,3,4,5]
res=[i*2 for i in a if i%2==1]
print(res)
res=[]
for n in a:
    if n%2==1:
        res.append(n*2)
    else:
        res.append(n)
print(res)

# Q1
msg="How are you? fine thank you and you?"
print(''.join([i for i in msg if i not in 'aeiou']))

# Q2
#res=[i*2 for i in a if i%2==1] + [j for j in a if j%2==]
res=[n*2 if n%2==1 else n for n in a]
print(res)