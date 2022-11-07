# Drop duplicates
# In case of repetitive Fake news, no need to save both


import pandas as pd

data = pd.read_csv("../data/fake_clean.csv")

aux = len(data)
data.drop_duplicates(inplace=True) # 31 rows
data.to_csv('../data/fake_clean.csv', index=False)