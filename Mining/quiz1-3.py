# Quiz 1-3
ROW = int(input("row: "))
COL = int(input("col: "))
myList = []
tmpList = []

# 1부터 오름차순
for i in range(ROW):
    for j in range(COL):
        tmpList.append(COL*i+j+1)
    myList.append(tmpList)
    tmpList=[]
    
# print
for i in myList:
    for j in i:
        print("%2d" %j, end="   ")
    print(" ")

# Row by COL 내림차순
myList = []
tmpList = []
for i in range(ROW, 0, -1):
    for j in range(COL, 0, -1):
        tmpList.append(COL*(i-1)+j)
    myList.append(tmpList)
    tmpList=[]

# print
for i in myList:
    for j in i:
        print("%2d" %j, end="   ")
    print(" ")