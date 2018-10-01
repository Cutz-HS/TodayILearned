from tkinter import *
from tkinter.filedialog import *

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
    countList = sorted(rDic.items(), key=lambda var: var[1], reverse=True)
    print(countList)

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