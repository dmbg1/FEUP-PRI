# Using multi_rake

from multi_rake import Rake
import pandas as pd

fake_data = pd.read_csv("./data/fake_clean.csv")
rake = Rake(max_words=1)
body = ', '.join(fake_data['body'])
body = ''.join(x for x in body if (x.isalpha() or x == ' '))
keywords = rake.apply(body)



print(keywords[:10])