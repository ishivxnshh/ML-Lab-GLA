# importing libraries
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# data loading
data = {'Age': ['Young', 'Young', 'Middle', 'Old', 'Old', 'Middle'], 'Obesity': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No'], 'BP': ['High', 'Normal', 'High', 'Normal', 'Normal', 'High'], 'Diabetes': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No']}
df = pd.DataFrame(data)

# data preprocessing
le_age, le_ob, le_bp, le_di = LabelEncoder(), LabelEncoder(), LabelEncoder(), LabelEncoder()
X = pd.DataFrame({
    'Age': le_age.fit_transform(df['Age']),
    'Obesity': le_ob.fit_transform(df['Obesity']),
    'BP': le_bp.fit_transform(df['BP']),
})
Y = pd.DataFrame({
    'Diabetes': le_di.fit_transform(df['Diabetes'])
})
print(X)
print(Y)

# using model
model = CategoricalNB()
model.fit(X, Y.values.ravel())

# query
query = {'Age': 'Young', 'Obesity': 'Yes', 'BP': 'Normal'}
q = pd.DataFrame({
    'Age': [le_age.transform([query['Age']])[0]],
    'Obesity': [le_ob.transform([query['Obesity']])[0]],
    'BP': [le_bp.transform([query['BP']])[0]],
})
pred = model.predict(q)
print("Predicted Diabetes:", le_di.inverse_transform(pred))