import pandas as pd
import numpy as np

data = {
    'Patient_ID':[101,102,103,104,105,106,107],
    'Age':[25,30,28,np.nan,45,50,29],
    'Weight':[58,75,np.nan,55,85,90,np.nan],
    'BloodPressure':[120,np.nan,130,110,140,150,np.nan],
    'Cholesterol':[200,210,220,190,np.nan,250,230],
    'Gender':['Male','Female','Male','Female','Male','Male','Female']
}

df = pd.DataFrame(data)

print(df.isnull().sum())

df_drop=df.dropna()

print(df.drop)

df['Patient_ID'].fillna(df['Patient_ID'].mean(),inplace=True)
df['Age'].fillna(df['Age'].median(),inplace=True)
df['Weight'].fillna(method='ffill',inplace=True)
df['BloodPressure'].fillna(df['BloodPressure'].mode()[0],inplace=True)
df['Cholesterol'].fillna(method="bfill",inplace=True)
print(df)