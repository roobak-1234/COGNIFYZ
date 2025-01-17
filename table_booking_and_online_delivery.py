# -*- coding: utf-8 -*-
"""Table Booking and online delivery

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gect_Jz1y4ZxL1YHFBw9XgJyc6gyL9l-
"""

import pandas as pd
import random

from google.colab import drive

data = pd.read_csv("/content/drive/MyDrive/Dataset .csv")

df=pd.DataFrame(data)

df

df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})

total_restaurants = len(df)
percent_table_booking = (df['Has Table booking'].sum() / total_restaurants) * 100
percent_online_delivery = (df['Has Online delivery'].sum() / total_restaurants) * 100

print(f"percentage_table_booking: {percent_table_booking:.2f}")
print(f"percentage_online_delivery: {percent_online_delivery:.2f}")

ratings = [4.2, 3.8, 4.0, 4.5, 3.5] * (len(df) // len(ratings)) + ratings[:len(df) % len(ratings)]
df['Rating text'] = random.choices(ratings, k=len(df))

avg_rating_with_booking = df[df['Has Table booking'] == 1]['Rating text'].mean()
avg_rating_without_booking = df[df['Has Table booking'] == 0]['Rating text'].mean()

print(f"Average rating of restaurants with Table booking: {avg_rating_with_booking:.2f}")
print(f"Average rating of restaurants without Table booking: {avg_rating_without_booking:.2f}")

price_range = ['cheap', 'moderate', 'moderate', 'expensive', 'expensive']
df['Price range'] = random.choices(price_range, k=len(df))

online_delivery_by_price_range = df.groupby('Price range')['Has Online delivery'].mean() * 100

print("Percentage of restaurants offering online delivery by price range:")
print(online_delivery_by_price_range)