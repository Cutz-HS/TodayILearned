### Q3+ : HSI + RGB 화소영역 ###

from tkinter import *
import os.path
import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
import threading
import struct
import sqlite3
import csv
import pymysql
from xlsxwriter import Workbook
import xlrd
import numpy as np
import matplotlib.pyplot as plt

## 함수 선언부
def loadImage(fname) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    global inImageR, inImageG, inImageB, outImageR, outImageG, outImgageB
    photo = PhotoImage(file=filename)
    inW = photo.width()
    inH = photo.height()
    inImage = []
    tmpList = []
    for i in range(inH):
        tmpList = []
        for k in range(inW) :
            tmpList.append(np.array([0, 0, 0]))  #RGB를 각각 0 벡터를 만들어 inImage에 인덱스 형성
        inImage.append(tmpList)
    for  i  in range(inH):
        for  k  in  range(inW):
            r, g, b = photo.get(k, i)
            inImage[i][k] = [r, g, b] #RGB를 각각 리스트로 넣어 inImage에 추가
    inImage = np.array(inImage)
    photo = None

def openFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("GIF파일", "*.gif; *.png"), ("모든파일", "*.*")))
    loadImage(filename) # 파일 --> 입력메모리
    equal() # 입력메모리--> 출력메모리

def display() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 기존에 캐버스 있으면 뜯어내기.
    if  canvas != None :
        canvas.destroy()
    # 화면 준비 (고정됨)
    VIEW_X, VIEW_Y = 128, 128
    if VIEW_X >= outW or VIEW_Y >= outH:
        VIEW_X = outW
        VIEW_Y = outH
    step = int(outW / VIEW_X) # 축소배수
    window.geometry(str(VIEW_X*2) + 'x' + str(VIEW_Y*2))
    canvas = Canvas(window, width=VIEW_X, height=VIEW_Y)
    paper = PhotoImage(width=VIEW_X, height=VIEW_Y)
    canvas.create_image((VIEW_X/2, VIEW_Y/2), image=paper, state='normal')
    # 화면에 출력
    def putPixel() :
        for i in range(0, outH, step) :
            for k in range(0, outW, step) :
                data = outImage[i][k]
                paper.put('#%02x%02x%02x' % (int(data[0]), int(data[1]), int(data[2])), (int(k/step), int(i/step)))
    threading.Thread(target=putPixel).start()
    canvas.pack(expand=1, anchor=CENTER)
    status.configure(text="이미지 정보: " + str(outW) + " X " + str(outH))
    status.pack()

def equal() :  # 동일 영상 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    outW = inW
    outH = inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(np.array([0, 0, 0])) # RGB 0행렬
        outImage.append(tmpList)        
    for  i  in  range(inH):
        for  k  in  range(inW):
            outImage[i][k] = inImage[i][k]
    outImage = np.array(outImage)
    display()

def addImage() :  # 밝게하기 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(np.array([0, 0, 0]))
        outImage.append(tmpList)
    outImage = np.array(outImage)
    brt = askinteger('밝게하기', '밝게할 값', minvalue=1, maxvalue=255)
    inImage = np.array(inImage)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            outImage[i][k] = inImage[i][k] + brt # numpy broadcasting을 이용한 빠른 RGB 연산
            outImage[i][k][outImage[i][k] > 255] = 255
            outImage[i][k][outImage[i][k] < 0] = 0
    display()

def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.gif", filetypes=(("GIF파일", "*.gif"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write( struct.pack(outImage[i][k][0], outImage[i][k][1], outImage[i][k][2]))
    saveFp.close()

def exitFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

def saveCSV() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    output_file = asksaveasfile(parent=window, mode='w',
                               defaultextension="*.csv", filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    output_file = output_file.name

    header = ['Column', 'Row', 'Value']
    with open(output_file, 'w', newline='') as filewriter:
        csvWriter = csv.writer(filewriter)
        csvWriter.writerow(header)
        for row in range(outW):
            for col in range(outH):
                data = outImage[row][col]
                row_list = [row, col, data]
                csvWriter.writerow(row_list)
    print('OK!')

def saveShuffleCSV() :
    pass

def loadCSV(fname) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = -1
    fp = open(fname, 'r')
    for  f  in fp :
        fsize += 1
    fp.close()
    inH = inW = int(math.sqrt(fsize))  # 입력메모리 크기 결정! (중요)
    inImage = []; tmpList = []
    for i in range(inH) :  # 입력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(inW) :
            tmpList.append(0)
        inImage.append(tmpList)
    # 파일 --> 메모리로 데이터 로딩
    fp = open(fname, 'r') # 파일 열기(바이너리 모드)
    csvFP = csv.reader(fp)
    next(csvFP)
    for row_list in csvFP:
        row= int(row_list[0])
        col = int(row_list[1])
        value = row_list[2][1:-1].split() # string 상태의 RGB LIST를 다시 LIST 형태로 변환
        value = np.array(value, dtype=np.int32) # string을 int32으로 타입 변환
        inImage[row][col] = value
    fp.close()

def openCSV() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    loadCSV(filename) # 파일 --> 입력메모리
    equal() # 입력메모리--> 출력메모리

def saveSQLite() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file
    con = sqlite3.connect('d:/data/imageDB2')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    # 열이름 리스트 만들기
    inImage = outImage.copy()
    fname = os.path.basename(filename).split(".")[0]
    try:    
        sql = "DELETE FROM imageTable WHERE filename = '" + fname + "'"
        cur.execute(sql)
    except: pass
    try:
        sql = "CREATE TABLE imageTable(filename CHAR(20), resolution smallint" + \
            ", row  smallint,  col  smallint, value CHAR(20))"
        cur.execute(sql)
        con.commit()
    except:
        pass
    for i in range(inW) :
        for k in range(inH) :
            sql = "INSERT INTO imageTable VALUES('" + fname + "'," + str(inW) + \
                "," + str(i) + "," + str(k) + "," + "'" + str(inImage[i][k]) + "'" +")"
            cur.execute(sql) # str은 ' ' 앞뒤로 중요 (query)
    con.commit()
    cur.close()
    con.close()  # 데이터베이스 연결 종료
    print('Ok!')
    
def loadSQLite():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    con = sqlite3.connect('d:/data/imageDB2')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    inImage = []
    try:    
        sql = "SELECT DISTINCT filename, resolution FROM imageTable"
        cur.execute(sql)
        tableNameList = []
        while True :
            row = cur.fetchone()
            if row == None:
                break
            tableNameList.append(row[0] + ":" + str(row[1]))
        ##    
        def selectTable() :
            global window, filename, inImage, inW, inH, outW, outH
            index = listbox.curselection()[0]
            subWindow.destroy()
            fname, res = tableNameList[index].split(':')
            filename = fname
            sql = "SELECT * FROM imageTable WHERE filename = " + "'" + fname + "'"
            cur.execute(sql)
            row = cur.fetchone()
            inW = inH = int(row[1])
            tmpList = []
            for i in range(inH) :
                tmpList = []
                for k in range(inW) :
                    tmpList.append([0, 0, 0])
                inImage.append(tmpList)
            for i in range(inW*inH):
                inImage[int(row[2])][int(row[3])] = row[4][1:-1].split() # str을 다시 list로 (rgb)
                row = cur.fetchone()
            inImage = np.array(inImage, dtype=np.int32)
            cur.close()
            con.close()
            equal()    
        ##   
        subWindow = Toplevel(window)
        listbox = Listbox(subWindow)
        button = Button(subWindow, text='선택', command=selectTable)
        listbox.pack()
        button.pack()
        for  sName in tableNameList :
            listbox.insert(END, sName)
        subWindow.lift()
            ##
    except:
        cur.close()
        con.close()
        print("error")
        ##    

## Q1 / Q1+ ##
def savemySql() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # DB쿼리 / imageDB 생성
    '''
    mysql -u root -p
    CREATE DATABASE imageDB;
    '''
    # pymysql 연결 // 리눅스 ip, user: root // imageDB
    con = pymysql.connect(host='192.168.226.131', user='root', password='1234', db='imageDB2', charset='utf8')
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    # 열이름 리스트 만들기
    inImage = outImage.copy() # *변화된 outImage를 inImage로 변환
    fname = os.path.basename(filename).split(".")[0]
    sql = "DELETE FROM imageTable WHERE filename = '" + fname + "'" # 기존 데이터 삭제
    try: 
#        print(sql)
        cur.execute(sql)
        con.commit() # commit 중요
    except: pass
    try:
        sql = "CREATE TABLE imageTable( filename CHAR(20), resolution smallint" + \
            ", row  smallint,  col  smallint, value  char(20))"
        cur.execute(sql)
    except:
        pass

    for i in range(inW) :
        for k in range(inH) :
            sql = "INSERT INTO imageTable VALUES('" + fname + "'," + str(inW) + \
                "," + str(i) + "," + str(k) + "," + "'" + str(inImage[i][k]) + "'" + ")"
            cur.execute(sql)
    con.commit()
    cur.close()
    con.close()  # 데이터베이스 연결 종료
    print('Ok!')
    
def loadmySql():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # pymysql 연결 // linux >> DB 연결
    con = pymysql.connect(host='192.168.226.131', user='root', password='1234', db='imageDB2', charset='utf8')
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    inImage = []
    try:    
        # 중복치 제거 후 수집 >> distinct
        sql = "SELECT DISTINCT filename, resolution FROM imageTable"
        cur.execute(sql)
        tableNameList = []
        while True :
            row = cur.fetchone()
            if row == None:
                break
            tableNameList.append(row[0] + ":" + str(row[1]))
        ##    
        def selectTable() :
            global window, filename, inImage, inW, inH, outW, outH
            index = listbox.curselection()[0]
            subWindow.destroy()
            fname, res = tableNameList[index].split(':')
            filename = fname
            sql = "SELECT * FROM imageTable WHERE filename = " + "'" + fname + "'"
            cur.execute(sql)
            row = cur.fetchone()
            inW = inH = int(row[1])
            tmpList = []
            for i in range(inH) :
                tmpList = []
                for k in range(inW) :
                    tmpList.append(0)
                inImage.append(tmpList)
            for i in range(inW*inH):
                # ROW = [filename, resolution, rownum, colnum, grayscale]
                inImage[int(row[2])][int(row[3])] = row[4][1:-1].split()
                row = cur.fetchone()
            np.array(inImage, dtype=np.int32)
            cur.close()
            con.close()
            equal()    
        ##   
        subWindow = Toplevel(window)
        listbox = Listbox(subWindow)
        button = Button(subWindow, text='선택', command=selectTable)
        listbox.pack()
        button.pack()
        for  sName in tableNameList :
            listbox.insert(END, sName)
        subWindow.lift()
            ##
    except:
        cur.close()
        con.close()
        print("error")
        
## Q2 ##        
def sqlExcel1():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # save할 파일 결정
    outfilename = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.xlsx", filetypes=(("xlsx파일", "*.xlsx"), ("모든파일", "*.*")))
    wb = Workbook(outfilename)
    ws = wb.add_worksheet(os.path.basename(filename))
    with open(filename, 'rb') as fReader:
        for i in range(inW):
            for j in range(inH):
                data = inImage[i][j] # 저장되어 있던 inImage에서 data 추출
                ws.write(i, j, str(data)) # index마다 쓰기
    wb.close()
    
    

def sqlExcel2():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outfilename = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.xlsx", filetypes=(("xlsx파일", "*.xlsx"), ("모든파일", "*.*")))
    wb = Workbook(outfilename)
    ws = wb.add_worksheet(os.path.basename(filename))
    with open(filename, 'rb') as fReader:
        # 워크시트의 열 너비 / 행 높이 지정
        ws.set_column(0, inW, 1.0) # 0.34
        for row in range(inH):
            ws.set_row(row, 9.5) # 0.35
        for i in range(inW):
            for j in range(inH):
                data = inImage[i][j] # 기존에 있던 inImage에서 출력
                # data 셀 배경색 지정 #000000~FFFFFF
                if data[0] <= 15: # 15 이하일 경우, 1자리 수이기 때문에 0을 추가
                    hexStr = '#' + ('0' + hex(data[0])[2:])
                else: 
                    hexStr = '#' + (hex(data[0])[2:]) # 16진수 변환 후, R(2자리)
                if data[1] <= 15:
                    hexStr += ('0' + hex(data[1])[2:]) # G(2자리)
                else:
                    hexStr += hex(data[1])[2:]
                if data[2] <= 15:
                    hexStr += ('0' + hex(data[2])[2:]) # B(2자리)
                else:
                    hexStr += hex(data[2])[2:]
                cell_format = wb.add_format() # RGB코드는 #을 앞에
                cell_format.set_bg_color(hexStr)
                ws.write(i, j, '', cell_format)
    wb.close()

def sqlExcel3() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    inImage = []
    input_file = askopenfilename(parent=window, filetypes=(("EXCEL파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    for sheet in workbook.sheets():
        sRow = sheet.nrows
        sCol = sheet.ncols
        for i in range(sRow):
            tmpList = []
            for j in range(sCol):
                value = sheet.cell_value(i, j)[1:-1].split()
                tmpList.append(value)
            inImage.append(tmpList)
    np.array(inImage, dtype=np.int32)
    inW = len(inImage)
    inH = len(inImage[0])
    equal()

def a_histogram_plt():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    countListR, countListG, countListB = [0] * 256, [0] * 256, [0] * 256
    for i in range(outH):
        for k in range(outW):
            r, g, b = outImage[i][k][0], outImage[i][k][1], outImage[i][k][2]
            countListR[r] += 1
            countListG[g] += 1
            countListB[b] += 1
    plt.ion()
    plt.plot(countListR, 'r')
    plt.plot(countListG, 'g')
    plt.plot(countListB, 'b')
    plt.show()
    
def stretch():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    maxValR, maxValG, maxValB, minValR, minValG, minValB, high = 0, 0, 0, 255, 255, 255, 255
    for i in range(inH):
        for j in range(inW):
            dataR, dataG, dataB = inImage[i][j][0], inImage[i][j][1], inImage[i][j][2]
            if dataR > maxValR:
                maxValR = dataR
            if dataG > maxValG:
                maxValG = dataG
            if dataB > maxValB:
                maxValB = dataB
            if dataR < minValR:
                minValR = dataR
            if dataG < minValG:
                minValG = dataG
            if dataB < minValB:
                minValB = dataB
    for i in range(inH):
        for j in range(inW):
            valueR = int((inImage[i][j][0] - minValR) / (maxValR - minValR) * high)
            valueG = int((inImage[i][j][1] - minValG) / (maxValG - minValG) * high)
            valueB = int((inImage[i][j][2] - minValB) / (maxValB - minValB) * high)
            outImage[i][j] = [valueR, valueG, valueB]
            outImage[i][j][outImage[i][j] > 255] = 255
            outImage[i][j][outImage[i][j] < 0] = 0
    display()

def endin():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    maxValR, maxValG, maxValB, minValR, minValG, minValB, high = 0, 0, 0, 255, 255, 255, 255
    for i in range(inH):
        for j in range(inW):
            dataR, dataG, dataB = inImage[i][j][0], inImage[i][j][1], inImage[i][j][2]
            if dataR > maxValR:
                maxValR = dataR
            if dataG > maxValG:
                maxValG = dataG
            if dataB > maxValB:
                maxValB = dataB
            if dataR < minValR:
                minValR = dataR
            if dataG < minValG:
                minValG = dataG
            if dataB < minValB:
                minValB = dataB
    limit = askinteger('endin', '범위', minvalue=1, maxvalue=127)
    maxValR -= limit
    maxValG -= limit
    maxValB -= limit
    minValR += limit
    minValG += limit
    minValB += limit
    for i in range(inH):
        for j in range(inW):
            valueR = int((inImage[i][j][0] - minValR) / (maxValR - minValR) * high)
            valueG = int((inImage[i][j][1] - minValG) / (maxValG - minValG) * high)
            valueB = int((inImage[i][j][2] - minValB) / (maxValB - minValB) * high)
            outImage[i][j] = [valueR, valueG, valueB]
            outImage[i][j][outImage[i][j] > 255] = 255
            outImage[i][j][outImage[i][j] < 0] = 0
    display()
    
def equalize():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    maxValR, maxValG, maxValB, minValR, minValG, minValB, high = 0, 0, 0, 255, 255, 255, 255
    histR, histG, histB = [0] * 256, [0] * 256, [0] * 256
    cumR, cumG, cumB = [0] * 256, [0] * 256, [0] * 256
    normR, normG, normB = [0] * 256, [0] * 256, [0] * 256
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append([0, 0, 0])
        outImage.append(tmpList)
    for i in range(outH):
        for k in range(outW):
            r, g, b = inImage[i][k][0], inImage[i][k][1], inImage[i][k][2]
            histR[r] += 1
            histG[g] += 1
            histB[b] += 1
    sValR, sValG, sValB = 0, 0, 0
    for i in range(len(histR)):
        sValR += histR[i]
        sValG += histG[i]
        sValB += histB[i]
        cumR[i] = sValR
        cumG[i] = sValG
        cumB[i] = sValB
    for i in range(len(cumR)):
        normR[i] = cumR[i] / (outW * outH) * high
        normG[i] = cumG[i] / (outW * outH) * high
        normB[i] = cumB[i] / (outW * outH) * high
    for i in range(inH):
        for j in range(inW):
            index = inImage[i][j]
            outImage[i][j] = np.array([int(normR[index[0]]), int(normG[index[1]]), int(normB[index[2]])], dtype=np.int32)
            outImage[i][j][outImage[i][j] > 255] = 255
            outImage[i][j][outImage[i][j] < 0] = 0
    display()

def embossing():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    scale = askinteger("scale(3,5,7,9)", "정수", minvalue=1, maxvalue=10)
    outW, outH = inW, inH
    if int(scale) % 2 == 0: embossing()
    # mask matrix
    mask = np.zeros([scale, scale], dtype=np.int32)
    mask_num = np.array([-1, 1, 0])
    n = 0
    # rgb를 hsi로 미리 모두 변환
    inImage = rgb2hsi(inImage)
    outImage = np.array(outImage, dtype=np.float64)
    for i in range(scale):
        for j in range(scale):
            if i == j:
                mask[i][j] = mask_num[n]
                n += 1
                if n > 2: n = 0 
    for i in range(int(scale/2), inH - int(scale/2)):
        for j in range(int(scale/2), inW - int(scale/2)):
            for k in range(3):
                outImage[i][j][k] = np.sum(inImage[i - int(scale/2) : i + scale - int(scale/2), j - int(scale/2) : j + scale - int(scale/2), k] * mask)
    # hsi를 rgb로 변환
    outImage = hsi2rgb(outImage) + 127
    outImage[outImage > 255] = 255
    outImage[outImage < 0] = 0
    display()

def blurring(num):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    scale = askinteger("scale(3,5,7,9)", "정수", minvalue=1, maxvalue=10)
    outW, outH = inW, inH
    if int(scale) % 2 == 0: blurring()
    # mask matrix
    mask = np.ones([scale, scale], dtype=np.float32)
    mask = mask * (1/np.square(scale))
    # rgb를 hsi로 미리 모두 변환
    inImage = rgb2hsi(inImage)
    outImage = np.array(outImage, dtype=np.float64)
    for i in range(int(scale/2), inH - int(scale/2)):
        for j in range(int(scale/2), inW - int(scale/2)):
            for k in range(3):
                outImage[i][j][k] = np.sum(inImage[i - int(scale/2) : i + scale - int(scale/2), j - int(scale/2) : j + scale - int(scale/2), k] * mask)
    # hsi를 rgb로 변환
    outImage = hsi2rgb(outImage)
    outImage[outImage > 255] = 255
    outImage[outImage < 0] = 0
    display()
    
def gausian_blurring():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    outW, outH = inW, inH
    # mask matrix
    scale = 3
    mask = np.array([[1./16., 1./8., 1./16.], [1./8., 1./4., 1./8.], [1./16., 1./8., 1./16.]])
    # rgb를 hsi로 미리 모두 변환
    inImage = rgb2hsi(inImage)
    outImage = np.array(outImage, dtype=np.float64)
    for i in range(int(scale/2), inH - int(scale/2)):
        for j in range(int(scale/2), inW - int(scale/2)):
            for k in range(3):
                outImage[i][j][k] = np.sum(inImage[i - int(scale/2) : i + scale - int(scale/2), j - int(scale/2) : j + scale - int(scale/2), k] * mask)
    # hsi를 rgb로 변환
    outImage = hsi2rgb(outImage)
    outImage[outImage > 255] = 255
    outImage[outImage < 0] = 0
    display()
    
def sharpening(num):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    outW, outH = inW, inH
    # mask matrix
    scale = 3
    if num == 1:
        mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    if num == 2:
        mask = np.array([[-1./9., -1./9., -1./9.], [-1./9., 8./9., -1./9.], [-1./9., -1./9., -1./9.]])
    # rgb를 hsi로 미리 모두 변환
    inImage = rgb2hsi(inImage)
    outImage = np.array(outImage, dtype=np.float64)
    for i in range(int(scale/2), inH - int(scale/2)):
        for j in range(int(scale/2), inW - int(scale/2)):
            for k in range(3):
                outImage[i][j][k] = np.sum(inImage[i - int(scale/2) : i + scale - int(scale/2), j - int(scale/2) : j + scale - int(scale/2), k] * mask)
     # hsi를 rgb로 변환
    outImage = hsi2rgb(outImage)
    outImage[outImage > 255] = 255
    outImage[outImage < 0] = 0
    display()

    
def rgb2hsi(rgb):
    '''
    RGB 행렬을 받아 모두 연산처리
    '''
    rgb = np.array(rgb, dtype=np.float64)
    hsi = np.zeros(np.shape(rgb), dtype=np.float64)
    # 2중 for문으로 h, s, i를 각각 연산
    for k in range(np.shape(rgb)[0]):
        for j in range(np.shape(rgb)[1]):
            r, g, b = rgb[k][j][0], rgb[k][j][1], rgb[k][j][2]
            h, s, i = 0, 0, 0
            i = np.mean(rgb[k][j])
            if r == g == b:
                s, h = 0, 0
                hsi[k][j] = [h, s, i]
                continue
            s = 1 - (3 / np.sum(rgb[k][j]) * np.min(rgb[k][j]))
            angle = 0.5 * ((r - g) + (r - b)) / np.sqrt((r - g) * (r - g) + ((r - b) * (g - b)))
            h = np.arccos(angle)
            if b >= g:
                h = np.pi*2 - h
            hsi[k][j] = [h, s, i]
    return hsi

def hsi2rgb(hsi):
    '''
    hsi 행렬을 rgb행렬로 변환
    '''
    rgb = np.zeros(np.shape(hsi), dtype=np.float64)
    # 2중 for문으로 모든 각각의 hsi를 연산
    for k in range(np.shape(hsi)[0]):
        for j in range(np.shape(hsi)[1]):
            h, s, i = hsi[k][j][0], hsi[k][j][1], hsi[k][j][2]
            r, g, b = 0, 0, 0
            if s == 0:
                rgb[k][j] = [i, i, i]
                continue
            elif h <= np.pi/3 * 2:
                b = 1/3 * (1 - s)
                r = 1/3 * (1 + (s * np.cos(h) / np.cos(np.pi/3 - h)))
                g = 1 - (r + b)
            elif np.pi/3 * 2 < h <= np.pi/3 * 4:
                h = h - np.pi/3 * 2
                g = 1/3 * (1 + (s * np.cos(h) / np.cos(np.pi/3 - h)))
                r = 1/3 * (1 - s)
                b = 1 - (r + g)
            elif np.pi/3 * 4 < h <= np.pi * 2:
                h = h - np.pi/3 * 4
                g = 1/3 * (1 - s)
                b = 1/3 * (1 + (s * np.cos(h) / np.cos(np.pi/3 - h)))
                r = 1 - g - b
            rgb[k][j] = np.array([r, g, b]) * i * 3
    return np.array(rgb, dtype=np.int32)

## 전역 변수부
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4
panYN = False;  sx, sy, ex, ey = [0] * 4
VIEW_X, VIEW_Y = 128, 128

## 메인 코드부
window = Tk();  window.geometry('200x200');
window.title('영상 처리&데이터 분석 Ver 0.4')
status = Label(window, text='이미지 정보: ', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
pixelMenu.add_command(label='밝게하기', command=addImage)

areaMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소영역처리', menu=areaMenu)
areaMenu.add_command(label='엠보싱', command=embossing)
areaMenu.add_command(label='블러링', command=lambda: blurring(0))
areaMenu.add_command(label='가우시안블러링', command=gausian_blurring)
areaMenu.add_command(label='샤프닝', command=lambda: sharpening(1))
areaMenu.add_command(label='고주파샤프닝', command=lambda: sharpening(2))
areaMenu.add_command(label='언샤프마스크', command=lambda: blurring(1))

analyzeMenu = Menu(mainMenu);mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)
analyzeMenu.add_command(label='히스토그램', command=a_histogram_plt)
analyzeMenu.add_command(label='스트레칭', command=stretch)
analyzeMenu.add_command(label='엔드인', command=endin)
analyzeMenu.add_command(label='평활화', command=equalize)

otherMenu = Menu(mainMenu);mainMenu.add_cascade(label='다른 포맷 처리', menu=otherMenu)
otherMenu.add_command(label='CSV로 내보내기', command=saveCSV)
otherMenu.add_command(label='CSV(셔플)로 내보내기', command=saveShuffleCSV)
otherMenu.add_command(label='CSV 불러오기', command=openCSV)
otherMenu.add_separator()
otherMenu.add_command(label='SQLite로 내보내기', command=saveSQLite)
otherMenu.add_command(label='SQLite 목록 불러오기', command=loadSQLite)
otherMenu.add_separator()
otherMenu.add_command(label='mySQL로 내보내기', command=savemySql)
otherMenu.add_command(label='mySQL 목록 불러오기', command=loadmySql)
otherMenu.add_separator()
otherMenu.add_command(label='Excel로 내보내기(숫자)', command=sqlExcel1)
otherMenu.add_command(label='Excel로 내보내기(음영)', command=sqlExcel2)
otherMenu.add_command(label='Excel로 불러오기(숫자)', command=sqlExcel3)


window.mainloop()
