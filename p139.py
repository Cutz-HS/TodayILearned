import math
import random
import turtle

swidth, sheight=300,300

turtle.title("꼬북꼬북")
turtle.setup(swidth-20,sheight-20)
turtle.screensize(swidth-50,sheight-50)

t1=turtle.Turtle('turtle')
t1.color('red')
t1.penup()

t2=turtle.Turtle('turtle')
t2.color('blue')
t2.penup()

t3=turtle.Turtle('turtle')
t3.color('green')
t3.penup()

t1.goto(-140,0)
t2.goto(0,140)
t3.goto(140,0)

t1.speed(5)
t2.speed(5)
t3.speed(5)
size=1

while True:
    angle=random.randrange(0, 360)
    dist = random.randrange(1, 100)
    t1.left(angle)
    t1.forward(dist)

    angle=random.randrange(0, 360)
    dist = random.randrange(1, 100)
    t2.left(angle)
    t2.forward(dist)

    angle=random.randrange(0, 360)
    dist = random.randrange(1, 100)
    t3.left(angle)
    t3.forward(dist)

    t1X=t1.xcor()
    t1Y=t1.ycor()
    t2X=t2.xcor()
    t2Y=t2.ycor()
    t3X=t3.xcor()
    t3Y=t3.ycor()

    t1t2Dist=math.sqrt((t1X-t2X)*(t1X-t2X)+(t1Y-t2Y)*(t1Y-t2Y))
    t1t3Dist = math.sqrt((t1X - t3X) * (t1X - t3X) + (t1Y - t3Y) * (t1Y - t3Y))
    t2t3Dist = math.sqrt((t2X - t3X) * (t2X - t3X) + (t2Y - t3Y) * (t2Y - t3Y))


    if t1t2Dist<=20:
        t1.stamp()
        t2.stamp()
        size+=1
        t1.turtlesize(size)
        t2.turtlesize(size)
    elif t1t3Dist<=20:
        t1.stamp()
        t3.stamp()
        size+=1
        t1.turtlesize(size)
        t3.turtlesize(size)
    elif t2t3Dist <=20:
        t2.stamp()
        t3.stamp()
        size+=1
        t2.turtlesize(size)
        t3.turtlesize(size)

    if not -140 < t1X < 140 or not -140 < t1Y < 140:
        t1.goto(random.randrange(-140,140),random.randrange(-140,140))
    if not -140 < t2X < 140 or not -140 < t2Y < 140:
        t2.goto(random.randrange(-140,140),random.randrange(-140,140))
    if not -140 < t3X < 140 or not -140 < t3Y < 140:
        t3.goto(random.randrange(-140,140),random.randrange(-140,140))

turtle.done()