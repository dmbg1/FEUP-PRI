
import pandas as pd

data = pd.read_csv("./data/fake_clean.csv")

#print(data['language'].unique())

langsToRemove = []

for lang in data['language'].unique():
    print(lang, len(data[data['language'] == lang]))
    if(len(data[data['language'] == lang]) < 15):
        langsToRemove.append(lang)

print(langsToRemove)

data = data[~data['language'].isin(langsToRemove)]

print(data['language'].unique())

data['body_en'] = None
data['body_de'] = None
data['body_fr'] = None
data['body_es'] = None
data['body_ru'] = None
data['body_ar'] = None

data.loc[data['language'] == 'english', 'body_en'] = data['body']
data.loc[data['language'] == 'german', 'body_de'] = data['body']
data.loc[data['language'] == 'french', 'body_fr'] = data['body']
data.loc[data['language'] == 'spanish', 'body_es'] = data['body']
data.loc[data['language'] == 'russian', 'body_ru'] = data['body']
data.loc[data['language'] == 'arabic', 'body_ar'] = data['body']

data.drop(columns=['body'], inplace=True)

data.to_csv('./data/fake_clean_body_split.csv', index=False)