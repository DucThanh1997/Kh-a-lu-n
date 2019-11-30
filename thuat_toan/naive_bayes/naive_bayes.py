import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.naive_bayes import GaussianNB

# load data
dataset = pd.read_csv('C:/Users/Cuong/Desktop/hoc/Khoa_luan/thuat_toan/naive_bayes/data.csv', encoding = "utf-8")

# encode
le = LabelEncoder()



value = dataset.iloc[:, 0].values
changed = le.fit_transform(value)
dataset.iloc[:, 0] = changed

## set nhãn và tính năng
label = dataset.iloc[:, 0]

features = dataset.iloc[:, 1:]

## train và dự đoán
model = GaussianNB()

model.fit(features, label)


predicted = model.predict([[1,1,1]]) 
print("Predicted Value:", predicted)