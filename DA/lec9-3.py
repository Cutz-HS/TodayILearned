import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib as mpl
import matplotlib.pylab as plt

np.random.seed(777)

#plt.title("Plot")
#plt.plot([10,20,30,40], [1,4,9,16], 'bD-.')
#plt.xlim(0,50)
#plt.show()
#print(np.pi)
#x=np.linspace(0, np.pi*2, 256)
#c=np.sin(x)
#plt.plot(x,c)
#plt.xticks([0, np.pi/2, np.pi, np.pi*3/2, np.pi*2])
#plt.yticks([-1,0,1],['low','zero','high'])

#t=np.arange(0.,5.,0.2)
#plt.plot(t,t,'r--',t,0.5*t**2, 'bs:', t,0.2*t**3, 'g^-')

#x=np.linspace(0, np.pi*2, 256)
#c,s, t=np.cos(x), np.sin(x), np.tan(x)
#plt.plot(x,c,ls='--', label="cosine")
#plt.plot(x,s,ls=':', label="sin")
#plt.plot(x,t,ls='--', label="tan")
#plt.legend()
#plt.ylim(-1.00, 1.00)
#plt.xlabel("pi")
#plt.ylabel("-1<=y<=1")

#plt.figure(figsize=(10,2))
#plt.plot(np.random.randn(100))
#plt.show()

#f1=plt.figure(1)
#plt.plot([1,2,3,4],'ro:')
#f2=plt.gcf()
#print(f1, id(f1))
#print(f2, id(f2))


x1=np.linspace(0.0, 5.0)
#print(x1)
x2=np.linspace(0.0,2.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)
plt.plot(x1, y1, 'yo-', x2, y1, 'ro-')
plt.legend()
plt.show()

ax1=plt.subplot(2,1,1)
















