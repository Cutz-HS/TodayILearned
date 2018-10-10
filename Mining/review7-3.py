# Review Q3 : RAW 파일 분석 후, 빈도 통계 저장
# RAW열기 -> CSV저장

from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import os
import glob
import csv
import math
import operator

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

def saveCSV() :
    global csvList
    if csvList == [] :
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',
               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')
    for  row_list  in  csvList :
        row_str = ','.join(map(str, row_list))
        filewriter.writelines(row_str + '\n')
    filewriter.close()
    
    
def openRAW() :
    global filename,inImage, inW, inH, photo
    filename = askopenfilename(parent=window,
                               filetypes=(("그림파일", "*.raw; *.gif"), ("모든파일", "*.*")))
    loadImage(filename)

def loadImage(fname):
    global csvList, inW, inH, inImage, filename
    fsize = os.path.getsize(fname)
    inH = inW = int(math.sqrt(fsize))
    inImage = []
    for i in range(inH):
        tmpList = []
        for j in range(inW):
            tmpList.append(0)
        inImage.append(tmpList)
    fp = open(fname, 'rb')
    for i in range(inH):
        for j in range(inW):
            inImage[i][j] = int(ord(fp.read(1)))
    allDict1 = {}
    for i in range(inH):
        for j in range(inW):
            if inImage[i][j] in allDict1:
                allDict1[inImage[i][j]] += 1
            else:
                allDict1[inImage[i][j]] = 1              
    sortList1 = sorted(allDict1.items(), key=operator.itemgetter(1))
    csvList = sortList1
    drawSheet(csvList)

## 전역 변수 ##
csvList, cellList = [], []
inImage = []
inW, inH = [0] * 2

## 메인 코드 ##
window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='CSV 저장', command=saveCSV)
fileMenu.add_command(label='RAW 열기', command=openRAW)

window.mainloop()