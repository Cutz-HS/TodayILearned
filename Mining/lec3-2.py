from tkinter import *
from tkinter import messagebox

# 함수 선언
def keyEvent(e):
    global textBox
    key = chr(e.keycode)
    if '0' <= key <= '9':
        pass
    else:
        txt = textBox.get()
        txt = txt[:-1]
        textBox.delete(0, 'end')
        textBox.insert(0, txt)
        
# 변수 선언
window = None

# main
window = Tk()
window.geometry('400x400')

textBox = Entry(window)
textBox.bind("<KeyRelease>", keyEvent)
textBox.pack(anchor=CENTER)

window.mainloop()