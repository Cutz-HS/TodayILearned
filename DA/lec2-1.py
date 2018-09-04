import csv
import numpy as np
import pandas as pd

# lec1 test
#a=[1,3,5,7,9,0,2,4,6,8]
#print(a[len(a)-1::-1])
#print(a[-2::-2])

def read_car():
    f=open('data/cars.csv', 'r')
    rows=[]
    for row in f:
#        print(row)
        rows.append(row.strip().split(','))
    f.close()
    return rows

def write_car(rows):
    f=open("data/cars.txt", "w", newline='')
    writer=csv.writer(f, delimiter=":")
    for row in rows:
        writer.writerow(row)
    f.close()

a=np.array([1,3,5])
#print(a)
#print(type(a))
#
b=np.arange(7)
#print(b)

c=np.arange(3,7,0.1)
#print(c)
#print(b < 4)
#print(b[b<4])

d=np.arange(15).reshape(3,5)
#print(d.shape)
#print(d.reshape(3,5))
d2=d.reshape(3,5)+1
#print(d2[d2>5])

#d2=np.arange(48).reshape(2,3,4,2)
#print(d2)

#print(d[-1])
#print(d[0][0])
#print(d[-1][0])
#print(d[-1,0])
#print(d[::-1][::-1])
#print(d[::-1,::-1])
#print(d[1:3, 2:4])
#print(d.sum())
#print(d.sum(axis=1))

# 길이가 1~10인 정사각형 중, 길이가 짝수인 정사각형 넓이
#areas=[np.arange(i*i).reshape(i,i)+1 for i in range(1,11) if not i%2]
#print(areas)
        
#[(0,0),(0,1),(0,2)....(0,n)]
#areas=[(i,j) for i in range(3) for j in range(3)]
#print(areas)

students=['아톰', '똘이', '몽키', '철이']
stu_dict= {"{}번".format(number+1):name for number, name in enumerate(students)}
print(stu_dict)
#print(dict(enumerate(students)))

scores=[80,70,90,100]

score_dict=dict(zip(students, scores))
print(score_dict)

stu_dic={students:"{}점".format(scores) for students, scores in zip(students, scores)}
print(stu_dic)

a1=[i for i in range(5)]
print(a1)
a2=[a1[i]-i for i in range(5)]
print(a2)

a3=[[0,1] for _ in range(5)]
print(pd.DataFrame(a3))














































