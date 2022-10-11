from calendar import c
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./data/fake.csv")

def generate_frequency_pie_chart(column_name, pie_chart_title, gen_file_name):
    frequency = df[column_name].value_counts()
    plt.pie(frequency, labels=np.where(frequency / len(df) >= 0.1, frequency.index, ""))
    plt.title(pie_chart_title)
    plt.savefig("./data/plots/" + gen_file_name + ".png")
    plt.close()

generate_frequency_pie_chart("replies_count", "Reply Frequency", "replies_count_pie_chart")
generate_frequency_pie_chart("participants_count", "Comment Frequency", "participants_count_pie_chart")
generate_frequency_pie_chart("likes", "Like Frequency", "likes_pie_chart")
generate_frequency_pie_chart("comments", "Comment Frequency", "comments_pie_chart")
generate_frequency_pie_chart("shares", "Shares Frequency", "shares_pie_chart")

# NULL quantity 
# Columns that don't make sense keeping
# Duplicates