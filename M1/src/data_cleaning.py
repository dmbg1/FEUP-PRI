import pandas as pd
import numpy as np
from datetime import datetime


data = pd.read_csv("../data/fake.csv")

data.drop(inplace=True, columns=['uuid', 'ord_in_thread','crawled','main_img_url', 'domain_rank','replies_count','participants_count','likes', 'comments', 'shares', 'thread_title'])
data.rename(columns={"text": "body"}, inplace=True)

data['author'].fillna('Anonymous',inplace=True)

data = data[data['body'].notna()]              
data = data[data['title'].notna()]              # 5% Na Values
data = data[data['country'].notna()]            # 1% Na Values

data.drop_duplicates(inplace=True)

data['published'] = [datetime.fromisoformat(x) for x in data['published']]

print(data['published'].describe())

data.to_csv('../data/fakeNoNaNoDup.csv',sep=';', index=False)


print("Total:",len(data.index))
print(len(data['body'].unique()))