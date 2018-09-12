import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import json

'''json'''
js=json.load(open('d:/data/database.json'))
#print(len(js))
#print(js[0].keys())
#print(js[0]['nutrients'])

nutrients=DataFrame(js[0]['nutrients'])
#print(nutrients.head(7))

info_keys=['description', 'group', 'id', 'manufacturer']

info=DataFrame(js, columns=info_keys)
#print(info['description'])
#print(info.info())

#print(pd.value_counts(info.group))

'''duplicated'''
nutrients=[]
for rec in js:
    fnuts=DataFrame(rec['nutrients'])
    fnuts['id']=rec['id']
    nutrients.append(fnuts)
print(len(nutrients))
print(nutrients[0].drop_duplicates())
print(nutrients[0])