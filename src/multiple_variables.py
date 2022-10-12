# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("../data/fake_clean.csv")

temp_data = data.drop(columns=['author', 'published', 'title', 'body', 'language', 'site_url', 'type'])

average_dict = {}

for c in temp_data['country'].unique():
    average_dict[c] = (temp_data.loc[temp_data['country'] == c, 'spam_score'].mean())

fig = plt.figure(figsize=(10, 5))
plt.bar(average_dict.keys(), average_dict.values())
plt.xlabel('Country')
plt.ylabel('Average spam score')
plt.title('Average spam score per country')
plt.show()

temp_data = data.drop(columns=['author', 'published', 'title', 'body', 'language', 'country', 'spam_score'])

result_data = pd.DataFrame(data={'site_url':temp_data['site_url'].unique()})
result_data['type'] = ""

for site in result_data['site_url'].unique():
    result_data.loc[result_data['site_url'] == site, 'type'] = temp_data[temp_data['site_url'] == site]['type'].unique()[0]

fig = plt.figure(figsize=(10, 5))
plt.bar(result_data['type'].value_counts().index, result_data['type'].value_counts().array)
plt.xlabel('Type of fake news')
plt.ylabel('Number of websites')
plt.title('Number of websites that write fake news of each specific type')
plt.show()
