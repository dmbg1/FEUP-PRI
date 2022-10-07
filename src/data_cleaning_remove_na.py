# Remove null values

import pandas as pd

data = pd.read_csv("./data/fake.csv")

data.drop_duplicates(inplace=True)

data.to_csv('./data/fake_no_na.csv',sep=';', index=False)