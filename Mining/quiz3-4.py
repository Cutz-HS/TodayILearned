# Q4

from tkinter import *
from tkinter.filedialog import *
import operator

# 함수선언
def openFile():
    global photo
    fileName = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    label1.configure(text=fileName)
    photo = PhotoImage(file = fileName)
    pLabel.configure(image=photo)
    pLabel.image = photo

def exitFile():
    window.quit()
    window.destroy()

def analyzeGIF():
    global photo
    rDic, gDic, bDic = {}, {}, {}
    xSize, ySize = photo.width(), photo.height()
    rMean, rMid, gMean, gMid, bMean, bMid = [0]*6
    for i in range(xSize):
        for j in range(ySize):
            r, g, b = photo.get(i,j)
            if r in rDic:
                rDic[r] += 1
            else:
                rDic[r] = 1
            if g in gDic:
                gDic[g] += 1
            else:
                gDic[g] = 1
            if b in bDic:
                bDic[b] += 1
            else:
                bDic[b] = 1
                
    countList1 = sorted(rDic.items(), key=operator.itemgetter(1))
    countList2 = sorted(gDic.items(), key=operator.itemgetter(1))
    countList3 = sorted(bDic.items(), key=operator.itemgetter(1))
    rList, gList, bList = [], [], []
    
    for i in countList1:
        for j in range(i[1]):
            rList.append(i[0])
    for i in countList2:
        for j in range(i[1]):
            gList.append(i[0])
    for i in countList3:
        for j in range(i[1]):
            bList.append(i[0]) 
           
    rMean = sum(rList) / len(rList)
    gMean = sum(gList) / len(gList)
    bMean = sum(bList) / len(bList)
    
    mid = int((xSize * ySize) / 2)
    
    countList1 = sorted(rDic.items(), key=operator.itemgetter(0))
    countList2 = sorted(gDic.items(), key=operator.itemgetter(0))
    countList3 = sorted(bDic.items(), key=operator.itemgetter(0))
    rList, gList, bList = [], [], []
    
    for i in countList1:
        for j in range(i[1]):
            rList.append(i[0])
    for i in countList2:
        for j in range(i[1]):
            gList.append(i[0])
    for i in countList3:
        for j in range(i[1]):
            bList.append(i[0])
        
    if len(rList) %2 == 0:
        rMid = (rList[mid+1] + rList[mid]) / 2
    else:
        rMid = rList[mid+1]
    if len(gList) %2 == 0:
        gMid = (gList[mid+1] + gList[mid]) / 2
    else:
        gMid = gList[mid+1]        
    if len(bList) %2 == 0:
        bMid = (bList[mid+1] + bList[mid]) / 2
    else:
        bMid = bList[mid+1]
        
    print("r max: ", countList1[-1], " / r min: ", countList1[0], 
          " / r mean: ", rMean , " / r median: ", rMid)
    print("g max: ", countList2[-1], " / g min: ", countList2[0], 
          " / g mean: ", gMean , " / g median: ", gMid) 
    print("b max: ", countList3[-1], " / b min: ", countList3[0], 
          " / b mean: ", bMean , " / b median: ", bMid)     

# 변수선언
window = None
photo = None

# main
window = Tk()
window.title("Memo")
window.geometry("400x400")
mainMenu = Menu(window)
window.config(menu=mainMenu)
label1 = Label(window)
label1.pack()

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일(F)", menu=fileMenu)
fileMenu.add_command(label="열기(O)...", command=lambda : openFile())
fileMenu.add_separator()
fileMenu.add_command(label="GIF 데이터 분석", command=analyzeGIF)
fileMenu.add_separator()
fileMenu.add_command(label="끝내기(X)", command=lambda : exitFile())

# 빈 사진 준비
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand = 1, anchor = CENTER)

window.mainloop()

# 변수선언
window = None
photo = None

# main
window = Tk()
window.title("Memo")
window.geometry("400x400")
mainMenu = Menu(window)
window.config(menu=mainMenu)
label1 = Label(window)
label1.pack()

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일(F)", menu=fileMenu)
fileMenu.add_command(label="열기(O)...", command=lambda : openFile())
fileMenu.add_separator()
fileMenu.add_command(label="GIF 데이터 분석", command=analyzeGIF)
fileMenu.add_separator()
fileMenu.add_command(label="끝내기(X)", command=lambda : exitFile())

# 빈 사진 준비
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand = 1, anchor = CENTER)

window.mainloop()