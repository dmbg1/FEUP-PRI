from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pylab as plt

# Words to avoid on the wordcloud construction
stopwords = set(STOPWORDS)
stopwords.add('s')
stopwords.add('U')
stopwords.add('will')
stopwords.add('one')

data = pd.read_csv("../data/fake_clean.csv")

#wordcloud
wordcloud = WordCloud(stopwords=stopwords, width=1600, height=800).generate(''.join(data['body']))

plt.figure(figsize=(10, 5), facecolor='k')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig("../data/plots/word_cloud.png")
plt.close()