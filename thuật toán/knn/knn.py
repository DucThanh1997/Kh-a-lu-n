import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier

# names = ['ID', 'Age', 'Gender', 'Education', 'Mariage', 'Properites', 'Salary', 'Debt', 'TimeToPay', 'BadDebt']

dataset = pd.read_csv('C:/Users/Cuong/Desktop/hoc/Khoa_luan/thuat_toan/knn/Book1.csv', encoding = "utf-8")

le = LabelEncoder()
for x in range(2,6):
    value = dataset.iloc[:, x].values
    changed = le.fit_transform(value)
    dataset.iloc[:, x] = changed
    for y in range(0,15):
        if dataset.iloc[y, x] != dataset.iloc[15, x]:
            dataset.iloc[y, x] = dataset.iloc[15, x] + 1

mm_scaler  = preprocessing.MinMaxScaler()
value = dataset.iloc[:, [1,6,7]].values
changed = mm_scaler.fit_transform(value)
dataset.iloc[:, [1,6,7]] = changed

print(dataset)

X_train = dataset.iloc[:15, 1:9].values
X_test = dataset.iloc[15:, 1:9].values


y_train = dataset.iloc[:15, 9].values
y_test = dataset.iloc[15:, 9].values



classifier = KNeighborsClassifier(n_neighbors=4)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print("a: ", y_pred)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))