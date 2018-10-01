from tkinter import *


# 함수 선언
def openFun():
    print("멍멍")

# 변수선언
window = None


# main
window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기(Ctrl+O)', command=openFun)
fileMenu.add_separator()
fileMenu.add_command(label='닫기(Ctrl+X)', command=openFun)

window.mainloop()