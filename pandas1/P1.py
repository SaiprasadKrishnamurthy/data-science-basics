import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/saikris/PycharmProjects/python1/nyc_weather.csv")
plt.plot(np.arange(df['Temperature'].size), df['Temperature'], np.arange(df['Humidity'].size), df['Humidity'])
print(df[df['Events'] == 'Rain']['EST'])
print(df.head())
print(df.columns)

g = df.groupby("Events")
for e, f in g:
    print(e)
    print(f)
    print(" -------------- ")

df = pd.DataFrame({
    "city": ["chennai", "mumbai", "delhi"],
    "power_consumed": [100, 200, 300]
})

df1 = pd.DataFrame({
    "city": ["london", "cardiff", "plymouth"],
    "waste_disposed": [30, 10, 15]
})
print(pd.merge(df, df1, on="city", how="outer"))
