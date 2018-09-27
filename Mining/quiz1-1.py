import turtle
import random
import tkinter as tk

# 퀴즈1. 거북이 완성하기

# 함수 선언
def clickLeft(x, y):
    '''
    (x, y) = 파라미터, 클릭한 위치
    '''
    r, g, b = random.random(), random.random(), random.random()
    turtle.pencolor((r, g, b))
    turtle.pensize(random.randint(1,20))
    turtle.pendown()
    turtle.goto(x,y)
    
def clickRight(x, y):
    '''
    그리지 않고 이동
    '''
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def clickMid(x, y):
    '''
    거북이 색상과 크기 변경
    '''
    turtle.shapesize(random.randint(1,10))
    r, g, b = random.random(), random.random(), random.random()
    turtle.color((r,g,b))
    
def clickDouble(x, y):
    '''
    더블클릭할 때, 그 전 자리로
    '''
    turtle.undo()


# 변수 선언
penSize = 0
r,g,b = [0]*3

# 메인 코드
if __name__=='__main__':
    turtle.title("거북이 그리기")
    turtle.shape('turtle')
    turtle.onscreenclick(clickLeft, 1)
#    turtle.onscreenclick(None, 1)
    turtle.onscreenclick(clickMid, 2)
    turtle.onscreenclick(clickRight, 3)
    turtle.done()