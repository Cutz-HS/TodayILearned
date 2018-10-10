### review Q2 : GUI에 표현 ###
### 여러 CSV 출력 --> 총합 & 평균 선택

from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import os
import glob
import csv

def drawSheet(cList) :
    global cellList
    if cellList == None or cellList == [] :
        pass
    else :
        for row in cellList:
            for col in row:
                col.destroy()

    rowNum = len(cList)
    colNum = len(cList[0])
    cellList = []
    # 빈 시트 만들기
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='')
            tmpList.append(ent)
            ent.grid(row=i, column=k)
        cellList.append(tmpList)
    # 시트에 리스트값 채우기. (= 각 엔트리에 값 넣기)
    for i in range(0, rowNum):
        for k in range(0, colNum):
            cellList[i][k].insert(0, cList[i][k])
    
def csvData04():
    global csvList
    dirName = askdirectory()
    file_list = glob.glob(os.path.join(dirName, "*.csv"))
    for file in file_list:
        filereader = open(file, 'r', newline='')
        csvReader = csv.reader(filereader)
        header_list = next(csvReader)
        csvList.append(header_list)
        for row in filereader:
            row = row.strip()
            row_list = row.split(",")
            row_list[3] = row_list[3][2] + row_list[4][:len(row_list)]
            row_list[4] = row_list[5]
            csvList.append(row_list)   
        filereader.close()
    drawSheet(csvList)
    
def csvData05():
    global csvList
    sumList = []
    for i in range(len(csvList)):
        if csvList[i][3] != 'Sale Amount':
            sumList.append(float(csvList[i][3]))
    allsum =  sum(sumList)
    avg = sum(sumList) / ((len(csvList) - 3))
    subWindow = Toplevel(window)
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text="총합: " + str(allsum) + "\n" + "평균: " + str(avg))
    label1.pack()
    
    
# 전역 변수
csvList, cellList = [], []

# 메인 코드
window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='여러 CSV 출력', command=csvData04)
fileMenu.add_command(label='총합 & 평균', command=csvData05)

window.mainloop()