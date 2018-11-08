import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


## PCA ##
# 5차원 데이터 #
df = pd.DataFrame(columns=['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape'])
df.loc[0] = [1200, 1, 0, 0, 2, 'Skinny']
df.loc[1] = [2800, 1, 1, 1, 1, 'Normal']
df.loc[2] = [3500, 2, 2, 1, 0, 'Fat']
df.loc[3] = [1400, 0, 1, 0, 3, 'Skinny']
df.loc[4] = [5000, 2, 2, 2, 0, 'Fat']
df.loc[5] = [1300, 0, 0, 1, 2, 'Skinny']
df.loc[6] = [3000, 1, 0, 1, 1, 'Normal']
df.loc[7] = [4000, 2, 2, 2, 0, 'Fat']
df.loc[8] = [2600, 0, 2, 0, 0, 'Normal']
df.loc[9] = [3000, 1, 2, 1, 1, 'Fat']

X = df[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
y = df[['body_shape']]
x_std = StandardScaler().fit_transform(X)

# 공분산 행렬 #
features = x_std.T
cov = np.cov(features)

# 고유벡터, 고유값 #
eig_vals, eig_vecs = np.linalg.eig(cov)
projected_X = x_std.dot(eig_vecs.T[0])
#print(projected_X)

res = pd.DataFrame(projected_X, columns=['PC1'])
res['y-axis'] = 0.0
res['label'] = y

sns.lmplot('PC1', 'y-axis', data=res, scatter_kws={"s":50}, hue='label')
plt.title('PCA result')
plt.show()























