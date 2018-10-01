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
fileMenu.add_command(label="끝내기(X)")
fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label="편집(E)", menu=fileMenu2)
fileMenu2.add_command(label="실행취소(U)")
fileMenu2.add_separator()
fileMenu2.add_command(label="잘라내기(T)")
fileMenu2.add_command(label="복사(C)", command=lambda : editFile(1))
fileMenu2.add_command(label="붙여넣기(P)", command=lambda : editFile(2))
fileMenu2.add_command(label="삭제(L)", command=lambda : editFile(3))
fileMenu2.add_separator()
fileMenu2.add_command(label="찾기(F)")
fileMenu2.add_command(label="다음 찾기(N)")
fileMenu2.add_command(label="바꾸기(R)")
fileMenu2.add_command(label="이동(G)")
fileMenu2.add_separator()
fileMenu2.add_command(label="모두 선택(A)")
fileMenu2.add_command(label="시간/날짜(D)")

# 빈 사진 준
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand = 3, anchor = CENTER)

window.mainloop()