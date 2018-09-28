from tkinter import *

window = Tk()
window.geometry('400x400')

label1 = Button(window, text="siBa")
photo = PhotoImage(file='dog.gif')
label2 = Label(window, image=photo)

label1.pack()
label2.pack()
window.mainloop()
