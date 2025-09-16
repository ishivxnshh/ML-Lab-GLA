import pandas as pd
df=pd.read_csv('Salary_Data.csv')
print(df)
from sklearn.model_selection import train_test_split
x=df[['YearsExperience']]
y=df[['Salary']]
x_train,x_text,y_train,y_text=train_test_split(x,y,test_size=0.3)
print("x_train",x_train)
print("x_text",x_text)
print("y_train",y_train)
print("y_text",y_text)
print(df.head())
print("summary",df.describe())