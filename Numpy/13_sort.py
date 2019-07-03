import numpy as np

data = np.array([[1, 2, 3],
                [3, 2, 1],
                [4, 5, 3]])

print("sắp xếp theo trục: ", np.sort(data, axis=0))
print("sắp xếp theo dòng: ", np.sort(data))
print("tìm xem có bao số không là không: ", np.count_nonzero(data))
