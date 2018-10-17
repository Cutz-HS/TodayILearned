### 복습Q1 : RAW 파일 --> mySQL 테이블 ###
### 복습Q2 : mySQL --> RAW 파일 ###

from tkinter import *
import os.path
import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
import pymysql
import glob
import struct

def openRAW() :
    '''
    폴더 안의 raw 파일들을 모두 DB로 저장
    '''
    global window, canvas, paper, filename, inImage, inW, inH
    con = pymysql.connect(host='192.168.226.131', user='root', password='1234', db='imagedb', charset='utf8')  # pymySQL 연결
    cur = con.cursor()
    dirName = askdirectory()
    file_list = glob.glob(os.path.join(dirName, "*.raw")) # 폴더지정
    for input_file in file_list:
        filereader = open(input_file, 'rb')
        fsize = os.path.getsize(input_file) # raw파일 size
        inH = inW = int(math.sqrt(fsize))
        tableName = os.path.basename(input_file).split(".")[0] # tablename을 위한 축략
        colList = ["row", "col", "grayscale"] # table col에 들어갈 리스트
        try:
            sql = "CREATE table " + tableName + "("
            for colname in colList:
                sql += colname + " int(5),"
            sql = sql[:-1]
            sql += ")"
            cur.execute(sql) # table query (filename, row, col, grayscale)
        except:
            print("error --> ", input_file)
        for i in range(inW):
            for j in range(inH):
                sql = "INSERT into "+ tableName + " Values("
                sql += str(i) + ", " + str(j) + ", " + str(int(ord(filereader.read(1))))
                sql += ")"
                try:
                    cur.execute(sql) # value insert
                except: pass
    filereader.close()
    con.commit()
    cur.close()
    con.close()
    print("OK")
    
def saveRAW():
    '''
    DB 안의 RAW(filename / row / col / grayscale) 데이터를 파일로 저장하는 함수
    '''
    global window, canvas, paper, filename, inImage, inW, inH
    con = pymysql.connect(host='192.168.226.131', user='root', password='1234', db='imagedb', charset='utf8')  # pymySQL 연결
    cur = con.cursor()
    sql = "SHOW TABLES" # table description이 담긴 정보를 리턴하는 쿼리
    cur.execute(sql)
    dirName = askdirectory() # 저장할 폴더 directory ask
    tableNameList = []
    while True:
        row = cur.fetchone()
        if row == None:
            break
        tableNameList.append(row[0]) # tableNameList -> 모든 Table의 이름을 받아 리스트
    for tableName in tableNameList:
        sql = "SELECT * FROM " + tableName
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            output_file = dirName + "/" + tableName + ".raw" # save file 경로
            saveFp = open(output_file, "wb")
            saveFp.write(struct.pack('B', row[2]))
        saveFp.close()
    cur.close()
    con.close()
    
 
## 전역 변수부    
window, canvas, paper, filename = [None] * 4
inImage = []
inW, inH = [0] * 2

## 메인 코드부
window = Tk() 
window.geometry('200x200');

mainMenu = Menu(window)
window.config(menu=mainMenu)

otherMenu = Menu(mainMenu);mainMenu.add_cascade(label='RAW 포맷 처리', menu=otherMenu)
otherMenu.add_command(label='RAW --> DB 저장', command=openRAW)
otherMenu.add_command(label='DB --> RAW 저장', command=saveRAW)

window.mainloop()
