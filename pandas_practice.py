import pandas as pd
dict={
    "Name":["Ashish","Raj","Ram"],
    "Age":[27,28,29],
    "Salary":[50000,60000,70000]
}
df=pd.DataFrame(dict)
print(df)
print("Summary", df.describe())