import pandas as pd
from  sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

data = {
    'Height': [170, 160, 175, 165, 180, 158],
    'Weight': [85, 55, 70, 80, 75, 50],
    'HairLength': [5, 20, 4, 18, 8, 22],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

l_G = LabelEncoder()

X = df[['Height', 'Weight', 'HairLength']]
y = l_G.fit_transform(df['Gender'])

# Train the model
model = GaussianNB()
model.fit(X, y)

# Make predictions
query = {'Height': 168, 'Weight': 62, 'HairLength': 15}
query_df = pd.DataFrame([query])
predictions = model.predict(query_df)
print(l_G.inverse_transform(predictions))