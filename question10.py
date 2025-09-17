import pandas as pd

df = pd.read_csv('Advertising.csv')

print(df)
print(df.head())
print(df.tail())
print(df.columns)
print(df.tail(3))
print(df.describe())
print(df.info())
print(df.dtypes)
print(df.isnull().sum())
print(df.dropna())
print(df.drop('radio', axis=1))
df['updated_sales'] = df['sales'] * 1.1
print(df)
print(df.shape)
