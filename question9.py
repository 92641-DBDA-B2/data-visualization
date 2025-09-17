import pandas as pd

empid = list(range(1,11))
temp = range(ord('a'),ord('k'))
names = [chr(i) for i in temp]

empid_series = pd.Series(empid)
names_series = pd.Series(names)


df = pd.DataFrame({'employee id':empid_series, 'names':names_series})
print(df)
print(df.head())
print(df.tail())
df.to_csv('MyRecord.csv', index= False)