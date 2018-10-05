import codecs
import json
from collections import Counter
from collections import defaultdict

path='example.txt'
fileRead=codecs.open(path).readline()
rec=[json.loads(line) for line in codecs.open(path, encoding='utf-8')]
time_zones=[myRec['tz'] for myRec in rec if 'tz' in myRec and myRec['tz']!=""]

def get_count(list):
    count=Counter(list)
    return count.most_common()

def get_count2(list):
    counts=defaultdict(int)
    for x in list:
        counts[x]+=1
    return counts

time_dict=dict(get_count(time_zones))
time_dict2=get_count2(time_zones)