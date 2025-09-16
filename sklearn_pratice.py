import pandas as pd

df=pd.read_csv("Salary_Data.csv")
print(df)

print(df.head())

from sklearn.model_selection import train_test_split

x=df[["YearsExperience"]]
y=df[["Salary"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=42)

print("x-train\n",x_train)
print("x-test\n",x_test)
print("y-train\n",y_train)
print("y-test\n",y_test)

print("Summary:",df.describe())