import numpy as np


print("với mảng 1 chiều nhân vào như nhau: ", np.dot(3, 4))

a = np.array([1, 2], np.uint8)
b = np.array([3, 4], np.uint8)

print("như trên 1*3 + 2*4: ", np.dot(a, b))

a = np.array([[1, 2], [3, 4]], np.uint8)
b = np.array([[5, 6], [7, 8]], np.uint8)
print("nhưng từ mảng 2 chiều trở lên sẽ dùng nhân 2 ma trận với nhau: ", np.dot(a, b))

a = np.random.rand(10, 5)
b = np.random.rand(5, 2)
c = np.random.rand(2, 3)
d = np.random.rand(3, 4)
print("Nhân nhiều ma trận với điều kiện dòng ma trận này phải bằng cột ma trận kia: ", np.linalg.multi_dot([a, b, c, d]))

print("\n")
print("\n")

print("Bây giờ nghịch đến vdot")

vector_a = 2 + 3j
vector_b = 4 + 5j
print("vector_a: ", vector_a)
print("vector_b: ", vector_b)
product = np.inner(vector_a, vector_b)
print(product)

print("nó là như này: 2(4 – 5j) + 3j(4 – 5j)")
print("= 8 – 10j + 12j + 15")
print("= 23 – 2j")


