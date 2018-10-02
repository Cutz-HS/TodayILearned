from tkinter import *
import os.path
import math

# 함수 선언
def loadImage(fname):
    global inW, inH, outW, outH, inImage, outImage, window, canvas, paper, filename
    fsize = os.path.getsize(fname)
    inH = inW = int(math.sqrt(fsize))
    inImage = []
    for i in range(inH):
        tmpList = []
        for j in range(inW):
            tmpList.append(0)
        inImage.append(tmpList)
        
    fp = open(fname, 'rb')
    for i in range(inH):
        for j in range(inW):
            inImage[i][j] = int(ord(fp.read(1)))
    
    return

def openFile():
    global inW, inH, outW, outH, inImage, outImage, window, canvas, paper, filename
    filename = "D:/downloads/512(1).raw"
    loadImage(filename)

def saveFile():
    global inW, inH, outW, outH, inImage, outImage, window, canvas, paper, filename
    pass

def exitFile():
    global inW, inH, outW, outH, inImage, outImage, window, canvas, paper, filename
    pass

def equal():
    global inW, inH, outW, outH, inImage, outImage, window, canvas, paper, filename
    # 출력 메모리의 크기를 결정
    outW = inW
    outH = inH
    outImage = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    for i in range(inH):
        for j in range(inW):
            outImage[i][j] = inImage[i][j]
    display()

def display():
    global inW, inH, outW, outH, inImage, outImage, window, canvas, paper, filename
    


# 변수 선언
inImage, outImage = [], []
inW, inH, outW, outH = [0] * 4
window, canvas, paper, filename = [None] * 4

# main
window = Tk()
window.title("dA Ver 0.01")
window.geometry("400x400")
mainMenu = Menu(window)
window.config(menu=mainMenu)
label1 = Label(window)
label1.pack()

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일(F)", menu=fileMenu)
fileMenu.add_command(label="열기(O)...", command=lambda : openFile())
fileMenu.add_command(label="저장(S)")
fileMenu.add_separator()
fileMenu.add_command(label="끝내기(X)", command=lambda : exitFile())


window.mainloop()