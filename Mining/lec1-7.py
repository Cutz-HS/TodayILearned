# 2차원 리스트

# 4X5 크기의 빈 리스트를 만들자
#myList = [[0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0]]

ROW = int(input("row: "))
COL = int(input("col: "))
myList=[]
tmpList=[]
for i in range(ROW):
    for j in range(COL):
        tmpList.append(0)
    myList.append(tmpList)
    tmpList=[]
  
print(myList)