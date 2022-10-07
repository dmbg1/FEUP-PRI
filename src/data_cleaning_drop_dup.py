# Drop duplicates
# In case of repetitive Fake news, no need to save both


import pandas as pd

data = pd.read_csv("./data/fake_no_na.csv")

data.drop_duplicates(inplace=True)

data.to_csv('./data/fake_no_dup.csv',sep=';', index=False)