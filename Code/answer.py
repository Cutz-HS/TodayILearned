#파이썬 코드 연결 링크																									
																									
																									
myList=[]																									
cnt=0																									
a=0																									
																									
def hap(a1,a2,a3=0,a4=0,a5=0,a6=0,a7=0,a8=0,a9=0,a10=0):																									
    if cnt == 2:																									
        result = a1+a2																									
    elif cnt == 3:																									
        result = a1+a2+a3																									
    elif cnt == 4:																									
        result = a1+a2+a3+a4																									
    elif cnt == 5:																									
        result = a1 + a2 + a3 + a4 +a5																									
    elif cnt == 6:																									
        result = a1 + a2 + a3 + a4 +a5 +a6																									
    elif cnt == 7:																									
        result = a1 + a2 + a3 + a4 + a5 +a6 +a7																									
    elif cnt == 8:																									
        result = a1 + a2 + a3 + a4 + a5 +a6+a7 +a8																									
    elif cnt == 9:																									
        result = a1 + a2 + a3 + a4 + a5 +a6+a7 +a8 +a9																									
    elif cnt == 10:																									
        result = a1 + a2 + a3 + a4 + a5 +a6+a7 +a8 +a9 +a10																									
    else:																									
        print("너무 많이 입력하셨네요")																									
    return result																									
																									
for i in range(0,10):
    # 수정부분 // int("") Error를 무시하는 방향이기 때문에 (다른 Value Error에도 반응), 완전한 정답은 아닙니다.
    try:
        str = int(input("숫자를 입력하세요 => "))																									
        myList.append(str)																				
        cnt +=1
        if myList=="":
            pass
    except ValueError:
        break															
																							
if cnt == 2:																									
    res = hap(myList[0],myList[1])																									
elif cnt == 3:																									
    res = hap(myList[0],myList[1],myList[2])																									
elif cnt == 4:																									
    res = hap(myList[0],myList[1],myList[2],myList[3])																									
elif cnt == 5:																									
    res = hap(myList[0],myList[1],myList[2],myList[3],myList[4])																									
elif cnt == 6:																									
    res = hap(myList[0],myList[1],myList[2],myList[3],myList[4],myList[5])																									
elif cnt == 7:																									
    res = hap(myList[0],myList[1],myList[2],myList[3],myList[4],myList[5],myList[6])																									
elif cnt == 8:																									
    res = hap(myList[0],myList[1],myList[2],myList[3],myList[4],myList[5]																									
,myList[6],myList[7])																									
elif cnt == 9:																									
    res = hap(myList[0],myList[1],myList[2],myList[3],myList[4],myList[5]																									
,myList[6],myList[7],myList[8])																									
elif cnt == 10:																									
    res = hap(myList[0],myList[1],myList[2],myList[3],myList[4],myList[5]																									
,myList[6],myList[7],myList[8],myList[9])																									
else:																									
    print("너무 많이 입력했네")																									
																									
print(res)																									
																									
																								
