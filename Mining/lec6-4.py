from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *

# 함수선언
def editFile(num):
    if num == 1:
        value = askinteger('제목', '설명-->', minvalue=1, maxvalue=255)
        label1.configure(text=str(value))

def openFile():
    fileName = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    label1.configure(text=fileName)
    photo = PhotoImage(file = fileName)
    pLabel.configure(image=photo)
    pLabel.image = photo

def openCSV():
    global csvList
    csvList = []
    filename = askopenfilename(parent=window, filetypes=(("CSV파일", "*.csv"), ("모든 파일", "*.*")))
    filereader = open(input_file, 'r', newline='')
    header = filereader.readline()
    header = header.strip()
    header_list = header.split(',')
    csvList.append(header_list)
    for row in filereader:
        row = row.strip()
        row_list = row.split(',')
        csvList.append(row_list)
    drawSheed(csvList)

def drawSheet(cList):
    global cellList
    if cellList != None:
        for row in cellList:
            for col in row:
                col.destroy()
    rowNum = len(cList)
    colNum = len(cList[0])                
    cellList = []
    # 빈 시트
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window,text='')
            tmpList.append(ent)
            ent.grid(row=i, column=k)
        cellList.append(tmpList)
    for i in range(0, rowNum):
        for k in range(0, colNum):
            cellList[i][k].insert(0, cList[i][k])

def saveCSV():
    global csvList
    if csvList == []:
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv', filetypes=(("CSV파일", "*.csv"), ("모든 파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')
    for row_list in csvList:
        row_str = ','.join(map(str, row_list))
        filewriter.write(row_str + '\n')
    

# 변수선언
window = None
csvList, cellList = [], []

# main
window = Tk()
window.title("Memo")
window.geometry("700x700")
mainMenu = Menu(window)
window.config(menu=mainMenu)
label1 = Label(window)
label1.pack()

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일(F)", menu=fileMenu)
fileMenu.add_command(label="새로만들기(N)")
fileMenu.add_command(label="열기(O)...", command=lambda : openFile())
fileMenu.add_command(label="저장(S)", command=saveCSV)
fileMenu2.add_separator()
fileMenu2.add_command(label="잘라내기(T)")
fileMenu2.add_command(label="복사(C)", command=lambda : editFile(1))
fileMenu2.add_command(label="붙여넣기(P)", command=lambda : editFile(2))
fileMenu2.add_command(label="삭제(L)", command=lambda : editFile(3))
fileMenu2.add_separator()

# 빈 사진 준
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand = 3, anchor = CENTER)

window.mainloop()