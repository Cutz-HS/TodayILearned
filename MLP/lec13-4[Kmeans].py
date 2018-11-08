import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
labels = pd.DataFrame(iris.target)
labels.columns = ['labels']

data = pd.DataFrame(iris.data)
data.columns = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width']
data = pd.concat([data, labels], axis=1)
feature = data[['Sepal_length', 'Sepal_width']]

model = KMeans(n_clusters=5, algorithm='auto')
scaler = StandardScaler()
pipeline = make_pipeline(scaler, model)
pipeline.fit(feature)
predict = pd.DataFrame(pipeline.predict(feature))
ks = range(1,10)
inertias = []
for k in ks:
    model = KMeans(n_cluster=k)
    model.fit(feature)
    inertias.append(model.inertia_)


predict.columns = ['predict']
r = pd.concat([feature, predict], axis=1)

plt.scatter(r['Sepal_length'], r['Sepal_width'], c=r['predict'], alpha=0.5)

centers = pd.DataFrame(model.cluster_centers_, columns=['Sepal_length', 'Sepal_width'])

#center_x = centers['Sepal_length']
#center_y = centers['Sepal_width']
#plt.scatter(center_x, center_y, s=50, marker='D', c='r')
#plt.show()