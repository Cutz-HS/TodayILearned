import json
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

path="data/example.txt"
records=[json.loads(line) for line in open(path, encoding='utf-8')]

df=DataFrame(records)

clean_df=df[df.a.notnull()]
clean_df[clean_df.tz==""]="NaN"
os=np.where(clean_df.a.str.contains("Windows"),"Windows","Not Windows")
group_os=clean_df.groupby(['tz', os])
counts=group_os.size().unstack().fillna(0)
indexer=counts.sum(1).argsort(kind="mergesort")
res=counts.take(indexer)[-15:]

normed=res.div(res.sum(1), axis=0)
normed.plot(kind='barh', stacked=True)
plt.xlabel("Windows per")
plt.ylabel("City")
plt.show()