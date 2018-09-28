import turtle
import random

# 복습퀴즈1

# 함수선언
def random_turtle(tList):
    myTurtle = tList[0]
    myTurtle.color(tList[3])
    myTurtle.pencolor(tList[3])
    myTurtle.turtlesize(tList[2])
    myTurtle.penup()
    myTurtle.setpos(tList[4])
    myTurtle.stamp()
    myTurtle.pendown()
    myTurtle.goto(tList[1])

# 변수선언
myTurtle, tX, tY, eX, eY, tSize, tShape = [None] * 7
shapeList = []
playerTurtles = []
swidth, sheight = 800, 800

# 메인코드
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth,sheight)
shapeList = turtle.getshapes()

for i in range(20):
    random.shuffle(shapeList)
    myTurtle = turtle.Turtle(shapeList[0])
    tX = random.randrange(-swidth / 2, swidth / 2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    eX = random.randrange(-swidth / 2, swidth / 2)
    eY = random.randrange(-sheight / 2, sheight / 2)
    r, g, b = random.random(), random.random(), random.random()
    tSize = random.randrange(1,3)
    playerTurtles.append([myTurtle, (tX, tY), tSize, (r, g, b), (eX, eY)])
    
for tList in playerTurtles:
    random_turtle(tList)
turtle.done()
        
        
        
        