# Remove null values

import pandas as pd

data = pd.read_csv("./data/fake_clean.csv")

data = data[data['body'].notna()]              
data['body'] = data['body'].apply(lambda x: x.strip())
data = data[data['body'] != ""]              
data = data[data['title'].notna()]              # 5% Na Values
data = data[data['country'].notna()]            # 1% Na Values
data = data[data['language'] != 'ignore']
data.to_csv('./data/fake_clean.csv', index=False)