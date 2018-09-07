import numpy as np

'''
다음 배열은 첫번째 행(row)에 학번, 두번째 행에 영어 성적, 세번째 행에 수학 성적을 적은 배열이다. 
영어 성적을 기준으로 각 열(column)을 재정렬하라.
array([[  1,    2,    3,    4],
       [ 46,   99,  100,   71],
       [ 81,   59,   90,  100]])

실수로 이루어진 5 x 6 형태의 데이터 행렬을 만들고 이 데이터에 대해 다음과 같은 값을 구한다.
1.전체의 최댓값
2.각 행의 합
3.각 열의 평균
'''
# Q1. fancy indexing
score=np.array([[  1,    2,    3,    4],
                [ 46,   99,  100,   71],
                [ 81,   59,   90,  100]])

score_rank=score[2].argsort()
scoreE=score.take(score_rank, axis=1)
print("ANSWER 1")
print(scoreE)

# Q2. matrix
rand=np.random.randint(1,100, (5,6))
#1
print("="*50, "\nANSWER 2")
print(np.max(rand))
print(np.sum(rand, axis=1))
print(np.mean(rand, axis=0))