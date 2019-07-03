import numpy as np


x = np.array([[1, 2, 3], [4, 5, 6]], np.int16)
print("mảng x: ", x)
print("\n")

print("in cột 2 của x: ", x[:, 1])
print("\n")

print("in dòng 1 của x: ", x[0, :])
print("\n")
print("\n")

y = np.array([[[1, 2, 3], [4, 5, 6]], [[-1, -2, -3], [-4, -5, -6]]], np.int16)
print("mảng 2 chiều y : ", y)
print("\n")

print("in ra phần tử thứ nhất trong dòng thứ nhất ở mảng thứ nhất của y:", y[0, 0, 0])
print("\n")

print("in ra ở cả 2 mảng dòng 2 côt 3 của y: ", y[:, 1, 2])
print("\n")

print("số mảng, số dòng, số cột của y: ", y.shape)
print("\n")

print("in ra số cột của y:", y.ndim)
print("\n")

print("in ra kiểu dữ liệu của y:", y.dtype)
print("\n")

print("mảng np có thể được coi là 1 ma trận nên chúng ta có thể đảo chiều x từ 2 dòng 3 cột thành 3 dòng 2 cột: ", x.T)
print("\n")
print("\n")

print("In ra các giá trị mặc định")
print("Dương vô cùng:", np.Inf)
print("\n")
print("Not a number:", np.NAN)
print("\n")
print("âm vô cùng:", np.NINF)
print("\n")
print("âm 0: ", np.NZERO)
print("\n")
print("dương 0: ", np.PZERO)
print("\n")
print("số e: ", np.e)
print("\n")
print("euler: ", np.euler_gamma)
print("\n")
print("số pi: ", np.pi)



