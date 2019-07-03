import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# # filter đơn giản so sánh hơn kém bằng
# # phép and dùng lệnh &
# # phép hoặc dùng lệnh |
# colnames = ["star_rating", "title", "content_rating", "gerne", "duration", "actors_list"]
# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv", sep=",", header=None, names=colnames)
# # Chạy cái này trả về True False
# print((data.content_rating == "R"))
#
# # Chạy cái này trả về bảng đầy đủ thông tin các bản ghi thỏa mãn điều kiện
# print(data[(data.gerne.isin == "Crime")])

# Cả 2 đều trả về true false




# # Cách lấy riêng từng cột ra
# colnames = ["title", "genre"]
# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                    sep=",", usecols=colnames)
# print(data)

# # Chỉnh số dòng lấy ra bằng nrow
# colnames = ["title", "genre"]
# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                    sep=",", usecols=colnames, nrows=5)
# print(data)
#
#
#
#
# # Chạy iterate qua data frame
# for i in data.title:
#     print(i)
#
# for index, row in data.iterrows():
#     print(index, row.title, row.genre)



# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                     sep=",")
#
# print("Trung bình của các cột có chỉ số numerix: ", data.mean())
# print("Trung bình của các dòng có chỉ số numerix: ", data.mean(axis=1))




# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                     sep=",")
# print("In ra in hoa: ", data.title.str.upper())
# print("replace method: ", data.actors_list.str.replace("[", " ").str.replace("]", " "))
# print("In ra những cái chứa cái chữ the: ", data[data.title.str.contains("The")])




# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                      sep=",")
# # gán kiểu giá trị cho cột duration
# data.duration = data.duration.astype(float)
# print(data.dtypes)
#
# # Chúng ta cũng có thể gán ngay từ đầu khi đọc file
# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                      sep=",", dtype={"duration": float})
# print(data.dtypes)



# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                     sep=",")
# print("In ra trung bình duration group by genre: ", data.groupby("genre").duration.mean())
# # Các bạn không chỉ dùng mỗi mean mà còn có thể dùng max min median
# print("In ra trung bình duration group by genre: ", data.groupby("genre").agg(["min", "max", "mean", "count", "median"]))





# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                      sep=",")
# print("chi tiết genre: " + "\n", data.genre.describe())
# # count số bản ghi
# # unique có 16 tên riêng
# # xuất hiện nhiều nhất là drama với 279
#
# print("đếm số lần xuất hiện: " + "\n", data.genre.value_counts())
#
# print("đếm số lần xuất hiện theo tần suất lấy top5: " + "\n", data.genre.value_counts(normalize=True).head())
#
# print("in ra hết giá trị unique: ", data.genre.unique())
#
# print("check xem phim được rate như nào: ", pd.crosstab(data.genre, data.content_rating))





# data = pd.read_csv("https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv",
#                     sep=",")
# data.duration.plot(kind="hist")
# # In ra mô hình số lượng
# # plt.show()
# data.genre.value_counts().plot(kind="bar")
# plt.show()






# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")
# print("Check xem những cái nào null: " + "\t", data.isnull().head())
# print("Check xem những cái nào không null: " + "\t", data.notnull().head())
# print("Tổng số null: ", data.isnull().sum())
#
# print("Những dòng có city là null: ", data[data.City.isnull()])




# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")
# print("In ra các giá trị index bắt đầu từ đây, kết thức ở đâu, khoảng cách như nào: ", data.index)
#
# print("In ra các cột: " + "\n", data.columns)
#
# print("Cách set cột làm index: ", data.set_index("City", inplace=True))
#
# print(data.head())





# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")
#
# print("in ra dòng đầu tiên: ", data.loc[0, :])
# print("in ra dòng 0, 1, 2, 3: ", data.loc[[0, 1, 2, 3], :])
# print("in ra dòng 0, 1, 2, 3: ", data.loc[0:3, :])
# print("in ra dòng 0, 1, 2, 3: ", data.loc[0:3, :])
#
# print(data.loc[:, "City":"State"])




# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")
#
# print("In ra phần tử theo tọa độ: ", data.iloc[0, 0])
# print("In ra từ dòng 0 đến dòng 2 và cột 1 đến cột 3: ", data.iloc[0:3, 1:4])



# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv")
# print("Xóa cột đi: " + "\n", data.drop("continent", axis=1, inplace=True).head())
# # nếu bạn để inplace = True nó sẽ xóa vĩnh viên luôn còn nếu bạn để không để nó chỉ hiển thị mỗi lần đấy thôi




# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv")
# print("thông tin : ", data.info(memory_usage="deep"))
# print("độ lớn dữ liệu tính theo byte: ", data.memory_usage(deep=True))



# # Như các bạn thấy continent chỉ có 6 giá trị unique nhưng lại độn lên khoảng lưu trữ rất lớn nên tư tưởng
# # t sẽ đưa nó về dạng category
# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv")
# data["continent"] = data.continent.astype("category")
# print(data.continent.cat.codes.head())
# print("độ lớn dữ liệu tính theo byte: ", data.memory_usage(deep=True))
# # bây giờ các bạn thấy độ lớn của continent giảm đi hơn 10 lần



# # Bây giờ t sẽ chỉ cho các bạn cách tạo ra data.frame bằng tay
# data = pd.DataFrame({"Id": [1, 2, 3, 4], "customer name": ["Tom", "Harry", "Peter", "Thomas"]})
# print(data)




# # lấy random các dòng
# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")
# print(data.sample(n=5, random_state=45))
# # nếu để random_state là các số bằng nhau thì lần nào nõ cũng sẽ in ra kết quả nhủ cũ


# Dummy code
# # Nó đưa các giá trị về 0 với 1 để tránh trùng lặp
# # ví dụ
# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/titanic_train.csv")
# # đầu tiên sẽ bỏ sex đi
# # thay vào đó là 1 trường có tên là isMale nếu là Male thì là 1 còn lại là 0
# data["IsMale"] = data.Sex.map({"male": 1, "female": 0})
# print(data.head())
# # bây giờ xóa cột sex đi được rồi
# data.drop("Sex", axis=1, inplace=True)
# print(data.columns)
#
# # bây giờ xem cái embarked này có 3 giá trị tiêng là S C Q
# # ta cũng sẽ làm như Sex
# embark = pd.get_dummies(data.Embarked, prefix="dummy").iloc[:, :]
# print(embark)
# data = pd.concat([data, embark], axis=1)
# print(data.columns)



# data = pd.DataFrame({"Id":[1,2,3,4,1,2,3,4,1,2,3,4],
#                   "name": ["Tom", "Harry", "Peter", "Thomas","Tom", "Harry", "Peter", "Thomas","Tom", "Harry", "Peter", "Thomas"]})
#
# print("cái nào trả trùng sẽ trả về True dựa vào bạn để first hay last: ", data.name.duplicated(keep="first"))
# print("tính số dòng bị trùng: ", data.name.duplicated(keep="first").sum())


# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")
# # chúng ta sẽ đưa cột time về kiểu datetime bằng lệnh
# data["Time"] = pd.to_datetime(data.Time)
# print(data.head())

# chúng ta cũng có thể truy cập từng phần tử ngày giờ phút giây bằng câu lệnh
# data.Time.dt.minute
# còn rất nhiều hàm hay ho nữa mà các bạn cũng có thể search trên mạng form nó như này data.Time.dt. chỉ khác cái
# dấu chấm đằng sau thôi


# data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv")
# print(data.head())
# data["wine"] = data.wine_servings * 10000
# print(data.head())




# print("Show ra những option có chữ html: ", pd.describe_option("html"))
# print("Reset lại toàn bộ option: ", pd.reset_option("html"))
#
# print("Kiểm soát sự sắp xếp khi tạo data frame bằng tay bằng cách: " + "\n",
#       pd.DataFrame({"id": [1, 2, 3], "name": ["Ravi", "Ramu", "Prasad"]}, columns=["id", "name"]))





# print(pd.DataFrame({"id":np.arange(1,11,1), "grades": np.random.randint(0, 101, 10)}, columns=["id", "grades"]))
# a = pd.DataFrame({"id": [1, 2, 3], "country": ["India", "Us", "Germany"]}, index=["x", "y", "z"], columns=["id", "country"])
# print(a)
#
# b = pd.Series(["Washington", "Berlin"], index=["y", "z"], name="capital")
# print(b)
# print(pd.concat([a,b], axis=1))

df = pd.DataFrame([[16, 1, 2017], [16, 2, 2017], [16, 3, 2017]], columns=["days", "month", "year"])
print(pd.to_datetime(df))
