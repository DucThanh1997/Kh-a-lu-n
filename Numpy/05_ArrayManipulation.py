import numpy as np


x = np.arange(6)
print("In ra các phần tử từ 0 đến 5: " + "\n", x)
print("\n")

y = x.reshape((3, 2))
print("reshape lại x thành 1 ma trận 3 dòng 2 cột: " + "\n", y)
print("\n")

x = np.array([[0, 1, 2], [3, 4, 5]], dtype=np.uint8)
print("In ra ma trận 2 dòng 3 cột: " + "\n", x)
print("\n")

print("bây giờ chúng ta sẽ reshape lại thành 1 dòng 6 cột")
y = np.reshape(x, 6)
print(y)
print("\n")

print("Cách khác")
print(np.ravel(x, "K"))
print("\n")

print("Cách khác 2")
print(x.flatten("C"))
print("\n")

print("In kiểu này sẽ khác. Khác ở chỗ bình thường đọc dòng xuống dòng còn khi đặt biến F là từ cột sang cột theo chiều"
      " từ phải sang")
print(x.flatten("F"))
print("\n")



print(" Bây giờ chúng ta sẽ học cách gộp 2 mảng vào với nhau")
x = np.array([1, 2, 3], dtype=np.uint8)
y = np.array([4, 5, 6], dtype=np.uint8)
print("\n")

print("dùng lệnh stack chúng ta có: ")
print(np.stack((x, y), axis=0))
print("\n")

print("với axis = -1 thì sẽ là 3 dòng 2 cột ngược lại ở trên")
print(np.stack((x, y), axis=-1))
print("\n")

print("dùng lệnh dstack sẽ đưa chúng ta vào 1 mảng nhiều chiều")
print(np.dstack((x, y)))
print("\n")

print("dùng hstack sẽ đưa thành 1 dòng: ")
print(np.hstack((x, y)))
print("\n")

print("dùng vstack sẽ giống với stack thường")
print("\n")

print("sau đây sẽ dùng split: ")

x = np.arange(9)
a, b, c = np.split(x, 3)
print("tách x có 9 phần tử ra thành 3 mảng con a,b,c")
print(a, b, c)
print("\n")

print("tạo mảng 4 chiều có chứa các ma trận 4 dòng 4 cột vs phần tử ngẫu nhiên:")
x = np.random.rand(4, 4, 4)
print(x)
print("\n")
print("\n")



print("tách mảng x ra thành 2 mảng con y và z")
y, z = np.split(x, 2)
print("y")
print(y)
print("\n")
print("z")
print(z)
print("\n")
print("\n")


print("bây giờ chúng ta sẽ nghịch flip")
print("tạo 1 mảng có 16 phần tử từ 0 đến 15 và 4 dòng 4 cột")
x = np.arange(16).reshape(4, 4)
print(x)

print("\n")
print("flip làm cho các giá trị chuyển từ trái sang phải với giá trị axis=-1, tương tự với fliplr nhưng "
      " fliplr không cần phải cho axis vào")
print(np.flip(x, axis=-1))

print("\n")
print("flip làm cho các giá trị chuyển từ trên xuống dưới với giá trị axis=0 tương tự với flipud")
print(np.flip(x, axis=0))

print("\n")
print("flip roll nó khá buồn cười nó kiểu đảo từ dưới lên trên đi theo hàng, nghịch 1 lúc sẽ hiểu")
print(np.roll(x, 2))
