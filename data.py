import pandas as pd

data={
    "Exp":[5,6,7,8,9,10,11,12,13,14],
    "Salary":[27000,28000,29000,30000,31000,32000,33000,34000,35000,36000]
}

df=pd.DataFrame(data)
print(df)

#export df data into csv file
df.to_csv("user.csv")

#read csv file
df=pd.read_csv("user.csv")
print(df)

print(df.head())

from sklearn.model_selection import train_test_split

x=df[["Exp"]]
y=df[["Salary"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=42)

print("x-train\n",x_train)
print("x-test\n",x_test)
print("y-train\n",y_train)
print("y-test\n",y_test)

print("Summary:",df.describe())