# Replace 'null' authors with 'Anonymous'

import pandas as pd

data = pd.read_csv("../data/fake_clean.csv")

data['author'].fillna('Anonymous',inplace=True)

data.to_csv('../data/fake_clean.csv', index=False)