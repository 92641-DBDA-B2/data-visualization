import pandas as pd

df = pd.read_csv('Salaries .csv')

print(df)
print(df.head())
print(df.head(10))
print(df.tail())
print(df.tail(10))
print(df.columns)
print(df.shape)
print(df.describe())
print(df.info())
print(df.dtypes)
print(df.isnull().sum())
