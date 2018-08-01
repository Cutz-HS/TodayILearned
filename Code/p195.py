import turtle
import random

turtle.title("거북")
turtle.setup(550,550)
turtle.screensize(500,500)

allList=[]

shapeList=turtle.getshapes()
shapeList.remove('blank')
for i in range(100):
    myTurtle=turtle.Turtle(random.choice(shapeList))
    # goto(x,y)
    tX=random.randrange(-250,251)
    tY=random.randrange(-250,250)
    # color
    r=random.random()
    g=random.random()
    b=random.random()
    # size
    tSize=random.randrange(1,4)
    # list
    allList.append([myTurtle, tX, tY, tSize, r, g, b])

# sorting
for i in range(0, len(allList)-1):
    for j in range(1, len(allList)):
        if allList[i][1]+allList[i][2]>allList[j][1]+allList[j][2]:
            allList[i], allList[j]=allList[j], allList[i]

#turtle main
myTurtle=allList[0][0]
myTurtle.penup()
myTurtle.goto(allList[0][1],allList[0][2])
myTurtle.color((allList[0][4],allList[0][5],allList[0][6]))
myTurtle.turtlesize(allList[0][3])
#myTurtle.pendown()
del(allList[0])

for value in allList:
    myTurtle.color((value[4], value[5], value[6]))
    myTurtle.turtlesize(value[3])
    myTurtle.goto(value[1],value[2])
    myTurtle.pendown()
    myTurtle.stamp()
turtle.done()