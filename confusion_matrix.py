import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

y_act=[1,1,1,0,0,1,0,1,0]
y_pred=[1,1,0,1,1,0,1,1,0]
cm = confusion_matrix(y_act,y_pred)
print("confusion matrix: \n", cm)

tn, fp, fn, tp = cm.ravel()
print(f"True Positive= {tp} ")
print(f"True Negative= {tn} ")
print(f"False Positive= {fp} ")
print(f"False Negative= {fn} ")

print("Accuracy: ", accuracy_score(y_act, y_pred))
print("Precision, Recall, F1-score: \n", classification_report(y_act, y_pred))

plt.figure(figsize=(5,6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()