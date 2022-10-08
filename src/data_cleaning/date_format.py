
import pandas as pd
from datetime import datetime 

data = pd.read_csv("./data/fake_clean.csv")

data['published'] = [datetime.fromisoformat(x) for x in data['published']]

data.to_csv('./data/fake_clean.csv', index=False)