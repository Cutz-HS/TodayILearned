### 복습퀴즈1 : 폴더의 엑셀 파일을 SQLite의 테이블 입력 ###
### 복습퀴즈2 : SQLite의 테이블을 엑셀 파일로 저장 ###

from tkinter import *
import os.path
import glob
import xlrd, xlwt

## 함수 선언부
def openExcel() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    con = sqlite3.connect('d:/data/excelDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()
    dirName = askdirectory()
    file_list = glob.glob(os.path.join(dirName, "*.xlsx"))
    for input_file in file_list:
        filereader = open(input_file, 'r', newline='')
        workbook = xlrd.open_workbook(input_file)
        sheetCount = workbook.nsheets
        sheetList = workbook.sheets()
        sheet1 = sheetList[0]
        sRow = sheet1.nrows
        sCol = sheet1.ncols
        tableName = os.path.basename(input_file).split(".")[0]
        colList = []
        for j in range(sCol):
            colList.append(sheet1.cell_value(0,j))
        for colName in colList:
            colList[colList.index(colName)] = colName.replace(' ', '_')
        try:
            sql = "CREATE table " + tableName + "("
            for colName in colList:
                sql += colName + " CHAR(20),"
            sql = sql[:-1]
            sql += ")"
            cur.execute(sql)
        except:
            print("error --> ", input_file)
        for worksheet in sheetList:
            sRow = worksheet.nrows
            sCol = worksheet.ncols
            for i in range(1, sRow):
                sql = "INSERT into "+ tableName + " Values("
                for j in range(sCol):
                    data = worksheet.cell_value(i, j)
                    sql += "'" + str(data) + "',"
                sql = sql[:-1] + ")"
                try: 
                    cur.execute(sql)
                except : pass
        filereader.close()
        con.commit()
    cur.close()
    con.close()
    print("OK")
    
    
def saveExcel() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    con = sqlite3.connect('d:/data/excelDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()
    csvList = []
    sql = "SELECT name FROM sqlite_master WHERE type='table'"
    cur.execute(sql)
    tableNameList = []
    while True :
        row = cur.fetchone()
        if row == None:
            break
        tableNameList.append(row[0]);
    csvList.append(tableNameList)
    for tableName in tableNameList:
        csvList = []
        sql = "SELECT * FROM " + tableName
        cur.execute(sql)
        header = cur.description
        headerList = []
        for head in header:
            headerList.append(head[0])
        csvList.append(headerList)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            row_list = []
            for ii in range(len(row)) :
                row_list.append(row[ii])
            csvList.append(row_list)
        print("csvList, OK")
        if csvList == [] :
            break
        saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.xls',
                   filetypes=(("Excel", "*.xls"), ("모든파일", "*.*")))
        fileName = saveFp.name
        outWorkbook = xlwt.Workbook()
        outSheet = outWorkbook.add_sheet('sheet1')
        for i in range(len(csvList)) :
            for k in range(len(csvList[i])) :
                outSheet.write(i,k, csvList[i][k])
        outWorkbook.save(fileName)
    cur.close()
    con.close()

## 전역 변수부
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4
panYN = False;  sx, sy, ex, ey = [0] * 4

## 메인 코드부
window = Tk() 
window.geometry('200x200');

mainMenu = Menu(window)
window.config(menu=mainMenu)

otherMenu = Menu(mainMenu);mainMenu.add_cascade(label='다른 포맷 처리', menu=otherMenu)
otherMenu.add_command(label='Excel --> DB 저장', command=openExcel)
otherMenu.add_command(label='DB --> Excel 저장', command=saveExcel)

window.mainloop()
