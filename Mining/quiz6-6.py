# Quiz 6 -> Q5 메뉴추가 

from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *

# 함수선언
def openCSV():
    global csvList, headerList
    csvList = []
    filename = askopenfilename(parent=window, filetypes=(("CSV파일", "*.csv"), ("모든 파일", "*.*")))
    filereader = open(filename, 'r', newline='')
    header = filereader.readline()
    header = header.strip()
    headerList = header.split(',')
    csvList.append(header_list)
    for row in filereader:
        row = row.strip()
        row_list = row.split(',')
        csvList.append(row_list)
    drawSheet(csvList)

def drawSheet(cList):
    global headerList
    if cellList != None:
        for row in cellList:
            for col in row:
                col.destroy()   
    rowNum = len(cList) + 1
    colNum = len(cList[0])
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
            else: cellList[i][j].insert(0, cList[i-1][j])

def saveCSV():
    global csvList
    if csvList == []:
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv', filetypes=(("CSV파일", "*.csv"), ("모든 파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')
    for row_list in csvList:
        row_str = ','.join(map(str, row_list))
        filewriter.write(row_str + '\n')
    
def editCSV():
    global headerList
    input_file = "d:/data/csv/supplier_data.csv"
    csvList, headerList = [], []
    with open(input_file, 'r', newline='') as filereader:
        header = filereader.readline()
        header = header.strip()
        headerList = header.split(',')
        headerList.pop(headerList.index("Part Number"))
        headerList.pop(headerList.index("Purchase Date"))
        for  row  in  filereader :  # 모든행은 row에 넣고 돌리기.
            row = row.strip()
            row_list = row.split(',')
            row_list[3] = row_list[3][0] + str(float(row_list[3][1:]) * 3)[0:2] + "00.00"
            row_list.pop(2)
            row_list.pop(3)
            if row_list[0] != "Supplier Y":
                csvList.append(row_list)
    drawSheet(csvList)

# 변수선언
window = None
csvList, cellList, headerList = [], [], []

# main
window = Tk()
window.title("Memo")
window.geometry("700x700")
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일(F)", menu=fileMenu)
fileMenu.add_command(label="열기(O)...", command=openCSV)
fileMenu.add_command(label="저장(S)", command=saveCSV)
csvMenu = Menu(mainMenu)
mainMenu.add_cascade(label='CSV 데이터 분석', menu=csvMenu)
csvMenu.add_command(label='Q5 출력', command=editCSV)

window.mainloop()