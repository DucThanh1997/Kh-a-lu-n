import Chefboost as chef 
import pandas as pd 


df = pd.read_csv("dataset/golf2.txt")
config = {"algorithm": "CART"}

model = chef.fit(df.copy(), config)

test = df.iloc[2]

print(chef.predict(model, test))


