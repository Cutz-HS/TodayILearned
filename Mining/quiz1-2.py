import turtle

# Quiz 2


# 2진수 표현
# 함수 선언
def binary_draw(num, curX, curY):
    binary = bin(num)
    for i in range(len(binary)-2):
        turtle.goto(curX, curY)
        if num & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        curX -= 50
        num >>= 1 
        turtle.stamp()
        
def oct_draw(num, curX, curY):
    '''
    8진수를 size에 따라 거북이 그리기
    '''
    octnum = oct(num)
    for j in range(len(octnum)-1, 1, -1):
        print(j)
        turtle.goto(curX, curY)
        turtle.color('red')
        turtle.turtlesize(int(octnum[j]))
        curX -= 100
        turtle.stamp()
    turtle.done()

# 변수
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

# 메인 코드
def main():
    turtle.title('2진수')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)
    
    num1 = int(input("숫자1: "))
    num2 = int(input("숫자2: "))
    curX = swidth / 2
    curY = sheight / 2 - 50
    binary_draw(num1, curX, curY)
    binary_draw(num2, curX, curY-50)
    binary_draw(num1&num2, curX, curY-100)
    
    # 심화 Quiz
    # 8진수 표현 -> num 1로
    oct_draw(num1, curX, curY-200)
    turtle.done()
    
if __name__ == '__main__':
    main()