a=4.2E7 # E7 -> 지수(4.2 * 10^7)
print(a)

a=4.2E-7 # E-7 -> 10^-7
print(a)

print(7/4)
print(7//4) # 몫만 return
print(7%4) # 나머지만 return

# 다중주석 / 제어문자
msg="""
life is \ntoo short
you need Python
"""
print(msg)
print("-"*100)

# string index output
a="Life"
print(a[0])
print(a[-2])
print(a[1:3])

# formatting
print("I ate {1} apples so I was sick for {0} days".format(3,4))
pi=3.14
print("{0:10.4f}".format(pi))

# join
a=","
('abcd')
print(a.join('abcd'))
msg="Life:is:too:short"
#msg=msg.replace("Life", "Your leg")
print(msg)
print(msg.split()) # 공백
print(msg.split(":"))

# slicing
a=[1,2,3,['a','b',['c','d']]]
print(a[3][-1][1])

# list assign
a=[4,5,6]
a[2]=7
print(a)
a[a.index(5)]=['a','b','c']
print(a)
a[1:2]=['a','b','c']
print(a)

# value delete
a.remove("a") # 1 value
del a[1:3] ; print(a)
a[1:3] = [] ; print(a)

sumfun = lambda a, b: a+b
print(sumfun(2,5))

def sum2(*v):
    sum=0
    for i in v:
        sum+=i
    return sum

sum2 = lambda *v: sum=0, sum=sum+v

print(sum2(5,2))

# 파일처리
f=open("test.txt", "w", encoding="utf-8")
# text encoding-> ASCII / BCD / EBCDIC / UNICODE(UTF) / MS949 / EUC-KR ...

for i in range(1,11):
    f.writelines("메롱메롱 %d번 \n" %i)
    
f.close()

f=open("test.txt", "r", encoding="utf-8")
print(f)
#for i in f:
#    print(i, end="")
#while True:
#    line=f.readline()
#    if not line: break
#for i in f.readlines(): #list
#    print(i, end="")
data=f.read()
print(data)
f.close()

f=open("test.txt", "a", encoding='utf-8')
for i in range(11,15):
    data="%번째 줄입니다. \n" %i
f.close()

 input.txt 파일
 모든 숫자를 읽어 총합과 평균을 구하고 화면에 출력,
 result.txt파일에도 출력

inputFile=open("input.txt", "w")
inputFile.write("70\n55\n90\n87\n38")
inputFile.close()

readFile=open("input.txt", "r")
sumNum=0
allList=readFile.readlines()
for i in allList:
    sumNum+=int(i)
#allList=[sum for i in readFile.readlines() sum+=int(i)]
readFile.close()

inputFile2=open("result.txt", "w")
inputFile2.write("sum: %d \n" %sumNum)
mean=sumNum/len(allList)
inputFile2.write("mean: %0.1f" %mean)
print("mean: %0.1f" %mean)
inputFile2.close()






















