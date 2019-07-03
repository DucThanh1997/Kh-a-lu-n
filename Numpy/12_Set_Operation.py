import numpy as np

data = np.array([[1, 2, 3],
                [3, 2, 1],
                [4, 5, 3]])

print(np.unique(data))
a = np.array([1, 2])
print(np.in1d(data, a))

data1 = np.array([0, 1, 1, 3])
data2 = np. array([1, 2, 2, 3])
print("In ra những cái giống nhau: ", np.intersect1d(data1, data2))
print("In ra cái khác nhau chỉ ở argument đầu tiên: ", np.setdiff1d(data1, data2))
