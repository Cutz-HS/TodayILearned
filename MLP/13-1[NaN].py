### confusion matrix ###
### 결측치 처리 ###
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


sns.set(font_scale=2)
array = [[9, 1, 0 ,0],
         [1, 15, 3, 1],
         [5, 0, 24, 1],
         [0, 4, 1, 15]]

df_cm = pd.DataFrame(array, index=[i for i in "ABCD"], columns=[i for i in "ABCD"])
plt.figure()
sns.heatmap(df_cm, annot=True)
plt.show()