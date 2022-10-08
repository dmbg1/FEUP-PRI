# Drop columns from original file

import pandas as pd

data = pd.read_csv("./data/fake.csv")

data.rename(columns={"text": "body"}, inplace=True)
data.drop(inplace=True, columns=['uuid', 'ord_in_thread','crawled','main_img_url', 'domain_rank','replies_count','participants_count','likes', 'comments', 'shares', 'thread_title'])

data.to_csv('./data/fake_clean.csv', index=False)