### Q1: SNS data: KNN(결측치처리) & K-means ###
### Q1+: PCA -> K-means ###
### Q1+: SNS data: random forest -> gender prediction ###
### Q1+: deep learning: age prediction -> NA 대체 ##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

### Q1: SNS data ###
## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/snsdata.csv") # shape(30000, 40)
trim_data = all_data.drop(['age'], axis=1) # NA값이 많은 age feature 제거



## Q1+: KNN 결측치 대체 ##
gender_na = all_data['gender'].isna() # gender na 추출
gender = all_data[gender_na == False] # gender NA값 제외 --> shape(27276, 40)
gender_na = all_data[gender_na] # shape(2724, 40)

## gender 결측치 채우기: KNN ##
X = gender.iloc[:, 2:] # shape(27276, 38)
y = gender[['gender']] # shape(27276, 1)

# scaling #
mm = MinMaxScaler()
X_scale = mm.fit_transform(X)

# split #
x_train, x_test, y_train, y_test = train_test_split(X_scale, y, train_size=0.7, test_size=0.3, random_state=77)

# KNN #
### Q1+: k tuning graph ###
k_chart = np.zeros((10, 2)) # K_value, acc
k_chart = pd.DataFrame(k_chart)
k_chart.columns = ["K_value", "acc"]
k_list = [3,5,7,9,15,17,19,25,31,41]

## train ##
#for i in range(len(k_list)): # [1,3,5,7,9,11,13,15,17,19]로 각각의 k 모델링
#    knn = KNeighborsClassifier(n_neighbors=k_list[i], p=2, metric='minkowski')
#    knn.fit(x_train, y_train)
#    predict = knn.predict(x_test).reshape(len(x_test), 1)
#    acc = np.equal(y_test, predict)
#    accuracy = len(predict[acc]) / len(y_test)
#    k_chart.iloc[i, 0] = k_list[i]
#    k_chart.iloc[i, 1] = accuracy
#    
## 시각화 ##
#plt.figure(figsize=(13,5))
#plt.xlabel("K-value")
#plt.ylabel("accuracy")
#plt.plot(k_chart["K_value"], k_chart["acc"], "r-") # k값이 커짐에 따라 82% 정도에 수렴

knn = KNeighborsClassifier(n_neighbors=21, p=2, metric='minkowski')
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test).reshape(len(x_test), 1)
predict = np.equal(y_pred, y_test)
acc = len(y_pred[predict]) / len(y_test)
#print(acc) # 0.82

# confusion matrix #
print("\nKNN - <confusion matrics>\n", pd.crosstab(np.array(y_test).flatten(), np.array(y_pred).flatten(), rownames=["Actual"], colnames=["Predict"]))
print("\nKNN - <classification matrics>\n", classification_report(y_test, y_pred))
## confusion matrix와 classfication의 결과에 따라, 남성 재현율이 굉장히 낮음을 확인: 0.24 ##























