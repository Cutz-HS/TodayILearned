import turtle
import random

turtle.title("거북")
turtle.setup(550,550)
turtle.screensize(500,500)

allDict={}
j=0

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
    allDict[j]=[myTurtle, tX, tY, tSize, r, g, b]
    j+=1

for value in allDict.values():
    myTurtle=value[0]
    myTurtle.color((value[4], value[5], value[6]))
    myTurtle.turtlesize(value[3])
    myTurtle.goto(value[1],value[2])
turtle.done()