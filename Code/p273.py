list1=[1,2,3,4]
list2=[10,20,30,40]

# without map and lambda
def sum(n1,n2):
    return n1+n2

hapList=[]
for i in range(len(list1)):
    hapList.append(sum(list1[i],list2[i]))
print (hapList)

# map and lambda
hapList= list(map(lambda n1, n2:n1+n2, list1, list2))
print (hapList)