import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

names = ['ID', 'Age', 'Gender', 'Education', 'Mariage', 'Properites', 'Salary', 'Debt', 'TimeToPay', 'BadDebt']

dataset = pd.read_csv('', names=names)

dataset.head()