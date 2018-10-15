from  tkinter import *
from  tkinter.simpledialog import *
from tkinter.filedialog import *
import csv
import json
import os
import os.path
import xlrd
import xlwt
import sqlite3
import pymysql
import glob

con = sqlite3.connect('d:/data/userDB')
cur = con.cursor()

# 폴더 선택하고, 그 안의 파일목록 추출
dirName = askdirectory()
file_list = glob.glob(os.path.join(dirName, "*.csv"))

#print(file_list)

for input_file in file_list:
    filereader = open(input_file, 'r', newline='')
    csvReader = csv.reader(filereader)
    colList = next(csvReader)
    tableName = os.path.basename(input_file).split(".")[0]
    try:
        sql = "CREATE table " + tableName + "("
        for colName in colList:
            cList = colName.split()
            colName = ''
            for col in cList:
                colName += col + '_'
            colName = colName[:-1]
            sql += colName + " CHAR(20),"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)
    except:
        print("error --> ", input_file)
#        continue
    
    for rowList in csvReader:
        sql = "INSERT into "+ tableName + " Values("
        for data in rowList:
            sql += "'" + data + "',"
        sql = sql[:-1] + ")"
        cur.execute(sql)
    filereader.close()
    con.commit()

cur.close()
con.close()
print("OK")














