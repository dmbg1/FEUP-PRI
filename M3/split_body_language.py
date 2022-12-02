
import pandas as pd

data = pd.read_csv("./data/fake_clean.csv")

data.drop_duplicates(subset=['title', 'site_url'], inplace=True)

langsToRemove = []

""" for lang in data['language'].unique():
    print(lang, len(data[data['language'] == lang]))
    if(len(data[data['language'] == lang]) < 25):
        langsToRemove.append(lang) """

#print(langsToRemove)

data = data[~data['language'].isin(langsToRemove)]

#print(data['language'].unique())

data['title_en'] = None
data['title_de'] = None
data['title_fr'] = None
data['title_es'] = None
data['title_ru'] = None

data.loc[data['language'] == 'english', 'title_en'] = data['title']
data.loc[data['language'] == 'german', 'title_de'] = data['title']
data.loc[data['language'] == 'french', 'title_fr'] = data['title']
data.loc[data['language'] == 'spanish', 'title_es'] = data['title']
data.loc[data['language'] == 'russian', 'title_ru'] = data['title']

data.drop(columns=['title'], inplace=True)

data['body_en'] = None
data['body_de'] = None
data['body_fr'] = None
data['body_es'] = None
data['body_ru'] = None

data.loc[data['language'] == 'english', 'body_en'] = data['body']
data.loc[data['language'] == 'german', 'body_de'] = data['body']
data.loc[data['language'] == 'french', 'body_fr'] = data['body']
data.loc[data['language'] == 'spanish', 'body_es'] = data['body']
data.loc[data['language'] == 'russian', 'body_ru'] = data['body']

data.drop(columns=['body'], inplace=True)

data['id'] = data.index

data.to_csv('./data/fake_clean_lang_split.csv', index=False)