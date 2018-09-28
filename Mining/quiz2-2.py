import random
from tkinter import *

picList=["dog1.gif", "dog2.gif", "dog3.gif", "dog4.gif", "dog5.gif", "dog6.gif"]


def prevPic():
    global num
    num -= 1
    if num < 0:
        num = 5
    photo = PhotoImage(file="d:/data/gif/" + picList[num])
    label.configure(image=photo)
    label.image = photo
    label2.configure(text=picList[num])

def nextPic():
    global num
    num += 1
    if num > 5:
        num = 0
    photo = PhotoImage(file="d:/data/gif/" + picList[num])
    label.configure(image=photo)
    label.image = photo
    label2.configure(text=picList[num])

random.shuffle(picList)
num=0

window=Tk()
window.geometry("700x500")
window.title("PIC viewer")

button1=Button(window, text="Prev", command=prevPic)
button2=Button(window, text="Next", command=nextPic)


photo=PhotoImage(file="d:/data/gif/"+picList[num])
label=Label(window, image=photo)
label2=Label(window, text=picList[num])

button1.place(x=250, y=10)
button2.place(x=400, y=10)
label.place(x=15,y=50)
label2.place(x=320, y=10)

window.mainloop()