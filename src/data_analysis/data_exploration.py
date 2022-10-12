import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./data/fake_clean.csv")

country_distribution = pd.DataFrame({'lab':df['language'].unique(), 'val':[10, 30, 20]})

fig = plt.figure(figsize=(10, 5))
plt.bar(df['language'].unique(), df["language"].value_counts())
plt.show("./data/plots/avg_spam_per_country.jpg")