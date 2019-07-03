import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10 , 10)
print(x)

y = np.log10(x)
print("log(x): ", y)

plt.plot(x, y, "o-")
plt.show()

# giải đáp thắc mắc

# A = [[a1,b1],[c1,d1]]
# B = [[a2,b2],[c2,d2]]
# numpy.inner(A,B)
# array([[a1*a2 + b1*b2, a1*c2 + b1*d2],
#        [c1*a2 + d1*b2, c1*c2 + d1*d2])

# numpy.vdot cũng giống dot nhưng làm được mảng khác chiều nhau bằng cách làm phẳng chúng ra
# numpy.convolve có 3 kiểu full lấy hết full bỏ border thôi valid chỉ lấy cái ở giữa chùng
