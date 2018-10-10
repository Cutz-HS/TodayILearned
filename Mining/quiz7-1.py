### Q7-1: 지난번 사용한 CSV 읽어서 JSON 저장 // JSON 읽어오기 ###
### Q7-2: 2-1. Excel 데이터 파일 정보 ###
###       2-2. first-sheet 출력 
###       2-3. all-sheet
###       2-4. 선택택시트

from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import csv
import json
import os
import os.path
import xlrd

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

def openCSV() :
    global  csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filereader = open(input_file, 'r', newline='')
    header = filereader.readline()
    header = header.strip()  # 앞뒤 공백제거
    header_list = header.split(',')
    csvList.append(header_list)
    for row in filereader:  # 모든행은 row에 넣고 돌리기.
        row = row.strip()
        row_list = row.split(',')
        csvList.append(row_list)

    drawSheet(csvList)

    filereader.close()

def openJSON() :
    global  csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                filetypes=(("JSON파일", "*.json"), ("모든파일", "*.*")))
    filereader = open(input_file, 'r', newline='', encoding='utf-8')
    jsonDic = json.load(filereader)
    csvName = list(jsonDic.keys())
    jsonList = jsonDic[csvName[0]]
    # 헤더 추출
    header_list = list(jsonList[0].keys())
    csvList.append(header_list)
    # 행들 추출
    for tmpDic in jsonList:
        tmpList = []
        for header in header_list:
            data = tmpDic[header]
            tmpList.append(data)
        csvList.append(tmpList)

    drawSheet(csvList)

    filereader.close()

def  saveCSV() :
    global csvList, input_file
    if csvList == [] :
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',
               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')
    for  row_list  in  csvList :
        row_str = ','.join(map(str, row_list))
        filewriter.writelines(row_str + '\n')

    filewriter.close()
    
def  saveJSON() :
    global csvList, input_file
    if csvList == [] :
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.json',
               filetypes=(("JSON파일", "*.json"), ("모든파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')
    # csvList --> jsonDic
    fname = os.path.basename(input_file).split(".")[0]
    jsonDic = {}
    jsonList = []
    tmpDic = {}
    header_list = csvList[0]
    for i in range(1, len(csvList)) :
        rowList = csvList[i]
        tmpDic = {}
        for k in range(0, len(rowList)) :
            tmpDic[header_list[k]] = rowList[k]
        jsonList.append(tmpDic)

    jsonDic[fname] = jsonList
    json.dump(jsonDic, filewriter, indent=4)
    filewriter.close()
    
    
def jsonData():
    global csvList
    sumList = []
    for i in range(len(csvList)):
        if csvList[i][3] != 'Cost':
            sumList.append(float(csvList[i][3][1:]))
    allsum =  sum(sumList)
    avg = sum(sumList) / (len(csvList) - 1)
    subWindow = Toplevel(window)
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text="총합: " + str(allsum) + "\n" + "평균: " + str(avg))
    label1.pack()
    
def openExcel():
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window, filetypes=(("EXCEL파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    for worksheet in workbook.sheets():
        sheetName = worksheet.name
        sRow = worksheet.nrows
        sCol = worksheet.ncols
    subWindow = Toplevel(window)
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text=str(sheetName) + "\n" + str(sRow) + "\n" + str(sCol))
    label1.pack()
    
def excelData01():
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window, filetypes=(("EXCEL파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    sheet1 = workbook.sheets()[0]
    sheetName = sheet1.name
    sRow = sheet1.nrows
    sCol = sheet1.ncols
    for i in range(sRow):
        tmpList = []
        for j in range(sCol):
            value = sheet1.cell_value(i, j)
            tmpList.append(value)
        csvList.append(tmpList)
    drawSheet(csvList)

def excelData02():
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window, filetypes=(("EXCEL파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    sheet = workbook.sheets()[0]
    sheetName = sheet.name
    sRow = sheet.nrows
    sCol = sheet.ncols
    for k in range(sheetCount):
        for i in range(sRow):
            tmpList = []
            for j in range(sCol):
                value = workbook.sheets()[k].cell_value(i, j)
                tmpList.append(value)
            csvList.append(tmpList)
    drawSheet(csvList)
    
def excelData03():
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window, filetypes=(("EXCEL파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    num = askinteger('sheet 번호', 'sheet 번호(1~{})'.format(sheetCount), minvalue=1, maxvalue=sheetCount)
    sheet = workbook.sheets()[num-1]
    sheetNameList = []
    for worksheet in workbook.sheets():
        sheetNameList.append(worksheet.name)
#    subWindow = Toplevel(window) # window의 하위 지정
#    listbox = Listbox(subWindow)
#    button = Button(subWindow, text="선택", command=None)
#    listbox.pack()
#    button.pack()
#    for sName in sheetNameList:
#        listbox.insert(END, sName)
#    subWindow.lift()
    sRow = sheet.nrows
    sCol = sheet.ncols
    for i in range(sRow):
        tmpList = []
        for j in range(sCol):
            value = sheet.cell_value(i, j)
            tmpList.append(value)
        csvList.append(tmpList)
    drawSheet(csvList) 
        
## 전역 변수 ##
csvList, cellList = [], []
inputFile = ''

## 메인 코드 ##
window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='CSV 열기', command=openCSV)
fileMenu.add_command(label='CSV 저장', command=saveCSV)
fileMenu.add_separator()
fileMenu.add_command(label='JSON 열기', command=openJSON)
fileMenu.add_command(label='JSON 저장', command=saveJSON)
csvMenu = Menu(mainMenu)
mainMenu.add_cascade(label='JSON 데이터 분석', menu=csvMenu)
csvMenu.add_command(label='총합 & 평균', command=jsonData)
excelMenu = Menu(mainMenu)
mainMenu.add_cascade(label='Excel 데이터', menu=excelMenu)
excelMenu.add_command(label="Excel 파일 정보 보기", command=openExcel)
excelMenu.add_command(label='Excel 열기', command=excelData01)
excelMenu.add_command(label='Excel 열기(all sheet)', command=excelData02)
excelMenu.add_command(label='Excel 열기(선택 sheet)', command=excelData03)

window.mainloop()