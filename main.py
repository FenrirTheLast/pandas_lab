import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'], 'Stolica': ['Brukselia', 'New Delhi', 'Brasilia'], 'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal='.')
print(df)
# df.to_csv('plik.csv', index=False)

print(s ['c'])
print(s.c)
print(df[0:1])
print("")
print(df['Populacja'])
print(df.iloc[0, 0])
print(df.loc[0, "Kraj"])
print(df.at[0, "Kraj"])

print(df[1:0])
print(df["Populacja"])
print(df.iloc[0, 0])
print(df.loc[0, "Kraj"])
print('kraj:' + df.Kraj)
print(df.sample())

print(df.sample(2))
print(df.sample(frac=0.5))
print(df.sample(n=10, replace=True))
print(df.head(2))
print(df.tail(1))
print(df.describe())
print(df.T)
