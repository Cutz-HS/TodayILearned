

# Q3

# 메인 코드
ROW = int(input("ROW: "))
COL = int(input("COL: "))

myList = [[j for j in range(COL)] for i in range(ROW)]

for i in range(ROW):
    for j in range(COL):
        if i%2 == 0:
            myList[i][j] = COL*i+j+1
        else:
            myList[i][-j-1] = COL*i+j+1
# print
for i in myList:
    for j in i:
        print("%2d" %j, end="   ")
    print(" ")

myList = [[j for j in range(COL)] for i in range(ROW)]

for i in range(COL):
    for j in range(ROW):
        if i%2 == 0:
            myList[j][i] = ROW*i+j+1
        else:
            myList[-j-1][i] = ROW*i+j+1

# print
for i in myList:
    for j in i:
        print("%2d" %j, end="   ")
    print(" ")