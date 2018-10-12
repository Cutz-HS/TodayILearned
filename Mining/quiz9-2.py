### Q2: CSV to DB ###
### Q3: mySQL ###

from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import csv
import json
import os
import os.path
import xlrd
import xlwt
import sqlite3
import pymysql

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
    
    
def sqldata01():
    global csvList, input_file
    csvList = []
    con = sqlite3.connect('d:/data/userDB')
    cur = con.cursor()
    sql = "select * from userTable"
    cur.execute(sql)
    header_list = ["userID", "userName", "userAge"]
    csvList.append(header_list)
    while True:
        row = cur.fetchone()
        if row == None:
            break
        userID = row[0]
        userName = row[1]
        userAge = row[2]
        row_list = [userID, userName, userAge]
        csvList.append(row_list)
    drawSheet(csvList)
    cur.close()
    con.close()

def sqldata02():
    global csvList, input_file
    con = sqlite3.connect('d:/data/userDB')
    cur = con.cursor()
    headerList = []
    tableName = os.path.basename(input_file)
    tableName = tableName[:tableName.find(".")]
    for header in csvList[0]:
        headerList.append(header.replace(" ", ""))
    sql = "create table "
    sql += tableName + "("
    for header in headerList:
        sql += header + " char(20),"
    sql = sql[:-1]
    sql += ");"
    cur.execute(sql)
    for i in range(1, len(csvList)):
        rowList = csvList[i]
        sql = "insert into " + tableName + " Values("
        for row in rowList:
            sql += "'" + row + "',"
        sql = sql[:-1]
        sql += ");"
        cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

def sqldata03():
    global csvList, input_file
    csvList = []
    con = sqlite3.connect('d:/data/userDB')
    cur = con.cursor()
    sql = "SELECT name FROM sqlite_master WHERE type='table'"
    cur.execute(sql)
    tableNameList = []
    while True:
        row = cur.fetchone()
        if row == None:
            break
        tableNameList.append(row[0])
    def selectTable():
        index = listbox.curselection()[0]
        subWindow.destroy()
        sql = "SELECT * FROM "
        sql += tableNameList[index]
        cur.execute(sql)
        col = cur.description
        colNameList = []
        for cName in col:
            colNameList.append(cName[0])
        csvList.append(colNameList)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            csvList.append(list(row))
        cur.close()
        con.close()
        drawSheet(csvList)
       
    subWindow = Toplevel(window) # window의 하위 지정
    listbox = Listbox(subWindow)
    button = Button(subWindow, text="선택", command=selectTable)
    listbox.pack()
    button.pack()
    for tName in tableNameList:
        listbox.insert(END, tName)
    subWindow.lift()
    
    
def mySqldata01():
    global csvList, input_file
    csvList = []
    con = pymysql.connect(host='192.168.226.128', user='winuser', password='1234', db='userDB', charset='utf8')
    cur = con.cursor()
    sql = "select * from userTable"
    cur.execute(sql)
    header_list = ["userID", "userName", "userAge"]
    csvList.append(header_list)
    while True:
        row = cur.fetchone()
        if row == None:
            break
        userID = row[0]
        userName = row[1]
        userAge = row[2]
        row_list = [userID, userName, userAge]
        csvList.append(row_list)
    drawSheet(csvList)
    cur.close()
    con.close()

def mySqldata02():
    global csvList, input_file
    con = pymysql.connect(host='192.168.226.128', user='winuser', password='1234', db='userDB', charset='utf8')
    cur = con.cursor()
    headerList = []
    tableName = os.path.basename(input_file)
    tableName = tableName[:tableName.find(".")]
    for header in csvList[0]:
        headerList.append(header.replace(" ", ""))
    sql = "CREATE TABLE "
    sql += tableName + "("
    for header in headerList:
        sql += header + " CHAR(20), "
    sql = sql[:-2]
    sql += ");"
    cur.execute(sql)
    for i in range(1, len(csvList)):
        rowList = csvList[i]
        sql = "INSERT INTO " + tableName + " VALUES("
        for row in rowList:
            sql += "'" + row + "', "
        sql = sql[:-2]
        sql += ");"
        cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

def mySqldata03():
    global csvList, input_file
    csvList = []
    con = pymysql.connect(host='192.168.226.128', user='winuser', password='1234', db='userDB', charset='utf8')
    cur = con.cursor()
    sql = "SHOW TABLES"
    cur.execute(sql)
    tableNameList = []
    while True:
        row = cur.fetchone()
        if row == None:
            break
        tableNameList.append(row[0])
    def selectTable():
        index = listbox.curselection()[0]
        subWindow.destroy()
        sql = "SELECT * FROM "
        sql += tableNameList[index]
        cur.execute(sql)
        col = cur.description
        colNameList = []
        for cName in col:
            colNameList.append(cName[0])
        csvList.append(colNameList)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            csvList.append(list(row))
        cur.close()
        con.close()
        drawSheet(csvList)
    subWindow = Toplevel(window) # window의 하위 지정
    listbox = Listbox(subWindow)
    button = Button(subWindow, text="선택", command=selectTable)
    listbox.pack()
    button.pack()
    for tName in tableNameList:
        listbox.insert(END, tName)
    subWindow.lift()
        
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
sqlMenu = Menu(mainMenu)
mainMenu.add_cascade(label='SQL 데이터', menu=sqlMenu)
sqlMenu.add_command(label='SQL 읽기', command=sqldata01)
sqlMenu.add_command(label='SQL 쓰기', command=sqldata02)
sqlMenu.add_command(label='SQL 범용 읽기', command=sqldata03)
mySqlMenu = Menu(mainMenu)
mainMenu.add_cascade(label='mySQL 데이터', menu=mySqlMenu)
mySqlMenu.add_command(label='mySQL 읽기', command=mySqldata01)
mySqlMenu.add_command(label='mySQL 쓰기', command=mySqldata02)
mySqlMenu.add_command(label='mySQL 범용 읽기', command=mySqldata03)
window.mainloop()