from tkinter import *

xSize=256
ySize=256
imageList=[]

def loadImage(name):
    global xSize, ySize, imageList
    file=open(name, 'rb')

    for i in range (0,xSize):
        tempList=[]
        for j in range (0, ySize):
            byte=int(ord(file.read(1)))
            tempList.append(byte)
            #print(tempList)
        imageList.append(tempList)

def displayImage(image):
    global xSize, ySize
    for i in range (0, xSize):
        for k in range(0, ySize):
            data = image[i][k]
            paper.put("#%02x%02x%02x" %(data,data,data), (k, i))

window=Tk()
window.title("B&W pic")
canvas=Canvas(window,height=xSize,width=ySize)
paper=PhotoImage(width=xSize,height=ySize)
canvas.create_image((xSize/2,ySize/2), image=paper, state="normal")

name="D:/python_study/C11/tree.raw"
loadImage(name)
#print(imageList)
displayImage(imageList)
canvas.pack()
window.mainloop()