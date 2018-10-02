# Q1
# Q1+
# Q2
# Q2+
# Q3

from tkinter import *
import os.path
import math
from tkinter.filedialog import *
from tkinter.simpledialog import *
import operator

## 함수 선언
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
            tmpList.append([0, 0, 0])
        inImage.append(tmpList)
        
    for  i  in range(inH):
        for  k  in  range(inW):
            r, g, b = photo.get(k, i)
            inImage[i][k] = [r, g, b]
    photo = None

def openFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH, photo
    filename = askopenfilename(parent=window,
                               filetypes=(("그림파일", "*.raw; *.gif"), ("모든파일", "*.*")))
    loadImage(filename)
    equal()

def display():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo, paper_copy
    if  canvas != None :
        canvas.destroy()
    window.geometry(str(outH+inH) + 'x' + str(outW+inW))
    canvas = Canvas(window, width=outW, height=outH)
    paper = PhotoImage(width=outW, height=outH)
    canvas.create_image((outW/2, outH/2), image=paper, state='normal')
    for i in range(outH):
        for k in range(outW):
            data = outImage[i][k]
            paper.put('#%02x%02x%02x' % (data, data, data), (k,i))
    canvas.pack(side=RIGHT)
    photo = PhotoImage(width=outW, height=outH)
    pLabel.configure(image=paper_copy)
    
def display_first():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo, paper_copy
    if  canvas != None :
        canvas.destroy()
    window.geometry(str(outH*2) + 'x' + str(outW))
    canvas = Canvas(window, width=outW, height=outH)
    paper = PhotoImage(width=outW, height=outH)
    paper_copy = paper.copy()
    canvas.create_image((outW/2, outH/2), image=paper, state='normal')
    for i in range(outH):
        for k in range(outW):
            data = outImage[i][k]
            paper.put('#%02x%02x%02x' % (data[0], data[1], data[2]), (k,i))
            paper_copy.put('#%02x%02x%02x' % (data[0], data[1], data[2]), (k,i))
    canvas.pack(side=RIGHT)
    pLabel.configure(image=paper_copy)
            
def equal():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    outW = inW
    outH = inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append([0, 0, 0])
        outImage.append(tmpList)        
    for  i  in  range(inH):
        for  k  in  range(inW):
            outImage[i][k] = inImage[i][k]
    display_first()
    
def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

def exitFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

#def addImage(num):
#    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
#    outW = inW
#    outH = inH
#    outImage = []
#    tmpList = []
#    for i in range(outH):
#        tmpList = []
#        for k in range(outW):
#            tmpList.append(0)
#        outImage.append(tmpList)
#        
#    if num == 1:
#        brt = askinteger('밝게하기', '밝게할 값', minvalue=1, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                if inImage[i][k] + brt > 255:
#                    outImage[i][k] = 255
#                else:
#                    outImage[i][k] = inImage[i][k] + brt
#                    
#    elif num == 2:
#        brt = askinteger('어둡게하기', '어둡게할 값', minvalue=1, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                if inImage[i][k] - brt < 0:
#                    outImage[i][k] = 0
#                else:
#                    outImage[i][k] = inImage[i][k] - brt
#    elif num == 3:
#        brt = askinteger('밝게하기', '곱할 값', minvalue=1, maxvalue=10)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                if inImage[i][k] * brt > 255:
#                    outImage[i][k] = 255
#                else:
#                    outImage[i][k] = inImage[i][k] * brt
#    elif num == 4:
#        brt = askinteger('어둡게하기', '나눌 값', minvalue=1, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                outImage[i][k] = int(inImage[i][k] / brt)
#                
#    elif num == 5: # AND
#        brt = askinteger('AND', '상수', minvalue=1, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                if inImage[i][k] & brt > 255:
#                    outImage[i][k] = 255
#                elif inImage[i][k] & brt < 0:
#                    outImage[i][k] = 0
#                else:                  
#                    outImage[i][k] = inImage[i][k] & brt
#    elif num == 6: # OR
#        brt = askinteger('OR', '상수', minvalue=1, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                if inImage[i][k] | brt > 255:
#                    outImage[i][k] = 255
#                elif inImage[i][k] | brt < 0:
#                    outImage[i][k] = 0
#                else:                  
#                    outImage[i][k] = inImage[i][k] | brt
#
#    elif num == 7: # XOR
#        brt = askinteger('OR', '상수', minvalue=1, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                outImage[i][k] = inImage[i][k] ^ brt
#                if outImage[i][k] > 255: outImage[i][k] = 255
#                elif outImage[i][k] < 0: outImage[i][k] = 0
#                    
#                    
#    elif num == 8: # 반전
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                outImage[i][k] = 255 - inImage[i][k]
#                
#    elif num == 9: # 감마
#        brt = askfloat('감마', '소수', minvalue=0, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                outImage[i][k] = int(inImage[i][k] * (1/brt))
#                if outImage[i][k] > 255: outImage[i][k] = 255
#                elif outImage[i][k] < 0: outImage[i][k] = 0
#                       
#           
#    elif num == 10: # parabola(cap)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                outImage[i][k] = int(-255 * ((inImage[i][k] / 127 - 1) ** 2) + 255)
#                if outImage[i][k] > 255: outImage[i][k] = 255
#                elif outImage[i][k] < 0: outImage[i][k] = 0
#
#    elif num == 11: # parabola(cap)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                outImage[i][k] = int(255 * ((inImage[i][k] / 127 - 1) ** 2))
#                if outImage[i][k] > 255: outImage[i][k] = 255
#                elif outImage[i][k] < 0: outImage[i][k] = 0
#    
#    elif num == 12: # binary
#        brt = askinteger('임계치', '정수(1~255)', minvalue=0, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                if inImage[i][k] > brt: outImage[i][k] = 255
#                elif inImage[i][k] <= brt: outImage[i][k] = 0
#
#    elif num == 13: # 범위강조
#        brt1 = askinteger('첫 번째 범위 수', '정수(1~255)', minvalue=0, maxvalue=255)
#        brt2 = askinteger('두 번째 범위 수', '정수(1~255)', minvalue=0, maxvalue=255)
#        for  i  in  range(inH) :
#            for  k  in  range(inW) :
#                if inImage[i][k] > brt1 and inImage[i][k] < brt2:
#                    outImage[i][k] = 255
#                
#    display()

def a_average(num): # 입력 // 출력 평균
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    sumList1, sumList2 = [], []
    if num == 2:
        brt = askinteger('절사 수치', '정수(1~100)%', minvalue=1, maxvalue=100)
        cut = 255*(brt/100)
    for i in range(inH):
        for k in range(inW):
            if num == 1:
                sumList1.append(inImage[i][k])
                sumList2.append(outImage[i][k])
            if num == 2:
                if inImage[i][k] > int(cut) and inImage[i][k] < 255-int(cut):
                    sumList1.append(inImage[i][k])
                if outImage[i][k] > int(cut) and outImage[i][k] < 255-int(cut):
                    sumList2.append(outImage[i][k])                   
    inAvg = sum(sumList1) / len(sumList1)
    outAvg = sum(sumList2) / len(sumList2)
    subWindow = Toplevel(window)
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text="입력 평균: " + str(inAvg))
    label2 = Label(subWindow, text="출력 평균: " + str(outAvg))
    label1.pack()
    label2.pack()
    
def a_minmax():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    allDict1, allDict2 = {}, {}
    for i in range(inH):
        for j in range(inW):
            if inImage[i][j] in allDict1:
                allDict1[inImage[i][j]] += 1
            else:
                allDict1[inImage[i][j]] = 1
            if outImage[i][j] in allDict2:
                allDict2[outImage[i][j]] += 1
            else:
                allDict2[outImage[i][j]] = 1                
    sortList1 = sorted(allDict1.items(), key=operator.itemgetter(1))
    sortList2 = sorted(allDict2.items(), key=operator.itemgetter(1))
    subWindow = Toplevel(window)
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text="입력 최대&최소: " + str(sortList1[-1]) + str(sortList1[0]))
    label2 = Label(subWindow, text="출력 최대&최소: " + str(sortList2[-1]) + str(sortList2[0]))
    label1.pack()
    label2.pack()            

def direct(num):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    outW = inW
    outH = inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)        
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            if num == 1:
                outImage[outW-1-i][k] = inImage[i][k]
            if num == 2:
                outImage[i][outH-1-k] = inImage[i][k]
            
    display()
    
def panImage():
    global panYN
    panYN = True

def mouseClick(event):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    global sx, sy, ex, ey, panYN
    if not panYN:
        return
    sx = event.x
    sy = event.y

def mouseDrop(event):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    global sx, sy, ex, ey, panYN
    if not panYN:
        return
    ex = event.x
    ey = event.y
    mx = sx - ex
    my = sy - ey
    outW = inW
    outH = inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    for  i  in  range(inH) :
        for  k  in  range(inW):
            if 0 < i-mx < outH and 0 < k-my < outW:
                outImage[i-mx][k-my] = inImage[i][k]
    panYN = False
    display_geo()
    
def zoomOut():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    scale = askinteger('축소하기', '축소할 배수-->', minvalue=2, maxvalue=32)
    outW = int(inW/scale);  outH = int(inH/scale);
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
             outImage[int(i/scale)][int(k/scale)] = inImage[i][k]
    display()

def zoomIn(num):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, photo
    scale = askinteger("확대하기", "배수", minvalue=2, maxvalue=32)
    outW = inW * scale
    outH = outH * scale
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList) 
    if num == 1:
        for  i  in  range(inH):
            for  k  in  range(inW):
                outImage[int(i*scale)][int(k*scale)] = inImage[i][k]
    if num == 2:
        for i in range(outH):
            for k in range(outW):
                outImage[int(i)][int(k)] = inImage[int(i/scale)][int(k/scale)]
    display()
    
## 변수선언
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []
inW, inH, outW, outH = [0] * 4
photo, paper_copy = None, None
panYN = False
sx, sy, ex, ey = [0] * 4
inImage, outImage = [], []
## main
window = Tk()
window.geometry('400x400')
window.title('영상 처리&데이터 분석 Ver 0.05')
window.bind("<Button-1>", mouseClick)
window.bind("<ButtonRelease-1>", mouseDrop)
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(side=LEFT)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu)
mainMenu.add_cascade(labe='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
pixelMenu.add_command(label='밝게하기', command=lambda : addImage(1))
pixelMenu.add_command(label="어둡게하기", command=lambda : addImage(2))
#pixelMenu.add_command(label='밝게하기(곱연산)', command=lambda: addImage(3))
#pixelMenu.add_command(label="어둡게하기(나눗셈)", command=lambda: addImage(4))
#pixelMenu.add_command(label='AND연산', command=lambda: addImage(5))
#pixelMenu.add_command(label="OR연산", command=lambda: addImage(6))
#pixelMenu.add_command(label='XOR연산', command=lambda: addImage(7))
#pixelMenu.add_command(label='반전', command=lambda: addImage(8))
#pixelMenu.add_command(label='감마', command=lambda: addImage(9))
#pixelMenu.add_command(label='파라볼라(Cap)', command=lambda: addImage(10))
#pixelMenu.add_command(label='파라볼라(Cup)', command=lambda: addImage(11))
#pixelMenu.add_command(label='이진화', command=lambda: addImage(12))
#pixelMenu.add_command(label='범위강조', command=lambda: addImage(13))

#geoMenu = Menu(mainMenu)
#mainMenu.add_cascade(label='기하학처리', menu=geoMenu)
#geoMenu.add_command(label='상하반전', command=lambda: direct(1))
#geoMenu.add_command(label='좌우반전', command=lambda: direct(2))
#geoMenu.add_command(label='화면이동', command=panImage)
#geoMenu.add_command(label='줌아웃', command=zoomOut)
#geoMenu.add_command(label='줌인(forward)', command=lambda: zoomIn(1))
#geoMenu.add_command(label='줌인(backward)', command=lambda: zoomIn(2))
#
#analyzeMenu = Menu(mainMenu)
#mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)
#analyzeMenu.add_command(label='평균값', command=lambda: a_average(1))
#analyzeMenu.add_command(label='최댓값&최솟값', command=a_minmax)
#analyzeMenu.add_command(label='절사평균', command=lambda: a_average(2))

window.mainloop()