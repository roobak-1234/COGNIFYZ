# -*- coding: utf-8 -*-
"""Feature Engineering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iXKw3GVjerXmdN95kou9VJVIUzgwUgME
"""

import pandas as pd

from google.colab import drive

data=pd.read_csv("/content/drive/MyDrive/Dataset .csv")

df = pd.DataFrame(data)

df

df['Res_length'] = df['Restaurant Name'].apply(len)
df['address_length'] = df['Address'].apply(len)

print("Data with Additional features:")
print(df)

df

df['Has Table booking'] = df['Has Table booking'].apply(lambda x: 1 if x else 0)
df['Has Online delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x else 0)

print("Data with new Categorical variables:")
print(df)

df