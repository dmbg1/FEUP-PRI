# Using multi_rake

from multi_rake import Rake
import pandas as pd

fake_data = pd.read_csv("./data/fake_clean.csv")
rake = Rake()
keywords = list()
for index, row in fake_data.iterrows():
    if(index == 1): break
    keywords.append(rake.apply(row['body']))
    
print(keywords[:10][:10])
    