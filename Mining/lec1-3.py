import turtle
import random

# 사춘기 거북이

# 변수 선언부
swidth, sheight, penSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0]*7


# 메인코드
def main():
    global exitCount
    turtle.shape('turtle')
    turtle.pensize(penSize)
    turtle.setup(width=swidth+30, height=sheight+30)
    turtle.screensize(swidth, sheight)
    while True:
        if exitCount == 3:
            break
        r, g, b = random.random(), random.random(), random.random()
        turtle.pencolor((r,g,b))
        angle = random.randrange(0,360)
        dist = random.randint(0, 100)
        turtle.left(angle)
        turtle.forward(dist)
        curX = turtle.xcor()
        curY = turtle.ycor()
        if -swidth/2 < curX < swidth/2 and -sheight/2 < curY < sheight/2:
            pass
        else:
            turtle.penup()
            turtle.home()
            turtle.pendown()
            exitCount+=1
    return

if __name__ == '__main__':
    main()
    turtle.done()