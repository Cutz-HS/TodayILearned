import math
import pandas as pd
from scipy.spatial import distance

with open("d:/data/prac/nba_2013.csv", "r") as csvfile:
    nba = pandas.read_csv(csvfile)
    
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga',
       'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft',
       'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf',
       'pts']

## 표준화 ##
nba_numeric = nba[distance_columns]
nba_norm = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()
#nba[distance_columns] = nba_norm
nba_norm.fillna(0, inplace=True)

selected_player = nba_norm[nba["player"]=="LeBron James"]

def euclidean_distance(row):
    inner_value = 0
    for k in distance_columns:
        inner_value += (selected_player[k] - row[k])**2
    return math.sqrt(inner_value)

dist = nba_norm.apply(lambda row: distance.euclidean(row, selected_player), axis=1)

d_frame = pd.DataFrame(data={'dist': dist, 'idx': dist.index})
d_frame = d_frame.sort_values(by=['dist'], ascending=True)