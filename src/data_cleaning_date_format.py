
import pandas as pd

data = pd.read_csv("./data/fake_no_na.csv")

data.drop_duplicates(inplace=True)

data.to_csv('./data/fake_clean.csv',sep=';', index=False)