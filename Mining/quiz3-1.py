# Q1

from tkinter import *
from tkinter import messagebox

# 함수선언
def keyEvent(event):
    messagebox.showinfo("키보드", "기타")  
    return

def az(event):
    messagebox.showinfo("키보드", "소문자")
    return

def cap_az(event):
    messagebox.showinfo("키보드", "대문자")
    return

def num(event):
    messagebox.showinfo("키보드", "숫자")

# 변수 선언
window = None # main window


# main
window = Tk()
window.geometry('400x400')
label1 = Label(window)
label1.pack(expand=1, anchor=CENTER)
window.bind("<Key>", keyEvent)
#window.bind(, az)
for i in range(97, 123):
    window.bind(chr(i), az)

for i in range(65, 91):
    window.bind(chr(i), cap_az)
    
for i in range(0, 10):
    window.bind(i, num)

window.mainloop()