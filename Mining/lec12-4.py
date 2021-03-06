from tkinter import *; import os.path ;import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
import matplotlib.pyplot as plt
import numpy as np

## 함수 선언부
def loadImage(fname) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = os.path.getsize(fname) # 파일 크기 확인
    inH = inW = int(math.sqrt(fsize))  # 입력메모리 크기 결정! (중요)
    inImage = []; tmpList = []
    for i in range(inH) :  # 입력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(inW) :
            tmpList.append(0)
        inImage.append(tmpList)
    # 파일 --> 메모리로 데이터 로딩
    fp = open(fname, 'rb') # 파일 열기(바이너리 모드)
    for  i  in range(inH) :
        for  k  in  range(inW) :
            inImage[i][k] =  int(ord(fp.read(1)))
    fp.close()

def openFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    loadImage(filename) # 파일 --> 입력메모리
    equal() # 입력메모리--> 출력메모리

import threading
def display() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, VIEW_X, VIEW_Y
    # 기존에 캐버스 있으면 뜯어내기.
    if  canvas != None :
        canvas.destroy()
    # 화면 준비 (고정됨)
    if VIEW_X >= outW or VIEW_Y >= outH : # 영상이 128미만이면
        VIEW_X = outW
        VIEW_Y = outH
        step = 1  # 건너뛸숫자
    else :
        step = int(outW / VIEW_X)

    window.geometry(str(VIEW_X*2) + 'x' + str(VIEW_Y*2))
    canvas = Canvas(window, width=VIEW_X, height=VIEW_Y)
    paper = PhotoImage(width=VIEW_X, height=VIEW_Y)
    canvas.create_image((VIEW_X/2, VIEW_X/2), image=paper, state='normal')
    # 화면에 출력
    def putPixel() :
        for i in range(0, outH,step) :
            for k in range(0, outW,step) :
                data = outImage[i][k]
                paper.put('#%02x%02x%02x' % (data, data, data),
                          ( int(k/step),int(i/step)))

    threading.Thread(target=putPixel).start()
    canvas.pack(expand=1, anchor =CENTER)
    status.configure(text='이미지 정보:' + str(outW) + 'x' + str(outH) )


def equal() :  # 동일 영상 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            outImage[i][k] = inImage[i][k]

    display()


def addImage() :  # 밝게하기 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    value = askinteger('밝게하기', '밝게할 값-->', minvalue=1, maxvalue=255)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            if inImage[i][k] + value > 255 :
                outImage[i][k] = 255
            else :
                outImage[i][k] = inImage[i][k] + value
    display()

def a_average() :  # 입출력 영상의 평균값
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    rawSum = 0
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            rawSum += inImage[i][k]
    inRawAvg = int(rawSum / (inH*inW))

    rawSum = 0
    for  i  in  range(outH) :
        for  k  in  range(outW) :
            rawSum += outImage[i][k]
    outRawAvg = int(rawSum / (outH*outW))

    subWindow = Toplevel(window) # 부모(window)에 종속된 서브윈도
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text='입력영상 평균값 -->' + str(inRawAvg) ); label1.pack()
    label2 = Label(subWindow, text='출력영상 평균값 -->' + str(outRawAvg)); label2.pack()
    subWindow.mainloop()

def a_histogram():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    countList = [0] * 256
    normList = [0] * 256
    for i in range(outH):
        for k in range(outW):
            value = outImage[i][k]
            countList[value] += 1
    maxVal = max(countList)
    minVal = min(countList)
    for i in range(len(countList)):
        normList[i] = (countList[i] - minVal) * 256 / (maxVal - minVal)
    subWindow = Toplevel(window)
    subWindow.geometry('256x256')
    subCanvas = Canvas(subWindow, width=256, height=256)
    subPaper = PhotoImage(width=256, height=256)
    subCanvas.create_image((256/2, 256/2), image=subPaper, state='normal')
    for i in range(0, 256):
        for k in range(0, int(normList[i])):
            data = 0
            subPaper.put('#%02x%02x%02x' % (data, data, data), (i,256-k))
    subCanvas.pack(expand=1, anchor=CENTER)
    subWindow.mainloop()        

def a_histogram_plt():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    countList = [0] * 256
    normList = [0] * 256
    for i in range(outH):
        for k in range(outW):
            value = outImage[i][k]
            countList[value] += 1
    plt.plot(countList)
    plt.show()
    
def stretch():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    maxVal, minVal, high = 0, 255, 255
    for i in range(inH):
        for j in range(inW):
            data = inImage[i][j]
            if data > maxVal:
                maxVal = data
            if data < minVal:
                minVal = data
    for i in range(inH):
        for j in range(inW):
            value = int((inImage[i][j] - minVal) / (maxVal - minVal) * high)
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            inImage[i][j] = value
    equal()

def endin():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    maxVal, minVal, high = 0, 255, 255
    for i in range(inH):
        for j in range(inW):
            data = inImage[i][j]
            if data > maxVal:
                maxVal = data
            if data < minVal:
                minVal = data
    limit = askinteger('endin', '범위', minvalue=1, maxvalue=127)
    maxVal -= limit
    minVal += limit 
    for i in range(inH):
        for j in range(inW):
            value = int((inImage[i][j] - minVal) / (maxVal - minVal) * high)
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            inImage[i][j] = value
    equal()
    
def equalize():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    maxVal, minVal, high = 0, 255, 255
    hist = [0] * 255;  cum = [0] * 255; norm = [0] * 255
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    for i in range(inH):
        for j in range(inW):
            value = inImage[i][j]
            hist[value] += 1
    sVal = 0
    for i in range(len(hist)):
        sVal += hist[i]
        cum[i] = sVal
    for i in range(len(cum)):
        norm[i] = cum[i] / (outW * outH) * high
    for i in range(inH):
        for j in range(inW):
            index = inImage[i][j]
            outImage[i][j] = int(norm[index])
            print(inImage[i][j], outImage[i][j])
            if outImage[i][j] < 0:
                outImage[i][j] = 0
            elif outImage[i][j] > 255:
                outImage[i][j] = 255
    display()

def upDown() :  # 상하 반전 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            outImage[outW-1-i][k] = inImage[i][k]

    display()

def panImage() :
    global  panYN
    panYN = True

def mouseClick(event) :  # 동일 영상 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global sx, sy, ex, ey, panYN
    if not panYN :
        return
    sx = event.x;  sy = event.y;

def mouseDrop(event):  # 동일 영상 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global sx, sy, ex, ey, panYN
    if not panYN:
        return
    ex = event.x; ey = event.y;
    my = sx - ex ; mx = sy - ey

    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            if 0<= i-mx <outH and 0<= k-my < outW :
                outImage[i-mx][k-my] = inImage[i][k]
    panYN = False
    display()


def zoomOut() :  # 축소하기 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    scale = askinteger('축소하기', '축소할 배수-->', minvalue=2, maxvalue=32)
    outW = int(inW/scale);  outH = int(inH/scale);
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    for  i  in  range(inH) :
        for  k  in  range(inW) :
             outImage[int(i/scale)][int(k/scale)] = inImage[i][k]
    display()

import struct
def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write( struct.pack('B',outImage[i][k]))

    saveFp.close()

def exitFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

import csv
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
    for row_list in csvFP :
        row= int(row_list[0]) ; col = int(row_list[1]) ; value=int(row_list[2])
        inImage[row][col] = value
    fp.close()

def openCSV() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    loadCSV(filename) # 파일 --> 입력메모리
    equal() # 입력메모리--> 출력메모리

import sqlite3
def saveSQLite() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file
    con = sqlite3.connect('imageDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    # 열이름 리스트 만들기
    colList = []
    fname = os.path.basename(filename).split(".")[0]
    try:
        sql = "CREATE TABLE imageTable( filename CHAR(20), resolution smallint" + \
            ", row  smallint,  col  smallint, value  smallint)"
        cur.execute(sql)
    except:
        pass

    for i in range(inW) :
        for k in range(inH) :
            sql = "INSERT INTO imageTable VALUES('" + fname + "'," + str(inW) + \
                "," + str(i) + "," + str(k) + "," + str(inImage[i][k]) +")"
            cur.execute(sql)

    con.commit()

    cur.close()
    con.close()  # 데이터베이스 연결 종료
    print('Ok!')

def openSQLite() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file
    con = sqlite3.connect('imageDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    try :
        sql = "SELECT DISTINCT filename, resolution FROM imageTable"
        cur.execute(sql)
        tableNameList = [] # ['강아지:128', '강아지:512' ....]
        while True :
            row = cur.fetchone()
            if row == None :
                break
            tableNameList.append( row[0] + ':' + str(row[1]) )

        ######## 내부 함수 (Inner Function) : 함수 안의 함수,지역함수 #######
        def selectTable() :
            global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
            selectedIndex = listbox.curselection()[0]
            subWindow.destroy()
            fname, res = tableNameList[selectedIndex].split(':')
            filename = fname
            sql = "SELECT row, col, value FROM imageTable WHERE filename='" + \
                fname + "' AND resolution=" + res
            print(sql)
            cur.execute(sql)

            inH = inW = int(res)
            inImage = [];  tmpList = []
            for i in range(inH):  # 입력메모리 확보(0으로 초기화)
                tmpList = []
                for k in range(inW):
                    tmpList.append(0)
                inImage.append(tmpList)
            while True :
                row_tuple = cur.fetchone()
                if row_tuple == None :
                    break
                row, col, value = row_tuple
                inImage[row][col] = value

            cur.close()
            con.close()
            equal()
            print("Ok! openSQLite")

        ################################################################

        subWindow = Toplevel(window)
        listbox = Listbox(subWindow)
        button = Button(subWindow, text='선택', command=selectTable)
        listbox.pack(); button.pack()
        for sName in tableNameList :
            listbox.insert(END, sName)
        subWindow.lift()



    except :
        cur.close()
        con.close()
        print("Error! openSQLite")

import pymysql
def saveMySQL() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file
    con = pymysql.connect(host='192.168.174.129', user='root',
                          password='1234', db='imageDB', charset='utf8')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    # 열이름 리스트 만들기
    colList = []
    fname = os.path.basename(filename).split(".")[0]
    try:
        sql = "CREATE TABLE imageTable( filename CHAR(20), resolution smallint" + \
            ", row  smallint,  col  smallint, value  smallint)"
        cur.execute(sql)
    except:
        pass

    try:
        sql = "DELETE FROM imageTable WHERE filename='" + \
              fname + "' AND resolution=" + str(outW)
        cur.execute(sql)
        con.commit()
    except:
        pass

    for i in range(inW) :
        for k in range(inH) :
            sql = "INSERT INTO imageTable VALUES('" + fname + "'," + str(outW) + \
                "," + str(i) + "," + str(k) + "," + str(outImage[i][k]) +")"
            cur.execute(sql)

    con.commit()

    cur.close()
    con.close()  # 데이터베이스 연결 종료
    print('Ok! saveMySQL')

def openMySQL() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file
    con = pymysql.connect(host='192.168.174.129', user='root',
                          password='1234', db='imageDB', charset='utf8')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    try :
        sql = "SELECT DISTINCT filename, resolution FROM imageTable"
        cur.execute(sql)
        tableNameList = [] # ['강아지:128', '강아지:512' ....]
        while True :
            row = cur.fetchone()
            if row == None :
                break
            tableNameList.append( row[0] + ':' + str(row[1]) )

        ######## 내부 함수 (Inner Function) : 함수 안의 함수,지역함수 #######
        def selectTable() :
            global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
            selectedIndex = listbox.curselection()[0]
            subWindow.destroy()
            fname, res = tableNameList[selectedIndex].split(':')
            filename = fname
            sql = "SELECT row, col, value FROM imageTable WHERE filename='" + \
                fname + "' AND resolution=" + res
            print(sql)
            cur.execute(sql)

            inH = inW = int(res)
            inImage = [];  tmpList = []
            for i in range(inH):  # 입력메모리 확보(0으로 초기화)
                tmpList = []
                for k in range(inW):
                    tmpList.append(0)
                inImage.append(tmpList)
            while True :
                row_tuple = cur.fetchone()
                if row_tuple == None :
                    break
                row, col, value = row_tuple
                inImage[row][col] = value

            cur.close()
            con.close()
            equal()
            print("Ok! openMySQL")

        ################################################################

        subWindow = Toplevel(window)
        listbox = Listbox(subWindow)
        button = Button(subWindow, text='선택', command=selectTable)
        listbox.pack(); button.pack()
        for sName in tableNameList :
            listbox.insert(END, sName)
        subWindow.lift()



    except :
        cur.close()
        con.close()
        print("Error! openMySQL")

import xlwt
def saveExcel1() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    output_file = asksaveasfile(parent=window, mode='w',
                               defaultextension="*.xls", filetypes=(("XLS파일", "*.xls"), ("모든파일", "*.*")))
    output_file = output_file.name

    sheetName = os.path.basename(output_file).split(".")[0]
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheetName)

    for rowNum in range(outH):
        for colNum in range(outW):
            data = outImage[rowNum][colNum]
            ws.write(rowNum, colNum, data)

    wb.save(output_file)
    print('OK! saveExcel1')

import xlsxwriter
def saveExcel2() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    output_file = asksaveasfile(parent=window, mode='w',
                               defaultextension="*.xlsx", filetypes=(("XLSX파일", "*.xls"), ("모든파일", "*.*")))
    output_file = output_file.name

    sheetName = os.path.basename(output_file).split(".")[0]
    wb = xlsxwriter.Workbook(output_file)
    ws = wb.add_worksheet(sheetName)

    ws.set_column(0, outW, 1.0)  # 약 0.34 쯤
    for r in range(outH):
        ws.set_row(r, 9.5)  # 약 0.35 쯤
    for  rowNum in range(outW) :
        for colNum in range(outH) :
            data = outImage[rowNum][colNum]
            # data 값으로 셀의 배경색을 조절 #000000~#FFFFFF
            if data > 15 :
                hexStr = '#' + (hex(data)[2:])*3
            else :
                hexStr = '#' + ('0' + hex(data)[2:]) * 3

            # 셀의 포맷을 준비
            cell_format = wb.add_format()
            cell_format.set_bg_color(hexStr)

            ws.write(rowNum, colNum, '', cell_format)

    wb.close()
    print('OK! saveExcel2')

def embossing():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for j in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    MSIZE = 3
    mask = [[-1, 0, 0], [0, 0, 0], [0, 0, 1]]
    tmpinImage, tmpoutImage = [], []
    for i in range(inH + 2):
        tmpList = []
        for j in range(inW + 2):
            tmpList.append(128)
        tmpinImage.append(tmpList)
    for i in range(outH):
        tmpList = []
        for j in range(outW):
            tmpList.append(0)
        tmpoutImage.append(tmpList)
    for i in range(inH):
        for j in range(inW):
            tmpinImage[i+1][j+1] = inImage[i][j]
    # 회선 연산 하기, 마스크 연산
    for i in range(1, inH):
        for j in range(1, inW):
            S = 0.0
            for m in range(0, MSIZE):
                for n in range(0, MSIZE):
                    S += tmpinImage[i+(m-1)][j+(n-1)] * mask[m][n]
            tmpoutImage[i-1][j-1] = S
    for i in range(outW):
        for j in range(outH):
            tmpoutImage[i][j] += 127
    for i in range(outW):
        for j in range(outH):
            outImage[i][j] = int(tmpoutImage[i][j])
            if outImage[i][j] < 0: 
                outImage[i][j] = 0
            if outImage[i][j] > 255:
                outImage[i][j] = 255
    display()
    
## Q3 ##
def blurring(num):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    scale = askinteger("scale(3,5,7,9)", "정수", minvalue=1, maxvalue=10) # 홀수 입력
    outW, outH = inW, inH
    inImage = np.array(inImage, dtype=np.int32)
    outImage = np.array(outImage)
    if int(scale) % 2 == 0: blurring(0)
    mask = np.ones([scale, scale], dtype=np.float32)
    mask = mask * (1/np.square(scale)) # mask 1 행렬에 블러값 입력
    for i in range(int(scale/2), inH - int(scale/2)):
        for j in range(int(scale/2), inW - int(scale/2)):
            outImage[i][j] = int(np.sum(inImage[i - int(scale/2) : i + scale - int(scale/2), j - int(scale/2) : j + scale - int(scale/2)] * mask))
            if num == 1:
                outImage[i][j] = inImage[i][j] - outImage[i][j]
            if outImage[i][j] > 255: outImage[i][j] = 255
            elif outImage[i][j] < 0: outImage[i][j] = 0
    display()
    
def gausian_blurring():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    outW, outH = inW, inH
    inImage = np.array(inImage, dtype=np.int32)
    outImage = np.array(outImage)
    # mask matrix
    scale = 3
    mask = np.array([[1./16., 1./8., 1./16.], [1./8., 1./4., 1./8.], [1./16., 1./8., 1./16.]])
    for i in range(int(scale/2), inH - int(scale/2)):
        for j in range(int(scale/2), inW - int(scale/2)):
            outImage[i][j] = int(np.sum(inImage[i - int(scale/2) : i + scale - int(scale/2), j - int(scale/2) : j + scale - int(scale/2)] * mask))
            if outImage[i][j] > 255: outImage[i][j] = 255
            elif outImage[i][j] < 0: outImage[i][j] = 0
    display()
    
def sharpening(num):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    outW, outH = inW, inH
    inImage = np.array(inImage, dtype=np.int32)
    outImage = np.array(outImage)
    # mask matrix
    scale = 3
    if num == 1:
        mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    if num == 2:
        mask = np.array([[-1./9., -1./9., -1./9.], [-1./9., 8./9., -1./9.], [-1./9., -1./9., -1./9.]])
    for i in range(int(scale/2), inH - int(scale/2)):
        for j in range(int(scale/2), inW - int(scale/2)):
            outImage[i][j] = int(np.sum(inImage[i - int(scale/2) : i + scale - int(scale/2), j - int(scale/2) : j + scale - int(scale/2)] * mask))
            if outImage[i][j] > 255: outImage[i][j] = 255
            elif outImage[i][j] < 0: outImage[i][j] = 0
    display()

def morphing():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW, outH = inW, inH
    filename2 = askopenfilename(parent=window,
                               filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    if filename == '' or filename2 == None:
        return
    inImage2 = []
    fsize2 = os.path.getsize(filename2)
    inH2 = inW2 = int(math.sqrt(fsize2))
    if inH2 != inH:
        return
    outimage = []
    fp2 = open(filename2, 'rb')
    for i in range(outH):
        tmpList = []
        for j in range(outW):
            data = int(ord(fp2.read(1)))
            tmpList.append(data)
        inImage2.append(tmpList)
    fp2.close()
    for i in range(outH):
        tmpList = []
        for j in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    value = askinteger('합성 비율', '두 번째 영상 가중치', minvalue=1, maxvalue=100)
    w1 = (1 - value/100)
    w2 = value/100
    for i in range(outH):
        for j in range(outW):
            data = int(inImage[i][j] * w1) + int(inImage2[i][j] * w2)
            if data > 255:
                data = 255
            elif data < 0:
                data = 0
            outImage[i][j] = data
    display()
    
## 전역 변수부
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4
panYN = False;  sx, sy, ex, ey = [0] * 4
VIEW_X, VIEW_Y = 256, 256
status = None

## 메인 코드부
window = Tk();  window.geometry('400x400');
window.title('영상 처리&데이터 분석 Ver 0.7')
window.bind("<Button-1>", mouseClick)
window.bind("<ButtonRelease-1>", mouseDrop)

status = Label(window, text='이미지 정보:', bd=1, relief=SUNKEN, anchor=W)
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
pixelMenu.add_command(label='모핑', command=morphing)

geoMenu = Menu(mainMenu);mainMenu.add_cascade(label='기하학 처리', menu=geoMenu)
geoMenu.add_command(label='상하반전', command=upDown)
geoMenu.add_command(label='화면이동', command=panImage)
geoMenu.add_command(label='화면축소', command=zoomOut)

areaMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소영역처리', menu=areaMenu)
areaMenu.add_command(label='엠보싱', command=embossing)
areaMenu.add_command(label='블러링', command=lambda: blurring(0))
areaMenu.add_command(label='가우시안블러링', command=gausian_blurring)
areaMenu.add_command(label='샤프닝', command=lambda: sharpening(1))
areaMenu.add_command(label='고주파샤프닝', command=lambda: sharpening(2))
areaMenu.add_command(label='언샤프마스크', command=lambda: blurring(1))

analyzeMenu = Menu(mainMenu);mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)
analyzeMenu.add_command(label='평균값', command=a_average)
analyzeMenu.add_command(label='히스토그램', command=a_histogram)
analyzeMenu.add_command(label='히스토그램2', command=a_histogram_plt)
analyzeMenu.add_command(label='스트레칭', command=stretch)
analyzeMenu.add_command(label='엔드인', command=endin)
analyzeMenu.add_command(label='평활화', command=equalize)

otherMenu = Menu(mainMenu);mainMenu.add_cascade(label='다른 포맷 처리', menu=otherMenu)
otherMenu.add_command(label='CSV로 내보내기', command=saveCSV)
otherMenu.add_command(label='CSV(셔플)로 내보내기', command=saveShuffleCSV)
otherMenu.add_command(label='CSV 불러오기', command=openCSV)
otherMenu.add_separator()
otherMenu.add_command(label='SQLite로 내보내기', command=saveSQLite)
otherMenu.add_command(label='SQLite에서 가져오기', command=openSQLite)
otherMenu.add_separator()
otherMenu.add_command(label='MySQL로 내보내기', command=saveMySQL)
otherMenu.add_command(label='MySQL에서 가져오기', command=openMySQL)
otherMenu.add_separator()
otherMenu.add_command(label='Excel로 내보내기(숫자)', command=saveExcel1)
otherMenu.add_command(label='Excel로 내보내기(음영)', command=saveExcel2)

window.mainloop()
