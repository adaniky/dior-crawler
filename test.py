import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
import json

df = pd.read_csv('dior.csv')
a = dict(Counter(df['category']))
b = dict(Counter(df['gender']))
for i in a.keys():
    a[i] = a[i]/ len(df) * 100
for i in b.keys():
    b[i] = b[i]/ len(df) * 100
plt.figure(figsize = (12,8))
plt.title('category')
plt.pie(a.values(), labels=a.keys(),
           autopct=None)
plt.show()
plt.figure(figsize = (12,8))
plt.title('gender')
plt.pie(b.values(), labels=b.keys(),
           autopct=None)
plt.show()
result = {'category':a, 'gender':b}
f = open('test.json', 'w')
f.write(json.dumps(result))
f.close()
