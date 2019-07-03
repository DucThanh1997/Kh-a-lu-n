import numpy as np


x = np.empty([3, 3], np.uint8)
print("in ra 1 mảng có 3 dòng 3 cột và random phần tử: " + "\n", x)
print("\n")

y = np.eye(3, dtype=np.uint8)
print("in ra mảng có 3 dòng 3 cột và đường chéo bằng 1: " + "\n", y)
print("\n")

y_1 = np.eye(5, dtype=np.uint8, k=1)
print("như trên nhưng dịch 1 sang bên phải 1 đơn vị:" + "\n", y_1)


print("nếu để là k=-1 thì nó sẽ lùi về bên trái")
print("\n")
print("\n")

z = np.ones((2, 5, 5), dtype=np.int16)
print("in ra mảng np có 2 ma trận 5 dòng 5 cột vs tất cả các phần tử là 1: " + "\n", z)

print("tương tự với zeros sẽ in ra phần tử toàn 0")
print("\n")

z_1 = np.ones((2, 5, 5, 3), dtype=np.int16)
print("in ra mảng np có 2 mảng mỗi mảng có 5 ma trận 5 dòng 3 cột vs tất cả các phần tử là 1: " + "\n", z_1)
print("\n")

m = np.full((2, 3, 3), dtype=np.int16, fill_value=2)
print("in ra mảng np có 2 ma trận 3 dòng 3 cột và các phần tử là 2" + "\n", m)
print("\n")

tri_1 = np.tri(3, 3, k=-1, dtype=np.uint16)
print("In ra mảng có 3 cột 3 dòng -1 lùi về trái 1 đơn vị giống cahchs sử dụng k ở np.eye: " + "\n", tri_1)
print("\n")

x = np.ones((5, 5), dtype=np.uint8)
tri_2 = np.tril(x, k=2)
print("in ra ma trận x với chỉ số tam giác lệch phải 2 đơn vị" + "\n", tri_2)
print("\n")

tri_3 = np.triu(x, k=2)
print("đảo lại của tri_2" + "\n", tri_3)
