from sklearn.datasets import load_breast_cancer
from id3 import Id3Estimator
from id3 import export_graphviz
import pandas as pd

estimator = Id3Estimator()
dataset = pd.read_csv('C:/Users/Thanh/Desktop/company.csv', encoding = "utf-8")

label = dataset.iloc[:, -1]

features = dataset.iloc[:, :-1]


estimator.fit(features, label)


    
    
    
    
   