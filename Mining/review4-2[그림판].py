# Q3

from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *

def mouseClick(event) :
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width = penWidth, fill=penColor)
    
def getColor():
    global penColor
    color = askcolor()
    penColor = color[1]
    
def getWidth():
    global penWidth
    penWidth = askinteger("두께", "두께 입력", minvalue = 1, maxvalue=10)
    
# 변수 선언
window = None
canvas = None
x1, y1, x2, y2 = [None] * 4
penColor = 'black'
penWidth = 5

# main
window = Tk()
window.title("그림판")
canvas = Canvas(window, height=300, width=300)
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="설정", menu=fileMenu)
fileMenu.add_command(label="선 색상", command=getColor)
fileMenu.add_command(label="선 두께", command=getWidth)

window.mainloop()