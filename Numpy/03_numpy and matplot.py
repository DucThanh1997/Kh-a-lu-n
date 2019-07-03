import numpy as np
import matplotlib.pyplot as plt



x = np.arange(5)
print("In ra từ 0 đến 4: ", x, "và loại của nó là: ", type(x))
# Phải chạy từng cái 1 không chạy hết được
y = x
# x là tọa độ Ox y là toạn độ của Oy
# In ra các điểm
plt.plot(x, y, "o")
plt.show()
# In ra các điểm có nối
plt.plot(x, y, "o-")
plt.show()
# In ra các điểm có nối không liền
plt.plot(x, y, "o--")
plt.show()
# Gộp 2 bảng
plt.plot(x, y, "o--")
plt.plot(x, -y, "o--")
plt.show()

N = 11
x_1 = np.linspace(0, 11, N)
print("in ra các số từ 0 đến 10 cách nhau N đơn vị: ", x_1)

plt.plot(x, y, "o--")
plt.axis("off")
plt.show()
# Không có trục tọa độ chỉ có đường kẻ thôi


print("sử dụng hàm logarit: ", np.logspace(0, 100, 3))
