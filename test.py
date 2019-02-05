import pandas as pd
from collections import Counter
import json

df = pd.read_csv('dior.csv')
lst = ['category', 'colour', 'country', 'gender']
result = {}
for i in lst:
    result[i] = dict(Counter(df[i]))
for i in result.keys():
    for j in result[i].keys():
        result[i][j] = result[i][j]/len(df) * 100
result['count'] = len(df)
f = open('test.json', 'w')
f.write(json.dumps(result))
f.close()
