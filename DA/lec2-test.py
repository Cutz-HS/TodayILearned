# Q1. 1~100000 사이에 있는 7의 개수
print(sum([str(i).count('7') for i in range(1,100001)]))

# Q2. Maria 평균
maria={'kor':94, 'eng':91, 'math':89, 'sci':83}
print(sum(maria.values())/len(maria))

# Q3. self num
num = range(1,5000)
selfnum = [sum(int (i) for i in str(j)) + j for j in num]
result = set(num) - set(selfnum)
print(sum(result))