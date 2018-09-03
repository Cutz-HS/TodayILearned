import tensorflow as tf
import matplotlib.pyplot as plt

# Gradient Descent Algorithm
def cost_function(X,Y,W):
    cost=0
    for i in range(len(X)):
        hypothesis=W*X[i]
#        print(hypothesis)
        cost+=(hypothesis-Y[i])**2
    return cost/len(X)
    
    
x=[1,2,3]
y=[1,2,3]

w=10
#print(cost_function(x,y,w))
#print(cost_function(x,y,5))
#print(cost_function(x,y,1))

xxx, yyy=[], []
for i in range(-50, 71):
    w=i/10
    c=cost_function(x,y,w)
    xxx.append(w)
    yyy.append(c)
#    print(w, c)
    
plt.plot(xxx, yyy)
plt.plot(xxx,yyy,'ro')
plt.show()

