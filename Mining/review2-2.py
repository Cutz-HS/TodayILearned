# Q2

# 함수 선언
def all_sum(num):
    hap = 0
    sNum = int(str(num)[0])
    fNum = int(str(num)[len(str(num))-1])
    if sNum < fNum:
        for i in range(sNum, fNum+1):
            hap += i
    elif sNum == fNum:
        for i in range(sNum+1):
            hap += i
    else:
        for i in range(fNum, sNum+1):
            hap += i
    return hap

# 메인 코드
for i in range(2,10):
    for j in range(1, 10):
        print(i, " X ", j, " = ", all_sum(i*j))