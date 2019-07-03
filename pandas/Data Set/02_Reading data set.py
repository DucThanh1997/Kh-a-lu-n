import pandas as pd

# đọc file csv


# # sep để đánh dấu phân cách
# # header=None để bỏ tên cột đi
# # đặt tên cột colsname phải là 1 list hoặc set

colnames = ["order_id", "quantity","item_name", "choice_description", "item_price"]
data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv", sep="\t", header=None, names=colnames)

print("đọc 5 cái đầu: " + "\n", data.head())
print("số dòng số cột: ", data.shape)
print("đọc 5 cái cuối: ", "\n", data.tail())

print(data["item_name"])
print(data.item_name)
print(type(data))

# 2 cột có cùng kiểu có thể kết hợp với nhau bằng cách cộng

print("cộng cột order_id với itemprice: ", data["order_id"] + data["item_price"])

# ta có thể in ra tất tần tật thông số trung bình, trung vị, max, count bằng lệnh describe()
data.describe()

# Chúng ta có thể in ra hết tên cột bằng lệnh culumns
print(data.columns)

# Chúng ta có thể đổi tên cột bằng lệnh
data.rename(columns={"item_price": "giá"}, inplace=True)
print(data.columns)

# Nhanh hơn có cách này
cols = ["1", "2", "3", "4", "5"]
data.columns = cols

# chúng ta có thể replace hết các phần tử mà chúng ta muốn bằng lệnh
# data.columns.str.replace("_","")


# xóa dòng
# data.drop("giá", axis=1, inplace=True)
# xóa 2 cột data.drop(["order_id", "giá", axis=1, inplace=True)
# xóa dòng data.drop([0,1,2], axis=0, inplace=True)


# sắp xếp data.set
# tách 1 cột ra rồi sắp xếp data["giá"].sort_values()
# tách 1 cột ra rồi sắp xếp giảm dần data["giá"].sort_values(ascending=False)
# sắp xếp cả data set theo 1 cột: data.sort_values("giá")



# filter
# data[data.duration] > 175

