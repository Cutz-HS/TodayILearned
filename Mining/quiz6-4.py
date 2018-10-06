# Q4 : CSV -> GUI

from tkinter import *

# 함수 선언

# 변수 선언
resList = []
cellList = []

# main
inputFile = "d:/data/csv/supplier_data.csv"

file = open(inputFile, 'r', newline='')
header = file.readline()
header = header.strip()
headerList = header.split(',')

for row in file:
    row = row.strip()
    rowList = row.split(',')
    resList.append(rowList)

window = Tk()
rowNum = len(resList) + 1
colNum = len(resList[0])
for i in range(0, rowNum):
    tmpList = []
    for j in range(0, colNum):
        ent = Entry(window, text='')
        tmpList.append(ent)
        ent.grid(row=i, column=j)
    cellList.append(tmpList)
for i in range(0, rowNum):
    for j in range(0, colNum):
        if i == 0:
            cellList[i][j].insert(0, headerList[j])
        else: cellList[i][j].insert(0, resList[i-1][j])
window.mainloop()




















