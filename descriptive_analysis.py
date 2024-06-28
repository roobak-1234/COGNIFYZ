# -*- coding: utf-8 -*-
"""Descriptive analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dBIf_fbuD0xd82wbSJAQCJ0UnX5xSelZ
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive

df = pd.read_csv('/content/drive/MyDrive/Dataset .csv')

df.info()

df.describe()

print(df.describe())

categorical_columns = ["Country Code", "City", "Cuisines"]

for col in categorical_columns:
    print(df[col].value_counts())

top_cuisines = df['Cuisines'].value_counts().head(10)
print(top_cuisines)

top_cities = df['City'].value_counts().head(10)
print(top_cities)

df.hist(figsize=(10, 8))

plt.tight_layout()

plt.show()

sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))
sns.boxplot(data=df)
plt.show()

numeric_df = df.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()