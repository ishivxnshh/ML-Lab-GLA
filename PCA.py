import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

#Question-1
data={
    "x":[4,6,8,9],
    "y":[10,20,30,40]
}

df=pd.DataFrame(data)
print(df)

x=df-df.mean()
print(x)
Cov_matrix=np.cov(x.T)
print("covarience_matrix:",Cov_matrix)

pca=PCA(n_components=2)
x_pca=pca.fit_transform(x)
print("eigenvalues:\n", pca.explained_variance_,"\n")
print("eigenvectors:\n",pca.components_,"\n")
print("projection:\n",x_pca,"\n")

print("\n")
print("\n")


#Question 2
data={
    "x":[3,5,8,9],
    "y":[6,7,5,10]
}

df=pd.DataFrame(data)
print(df)

x=df-df.mean()
print(x)
Cov_matrix=np.cov(x.T)
print("covarience_matrix:",Cov_matrix)

pca=PCA(n_components=2)
x_pca=pca.fit_transform(x)
print("eigenvalues:\n", pca.explained_variance_,"\n")
print("eigenvectors:\n",pca.components_,"\n")
print("projection:\n",x_pca,"\n")