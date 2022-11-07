import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_clean = pd.read_csv("../data/fake_clean.csv")

# Number of news per country
fig = plt.figure(figsize=(10, 5))
plt.bar(df_clean['country'].unique(), df_clean['country'].value_counts())
plt.title("Fake news amount per country")
plt.ylabel("News amount")
plt.xlabel("Country Code")
plt.savefig("../data/plots/nr_news_per_country.png")
plt.close()

# Number of news per language
fig = plt.figure(figsize=(15, 5))
plt.bar(df_clean['language'].unique(), df_clean['language'].value_counts(), width=0.5)
plt.title("Fake news amount per language")
plt.ylabel("News amount")
plt.xlabel("Language")
plt.savefig("../data/plots/nr_news_per_language.png")
plt.close()

# Number of news per website
fig = plt.figure(figsize=(10, 5))
plt.bar(df_clean['site_url'].unique(), df_clean['site_url'].value_counts(), align='edge', width=0.66)
plt.xticks(color='w')
plt.title("Fake news amount grouped by website")
plt.ylabel("News amount")
plt.xlabel("Websites")
plt.savefig("../data/plots/nr_news_per_website.png")
plt.close()


print("Min-date: " + df_clean['published'].min())
print("Max-date: " + df_clean['published'].max())