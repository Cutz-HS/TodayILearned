### SVM: sklearn ###
import random
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

random.seed(777)

## data 생성 ##
#fp = open("d:/data/prac/bmi.csv", mode="w", encoding="utf-8")
#fp.write("height,weight,label\r\n") # header
#cnt={"thin":0, "normal":0, "fat":0}
#
#def calc_bmi(h, w):
#    bmi = w / (h/100) ** 2
#    if bmi < 18.5: return "thin"
#    if bmi < 25: return "normal"
#    else: return "fat"
#
#for i in range(20000):
#    h = random.randint(130, 205)
#    w = random.randint(35, 110)
#    label = calc_bmi(h, w)
#    cnt[label] += 1
#    fp.write("{0},{1},{2}\r\n".format(h, w, label))
#fp.close()

## 전처리 ##
tbl = pd.read_csv("d:/data/prac/bmi.csv")
label = tbl["label"]
w = tbl["weight"] / 110
h = tbl["height"] / 205
wh = pd.concat([w, h], axis=1)

# split #
x_train, x_test, y_train, y_test = train_test_split(wh, label, train_size=0.7, random_state=77)

## SVM ##
clf = svm.SVC()
clf.fit(x_train, y_train)

yhat = clf.predict(x_test)

accuracy = len(yhat[np.equal(yhat, y_test)]) / len(yhat)
#print(accuracy)

ac_score = metrics.accuracy_score(y_test, yhat)
#print(ac_score)

cl_report = metrics.classification_report(y_test, yhat)
print(cl_report)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b['weight'], b['height'], c=color, lable=lbl)

scatter("fat", "red")
scatter("normal", "yellow")
scatter("thin", "purple")
ax.legend()
plt.show()












