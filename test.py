#libs
import pandas as pd
from collections import Counter
import json

df = pd.read_csv('dior.csv') #open scraped data
lst = ['category', 'colour', 'country', 'gender'] # columns to be analyzed
result = {} # Empty dict
for i in lst:
    result[i] = dict(Counter(df[i])) # Count quantity of some subcategory
for i in result.keys():
    for j in result[i].keys():
        result[i][j] = result[i][j]/len(df) * 100 # From count to percentage
result['count'] = len(df) # general qantity of products
f = open('test.json', 'w') 
f.write(json.dumps(result)) # result to file
f.close()
