import Chefboost as chef 
import pandas as pd 


df = pd.read_csv("dataset/golf2.txt")
config = {"algorithm": "CART"}

model = chef.fit(df.copy(), config)

test = ["Sunny",90,85,"Strong"]

print(chef.predict(model, test))

# tim cach luu model
# lay source code va tim hieu no, cau hinh tham so dau vao 
# lam cai form de nguoi ta nhap dau vao (web)

