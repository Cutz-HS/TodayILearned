from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler, minmax_scale
from sklearn.preprocessing import Binarizer
import numpy as np

''' One Hot Encoder
 범주형 자료를 One Hot 으로 '''
data_train= np.array([[0,0,0],
                      [0, 1, 1],
                      [0, 2, 2],
                      [1, 0, 3],
                      [1, 1, 4]])
enc=OneHotEncoder()

enc.fit(data_train)
#print(enc.active_features_)
#print(enc.feature_indices_)

data_new=np.array([[1,2,3]])
#print(enc.transform(data_new).toarray())


'''MinMaxScaler'''
X= np.array([[10.,-10.,1.],
             [5.,0.,2.],
             [0.,10.,3.]])

mms=MinMaxScaler()
xms=mms.fit_transform(X)
print(xms)
xms2=minmax_scale(X, axis=0, copy=True)
print(xms2)

'''Binarizer'''
bini=Binarizer(threshold=2.0)
binii=bini.fit_transform(X)
#print(binii)