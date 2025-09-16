import numpy as np
import pandas as pd

data = {'age': [27, 28,29, None, 30,31,32,None,29,22],'height': [160, 162, 165, None,167,None,168,169,None,170],'weight': [56, 57, 58 ,59,60,None,61,62,None,65],'city': ['kolkata', 'np.nan', 'up', 'bihar','kanpur','np.nan','china','kolkata','np.nan','farnea'],'marks': [60, 65, None, 70,75,78,79,80,81,82]}
df = pd.DataFrame(data)
print(df)

print("Total missing values", df.isnull().sum())

df_drop=df.dropna()

print(df.drop)

df['age'].fillna(df['age'].mean(),inplace=True)
df['height'].fillna(df['height'].median(),inplace=True)
df['weight'].fillna(method='ffill',inplace=True)
df['city'].fillna(df['city'].mode()[0],inplace=True)
df['marks'].fillna(method="bfill",inplace=True)
print(df)

from sklearn.preprocessing import MinMaxScaler, StandardScaler

mm = MinMaxScaler()
std = StandardScaler()

df[['mm_age', 'mm_height']] = mm.fit_transform(df[['age', 'height']])
df[['std_wt', 'std_height']] = std.fit_transform(df[['age', 'height']])
print(df)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['le_city'] = le.fit_transform(df['city'])
print(df)

