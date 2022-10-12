from calendar import c
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_frequency_pie_chart(column_name, pie_chart_title, gen_file_name):
    def my_autopct(pct):
        return ('%.2f' % pct) + "%" if pct > 10 else ''
        
    frequency = df[column_name].value_counts()
    plt.pie(frequency, labels=np.where(frequency / len(df) >= 0.1, frequency.index, ""), autopct=my_autopct)
    plt.title(pie_chart_title)
    plt.savefig("./data/plots/" + gen_file_name + ".png")
    plt.close()


def generate_null_bar_chart(): 
    X = ['title', 'country', 'body', 'author']

    title_col_non_nulls = round(df['title'].count() * 100 / len(df), 2)
    country_col_non_nulls = round(df['country'].count() * 100 / len(df), 2)
    body_col_non_nulls = round(df['text'].count() * 100 / len(df), 2)
    author_col_non_nulls = round(df['author'].count() * 100 / len(df), 2)

    non_null_percts = [title_col_non_nulls, country_col_non_nulls, body_col_non_nulls, author_col_non_nulls]
    null_percts = [100 - title_col_non_nulls, 100 - country_col_non_nulls, 100 - body_col_non_nulls, 100 - author_col_non_nulls]

    X_axis = np.arange(len(X))

    bar1 = plt.bar(X_axis - 0.2, non_null_percts, 0.4, label = 'Non-Nulls %')
    bar2 = plt.bar(X_axis + 0.2, null_percts, 0.4, label = 'Nulls %')

    plt.bar_label(bar1, fmt='%.1f%%', label_type='edge')
    plt.bar_label(bar2, fmt='%.1f%%', label_type='edge')

    plt.xticks(X_axis, X)
    plt.xlabel("Columns")
    plt.ylabel("Percentage of Nulls and Non-Nulls")
    plt.title("Amount of Nulls/Non-Nulls in the different columns")
    plt.legend()
    plt.savefig('./data/plots/nulls_plot.png')
    plt.close()

df = pd.read_csv("./data/fake.csv")

# Dropped Columns with Frequencies
generate_frequency_pie_chart("replies_count", "Reply Frequency", "replies_count_pie_chart")
generate_frequency_pie_chart("participants_count", "Comment Frequency", "participants_count_pie_chart")
generate_frequency_pie_chart("likes", "Like Frequency", "likes_pie_chart")
generate_frequency_pie_chart("comments", "Comment Frequency", "comments_pie_chart")
generate_frequency_pie_chart("shares", "Shares Frequency", "shares_pie_chart")

# Dropped NULLs in columns quantity
generate_null_bar_chart()