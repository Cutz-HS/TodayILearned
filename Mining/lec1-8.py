import turtle
import random

# 함수
def random_turtle(tList):
    myTurtle = tList[0]
    myTurtle.color((tList[4], tList[5], tList[6])) 
    myTurtle.pencolor((tList[4], tList[5], tList[6])) 
    myTurtle.turtlesize(tList[3])
    myTurtle.goto(tList[1], tList[2])

# 전역 변수
myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
shapeList = []
playerTurtles = []
swidth, sheight = 500, 500

# 메인 코드
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth,sheight)
shapeList = turtle.getshapes()

for i in range(100):
    random.shuffle(shapeList)
    myTurtle = turtle.Turtle(shapeList[0])
    tX = random.randrange(-swidth / 2, swidth / 2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    r, g, b = random.random(), random.random(), random.random()
    tSize = random.randrange(1,3)
    playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])
    
for tList in playerTurtles:
    random_turtle(tList)
turtle.done()
    
