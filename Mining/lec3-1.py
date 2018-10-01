from tkinter import *
from tkinter import messagebox

# 함수선언
def clickLeft(event):
    xCor, yCor, mButton = event.x, event.y, event.num
    txt = ""
    if mButton == 1:
        txt += '왼쪽 '
    elif mButton == 2:
        txt += '가운데 '
    else:
        txt += '오른쪽 '
    txt += '를 ' + str(xCor) + ',' + str(yCor) + '에서 클릭'
    messagebox.showinfo("마우스", txt)

def keyEvent(event):
    code = event.keycode
    messagebox.showinfo("키보드", chr(code))
    return

# 변수 선언
window = None # main window


# main
window = Tk()
window.geometry('400x400')
photo = PhotoImage(file = "D:/data/gif/dog3.gif")
label1 = Label(window, image=photo)

textBox = Entry(window)
textBox.bind("<Key>", keyEvent)
textBox.pack(anchor=CENTER)

label1.pack(expand=1, anchor=CENTER)
label1.bind("<Button>", clickLeft)
window.bind("<Key>", keyEvent)

window.mainloop()