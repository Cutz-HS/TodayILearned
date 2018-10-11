### Q1: 엑셀 마지막 시트 출력 ###
from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import os
import xlrd
import glob

## function
def drawSheet(cList):
    global excelList, input_file
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

def Q1():        
    global excelList, input_file
    excelList = []
    input_file = askopenfilename(parent=window, filetypes=(("EXCEL파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    sheet = workbook.sheets()[0]
    sRow = sheet.nrows
    sCol = sheet.ncols
    for i in range(sRow):
        tmpList = []
        for j in range(sCol):
            value = workbook.sheets()[sheetCount-1].cell_value(i, j)
            tmpList.append(value)
        excelList.append(tmpList)
    drawSheet(excelList)

### Q2: 엑셀 모든 시트 화면 출력, 제목 행은 한 번만 ###
def Q2():
    global excelList, input_file
    excelList = []
    input_file = askopenfilename(parent=window, filetypes=(("EXCEL파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    sheet = workbook.sheets()[0]
    sheetName = sheet.name
    sRow = sheet.nrows
    sCol = sheet.ncols
    count = 0
    for k in range(sheetCount):
        for i in range(0, sRow):
            tmpList = []
            if i == 0: 
                if count >= 1: continue
                count += 1
            for j in range(sCol):
                value = workbook.sheets()[k].cell_value(i, j)
                tmpList.append(value)
            excelList.append(tmpList)
    drawSheet(excelList)

### Q3: 폴더 선택, 모든 엑셀파일 목록, 엑셀파일의 모든 시트 목록, 시트 출력 ###
def Q3():
    global excelList, input_file
    excelList = []
    dirName = askdirectory()
    file_list = glob.glob(os.path.join(dirName, "*.xlsx"))
    subWindow = Toplevel(window)
    listbox = Listbox(subWindow)
    
    def selectExcel():
        index = listbox.curselection()[0]
        subWindow.destroy()
        workbook = xlrd.open_workbook(file_list[index])
        sheetNameList = []
        for worksheet in workbook.sheets():
            sheetNameList.append(worksheet.name)
        
        def selectSheet():
            index1 = listbox2.curselection()[0]
            subWindow2.destroy()
            sheet = workbook.sheets()[index1]
            sRow = sheet.nrows
            sCol = sheet.ncols
            for i in range(sRow):
                tmpList = []
                for j in range(sCol):
                    value = sheet.cell_value(i, j)
                    tmpList.append(value)
                excelList.append(tmpList)
            drawSheet(excelList)
        
        subWindow2 = Toplevel(window)
        listbox2 = Listbox(subWindow2)
        button2 = Button(subWindow2, text="선택", command=selectSheet)
        listbox2.pack()
        button2.pack()
        for sName in sheetNameList:
            listbox2.insert(END, sName)
        subWindow2.lift()
        
    button = Button(subWindow, text="선택", command=selectExcel)
    listbox.pack()
    button.pack()
    for file in file_list:
        listbox.insert(END, file)
    subWindow.lift()
    for sheetName in sheetNameList:
        listbox2.insert(END, sheetName)


## variables
csvList, cellList = [], []
inputFile = ''

## main
window = Tk()
mainMenu = Menu(window)
window.config(menu=mainMenu)
excelMenu = Menu(mainMenu)
mainMenu.add_cascade(label='Excel', menu=excelMenu)
excelMenu.add_command(label='Q1', command=Q1)
excelMenu.add_command(label='Q2', command=Q2)
excelMenu.add_command(label='Q3', command=Q3)
window.mainloop()