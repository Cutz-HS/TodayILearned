from tkinter import *
from tkinter.filedialog import *

# 함수선언
def openFile():
    fileName = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    label1.configure(text=fileName)
    photo = PhotoImage(file = fileName)
    pLabel.configure(image=photo)
    pLabel.image = photo

def exitFile():
    window.quit()
    window.destroy()

# 변수선언
window = None

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
fileMenu.add_command(label="저장(S)")
fileMenu.add_command(label="다른이름으로 저장(A)...")
fileMenu.add_separator()
fileMenu.add_command(label="페이지 설정(U)...")
fileMenu.add_command(label="인쇄(P)")
fileMenu.add_separator()
fileMenu.add_command(label="끝내기(X)", command=lambda : exitFile())

# 빈 사진 준비
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand = 1, anchor = CENTER)

window.mainloop()