import turtle
import random

# 거북이 복습

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

# 변수 선언
penSize = 0
r,g,b = [0]*3

# 메인 코드
if __name__=='__main__':
    turtle.title("거북이가 그리기")
    turtle.shape('turtle')
    turtle.onscreenclick(clickLeft, 1)
    turtle.onscreenclick(clickRight, 3)
    
    turtle.done()